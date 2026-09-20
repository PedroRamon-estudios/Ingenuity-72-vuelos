# Reproducing the analysis and understanding its scope

[Español](REPRODUCIR_ANALISIS.md) · [English explorer](index-en.html)

## Acoustic figures in Spanish and English

The spectral and minima figures were regenerated for edition 1.4.2 from the four calibrated PDS `p02` WAV files and the original JPL test capture supplied for the study. English titles, axes, legends and phase labels use the same calculations and recordings.

1. Install Python and the recorded package versions:

   ```sh
   python -m pip install -r analisis/requirements.txt
   ```

2. Download the four WAV files using the `pds_wav` addresses in `datos/audio_ingenuity_pds.csv`. Save them in a working directory as `flight4.wav`, `flight5.wav`, `flight6.wav` and `flight8.wav`.

3. Exact reproduction of the ground comparison requires the original 94.848-second capture, containing mono AAC audio at 48,000 samples/s. This capture is not redistributed. The public source is the JPLraw video linked in the analysis. Another YouTube download may have different encoding or timing and cannot guarantee the same result. Extract the original capture's audio without trimming or changing the sample rate:

   ```sh
   ffmpeg -i CAPTURE.mp4 -vn -c:a pcm_f32le work/jpl-test-audio.wav
   ```

4. Run from the project root:

   ```sh
   python analisis/comparar_audio.py --pds-dir work --jpl-wav work/jpl-test-audio.wav --output figures --language es
   python analisis/comparar_audio.py --pds-dir work --jpl-wav work/jpl-test-audio.wav --output figures --language en
   ```

The WAV input SHA-256 hashes and library versions are recorded in `analisis/inputs.json`. Listening-preview MP3 files cannot replace these WAV inputs.

## What the program does

It calculates normalised Welch spectra, the filtered flight 5 envelope and the combined harmonic energy of the ground test. Windows, bands and normalisations are specified in the code. Language changes labels and output filenames, not calculations.

Minima markers and test phases are previously measured annotations explicitly entered as `JPL_DIPS`, `F5_NULLS` and `JPL_PHASES`. The program does not automatically detect those timings or recalculate the fourteen-peak fit. Those results are documented separately in the acoustic analysis.

## Visual metric

Tabulated outputs, percentiles and statistical checks are preserved. The original visual-extraction program, thresholds and exact score weights are not included. Full reproduction therefore remains partial. No new formula has been substituted for the missing procedure.

Official facts, observations and hypotheses remain distinct. This editorial revision does not turn the study's hypotheses into official accident findings.
