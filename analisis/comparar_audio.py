#!/usr/bin/env python3
# Copyright (c) 2026 Pedro Ramón Montserrat Cabrera.
# Fuerteventura, Islas Canarias, España. Todos los derechos reservados.
# Consulte ../LICENSE para las condiciones de uso.
"""Genera figuras comparables a partir de los WAV PDS y la referencia JPL.

Fuente audiovisual JPL:
https://www.youtube.com/watch?v=nAQxNd3uBN0&t=148s

Uso:
    python analisis/comparar_audio.py \
        --pds-dir .. \
        --jpl-wav ../jpl-test-audio.wav \
        --output assets/analisis

El programa compara posiciones espectrales y envolventes normalizadas. No
compara niveles acústicos absolutos: las cadenas de adquisición son distintas.
"""

from __future__ import annotations

import argparse
from math import gcd
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy.ndimage import gaussian_filter1d
from scipy.signal import butter, hilbert, resample_poly, sosfiltfilt, stft, welch


ACTIVE_WINDOWS = {4: (25.0, 139.0), 5: (18.0, 128.0), 6: (27.0, 66.0), 8: (32.0, 54.0)}
JPL_PHASES = [
    (5.0, "giro"),
    (15.5, "ascenso"),
    (21.0, "giro WP"),
    (23.0, "traslación"),
    (40.0, "hover"),
    (47.5, "giro 180°"),
    (54.0, "retorno"),
    (59.0, "hover"),
    (68.0, "rumbo"),
    (74.0, "aterrizaje"),
]
JPL_DIPS = np.array([15.74, 17.79, 21.38, 24.45, 47.49, 49.79, 52.99, 59.26, 62.59, 64.51, 67.97, 71.94, 74.50])
F5_NULLS = np.array([36.3, 46.8, 57.5, 71.7, 88.2, 103.7])


def read_wav(path: Path) -> tuple[int, np.ndarray]:
    sample_rate, samples = wavfile.read(path)
    samples = np.asarray(samples)
    if np.issubdtype(samples.dtype, np.integer):
        scale = max(abs(np.iinfo(samples.dtype).min), np.iinfo(samples.dtype).max)
        samples = samples.astype(np.float64) / scale
    else:
        samples = samples.astype(np.float64)
    if samples.ndim > 1:
        samples = samples.mean(axis=1)
    samples -= np.mean(samples)
    return int(sample_rate), samples


def normalized_psd(samples: np.ndarray, sample_rate: int, start: float, end: float) -> tuple[np.ndarray, np.ndarray]:
    segment = samples[int(start * sample_rate) : int(end * sample_rate)]
    nperseg = min(65_536, len(segment))
    frequency, power = welch(
        segment,
        sample_rate,
        window="hann",
        nperseg=nperseg,
        noverlap=nperseg // 2,
        nfft=131_072,
    )
    power_db = 10 * np.log10(power + np.finfo(float).tiny)
    selection = (frequency >= 60) & (frequency <= 250)
    power_db -= np.max(power_db[selection])
    return frequency, power_db


def f5_envelope(samples: np.ndarray, sample_rate: int) -> tuple[np.ndarray, np.ndarray]:
    divisor = gcd(sample_rate, 1_000)
    reduced = resample_poly(samples, 1_000 // divisor, sample_rate // divisor)
    reduced_rate = 1_000
    bandpass = butter(4, [81.5, 87.0], btype="bandpass", fs=reduced_rate, output="sos")
    filtered = sosfiltfilt(bandpass, reduced)
    envelope = np.abs(hilbert(filtered))
    envelope_db = 20 * np.log10(envelope + np.finfo(float).tiny)
    envelope_db = gaussian_filter1d(envelope_db, 0.5 * reduced_rate)
    envelope_db -= np.percentile(envelope_db[(np.arange(len(envelope_db)) / reduced_rate >= 20) & (np.arange(len(envelope_db)) / reduced_rate <= 125)], 95)
    time = np.arange(len(envelope_db)) / reduced_rate
    return time, envelope_db


def jpl_comb_envelope(samples: np.ndarray, sample_rate: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    divisor = gcd(sample_rate, 4_000)
    reduced = resample_poly(samples, 4_000 // divisor, sample_rate // divisor)
    reduced_rate = 4_000
    nperseg = 8_192
    hop = 512
    frequency, time, spectrum = stft(
        reduced,
        reduced_rate,
        window="hann",
        nperseg=nperseg,
        noverlap=nperseg - hop,
        nfft=32_768,
        boundary=None,
        padded=False,
    )
    power = np.abs(spectrum) ** 2
    fundamental_band = (frequency >= 70) & (frequency <= 82)
    tracked = frequency[fundamental_band][np.argmax(power[fundamental_band], axis=0)]
    comb = np.zeros_like(time)
    for column, fundamental in enumerate(tracked):
        for harmonic in range(1, 13):
            center = harmonic * fundamental
            narrow = (frequency >= center - 0.9) & (frequency <= center + 0.9)
            comb[column] += np.sum(power[narrow, column])
    comb_db = 10 * np.log10(comb + np.finfo(float).tiny)
    active = (time >= 12) & (time <= 82)
    comb_db -= np.percentile(comb_db[active], 95)
    return time, comb_db, tracked


def make_spectrum_figure(pds: dict[int, tuple[int, np.ndarray]], jpl: tuple[int, np.ndarray], output: Path, language: str = "es") -> None:
    tr = lambda es, en: en if language == "en" else es
    fig, ax = plt.subplots(figsize=(12, 6.75), constrained_layout=True)
    jpl_rate, jpl_samples = jpl
    frequency, power = normalized_psd(jpl_samples, jpl_rate, 15, 80)
    selection = (frequency >= 60) & (frequency <= 250)
    ax.plot(frequency[selection], power[selection], color="#d97706", linewidth=2.0, label=tr("Ensayo JPL · 2.277 rpm", "JPL test · 2,277 rpm"))
    colors = {4: "#2563eb", 5: "#0f766e", 6: "#7c3aed", 8: "#be123c"}
    for flight, (sample_rate, samples) in pds.items():
        start, end = ACTIVE_WINDOWS[flight]
        frequency, power = normalized_psd(samples, sample_rate, start, end)
        selection = (frequency >= 60) & (frequency <= 250)
        ax.plot(frequency[selection], power[selection], linewidth=1.35, alpha=0.9, color=colors[flight], label=tr(f"Perseverance · vuelo {flight}", f"Perseverance · flight {flight}"))
    for value, label in [(75.9, "75,9 Hz"), (84.4, "84,4 Hz"), (151.8, "151,8 Hz"), (168.8, "168,8 Hz")]:
        ax.axvline(value, color="#64748b", linewidth=0.8, alpha=0.5)
        ax.text(value + 1.0, -4, label.replace(",", ".") if language == "en" else label, rotation=90, va="top", ha="left", fontsize=8, color="#475569")
    ax.set_xlim(60, 250)
    ax.set_ylim(-45, 2)
    ax.set_title(tr("Firma tonal normalizada: ensayo terrestre frente a cuatro vuelos en Marte", "Normalised tonal signature: ground test and four flights on Mars"), loc="left", weight="bold")
    ax.set_xlabel(tr("Frecuencia (Hz)", "Frequency (Hz)"))
    ax.set_ylabel(tr("Densidad espectral relativa (dB; máximo de cada registro = 0)", "Relative spectral density (dB; maximum of each recording = 0)"))
    ax.grid(True, color="#cbd5e1", linewidth=0.6, alpha=0.55)
    ax.legend(ncol=2, frameon=False, loc="lower left")
    fig.savefig(output / ("audio-espectros-jpl-perseverance" + ("-en" if language == "en" else "") + ".png"), dpi=180)
    plt.close(fig)


def make_null_figure(flight5: tuple[int, np.ndarray], jpl: tuple[int, np.ndarray], output: Path, language: str = "es") -> None:
    tr = lambda es, en: en if language == "en" else es
    jpl_time, jpl_comb, _ = jpl_comb_envelope(jpl[1], jpl[0])
    f5_time, f5_env = f5_envelope(flight5[1], flight5[0])
    fig, axes = plt.subplots(2, 1, figsize=(13, 8), constrained_layout=True)

    axes[0].plot(jpl_time, jpl_comb, color="#d97706", linewidth=1.4)
    axes[0].scatter(JPL_DIPS, np.interp(JPL_DIPS, jpl_time, jpl_comb), color="#991b1b", s=20, zorder=3, label=tr("mínimos medidos", "Measured minima"))
    phases_en = ["Spin-up", "Ascent", "WP turn", "Translation", "Hover", "180° turn", "Return", "Hover", "Heading", "Landing"]
    for index, (time, label) in enumerate(JPL_PHASES):
        label = phases_en[index] if language == "en" else label
        axes[0].axvline(time, color="#64748b", linewidth=0.7, alpha=0.55)
        axes[0].text(time + 0.25, 1.5 if index % 2 == 0 else -1.0, label, rotation=90, va="top", fontsize=7.5, color="#334155")
    axes[0].set_xlim(5, 85)
    axes[0].set_ylim(-22, 3)
    axes[0].set_title(tr("Ensayo JPL: energía conjunta de los armónicos 1–12", "JPL test: combined energy of harmonics 1–12"), loc="left", weight="bold")
    axes[0].set_ylabel(tr("Nivel relativo (dB)", "Relative level (dB)"))
    axes[0].legend(frameon=False, loc="lower left")

    axes[1].plot(f5_time, f5_env, color="#0f766e", linewidth=1.3)
    axes[1].scatter(F5_NULLS, np.interp(F5_NULLS, f5_time, f5_env), color="#991b1b", s=24, zorder=3, label=tr("nulos medidos", "Measured nulls"))
    for time in [36, 47, 57, 72, 88, 104]:
        axes[1].axvline(time, color="#64748b", linewidth=0.8, linestyle="--", alpha=0.65)
    axes[1].set_xlim(20, 125)
    axes[1].set_ylim(-32, 3)
    axes[1].set_title(tr("Vuelo 5: envolvente de 81,5–87 Hz; líneas discontinuas = tiempos publicados", "Flight 5: 81.5–87 Hz envelope; dashed lines = published timings"), loc="left", weight="bold")
    axes[1].set_xlabel(tr("Tiempo del registro (s)", "Recording time (s)"))
    axes[1].set_ylabel(tr("Nivel relativo (dB)", "Relative level (dB)"))
    axes[1].legend(frameon=False, loc="lower left")
    for ax in axes:
        ax.grid(True, color="#cbd5e1", linewidth=0.6, alpha=0.55)
    fig.savefig(output / ("audio-nulos-jpl-vuelo5" + ("-en" if language == "en" else "") + ".png"), dpi=180)
    plt.close(fig)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pds-dir", type=Path, default=Path(".."), help="Directorio con flight4.wav, flight5.wav, flight6.wav y flight8.wav")
    parser.add_argument("--jpl-wav", type=Path, default=Path("../jpl-test-audio.wav"), help="WAV extraído de la referencia JPL")
    parser.add_argument("--output", type=Path, default=Path("assets/analisis"), help="Directorio de salida")
    parser.add_argument("--language", choices=("es", "en"), default="es", help="Idioma de títulos, ejes y leyendas")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    pds = {flight: read_wav(args.pds_dir / f"flight{flight}.wav") for flight in ACTIVE_WINDOWS}
    jpl = read_wav(args.jpl_wav)
    make_spectrum_figure(pds, jpl, args.output, args.language)
    make_null_figure(pds[5], jpl, args.output, args.language)
    print(f"Figuras guardadas en {args.output.resolve()}")


if __name__ == "__main__":
    main()
