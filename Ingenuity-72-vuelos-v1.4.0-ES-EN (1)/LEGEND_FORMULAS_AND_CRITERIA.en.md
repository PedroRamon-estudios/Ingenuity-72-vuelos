# Legend, formulas and interpretation criteria

## Ingenuity: an extended log of 72 flights, images and sound from Mars

[Español](LEYENDA_FORMULAS_Y_CRITERIOS.md) · [English explorer](index-en.html)

**Analysis, selection and narrative:** Pedro Ramón Montserrat Cabrera  
**Location:** Fuerteventura, Canary Islands, Spain  
**Methodology version:** 19 September 2026  
**Rights:** © 2026 Pedro Ramón Montserrat Cabrera. All rights reserved.

This document explains how to read the site, what each variable represents, which formulas can be verified in the project files and where public data reach their limits. It is intended for students, teachers, science communicators and anyone wishing to examine or reproduce the work.

The project is a personal, independent exercise in technical documentation, curiosity and learning. It brings scattered public sources into one chronology. It is not Ingenuity's internal telemetry, does not replace NASA/JPL analysis and has not been endorsed by those institutions.

## 1. Main rule for interpretation

| Level | Meaning | Example |
|---|---|---|
| **OBSERVED** | Directly visible in an image, audio recording or official source | Few distinguishable terrain features in public flight 72 imagery; NASA/JPL reported loss of visual tracking |
| **REPRODUCED** | Obtained again through a described procedure using public data | Recovering 75.8813 Hz from the JPL test or the six flight 5 minima |
| **HYPOTHESIS** | Physically possible interpretation requiring telemetry, complete original imagery or further testing | Relating a particular landing geometry to blade failure order |

Agreement between independent sources strengthens an explanation but does not automatically turn a hypothesis into a demonstrated fact.

## 2. What the extended log combines

| Layer | Source | Project use |
|---|---|---|
| 72-flight record | NASA Science / JPL | Dates, sols, profiles, distances, altitudes, speeds, durations and incidents |
| Animated 72-flight map | NASA/JPL-Caltech | Spatial context and navigation to each flight label |
| Chronological Navcam montage | Jacint Roger (Landru79), using public imagery | Visual continuity and exploratory feature-analysis input |
| Visual metrics | Project-derived | Uniform, relative comparisons within the same montage |
| SuperCam audio | NASA Planetary Data System | Analysis of flights 4, 5, 6 and 8 |
| Ground test | Public JPL video | Independent harmonic-comb and rotor-speed check |
| Hazard avoidance | NASA/JPL PIA25662 and technical papers | Conceptual comparison with 3D reconstruction, slope, roughness and uncertainty |

Original contributions include selection, organisation, comparison, narrative, code, visualisations and derived results. Third-party facts, images, audio and materials retain their original attribution and terms.

## 3. Main chart legend

| Element | Meaning | Does not mean |
|---|---|---|
| Horizontal axis | Flight number, 1–72 | Continuous time or distance |
| Vertical axis | Relative visual score, 0–100, within this montage | Ingenuity's internal feature count |
| Point | Provisional block assigned to a flight | Instantaneous telemetry sample |
| Line | Visual connection between successive flights to reveal trends | Continuous evolution between flights |
| Highlighted point | Flight selected in the main explorer | Necessarily the flight playing in the map |
| Event marker | Flight with a known test, anomaly or event | Evidence that texture caused the incident |
| Audio marker | Flight 4, 5, 6 or 8 with a studied SuperCam recording | Complete audible coverage of the flight |
| Final band | Flights 68–72 | An official NASA category |

### Editorial score categories

- **Below 20:** low visual references.
- **20 to below 45:** fewer or poorly distributed references.
- **45 or more:** relatively abundant references.

These are internal reading thresholds, not NASA/JPL safety, navigation or certification limits.

### Independent indices

The upper buttons, dropdown, chart and table change the main details and still image. Only the index beside the map seeks and plays that video; playback updates only that index. You can therefore study one flight while the map plays another.

## 4. Visual segmentation and sampling

### 4.1 Frames and time

The montage has \(N_f=22\,546\) frames at \(F_s=25\) fps, lasting \(T=901.84\) s. For frame index \(k\):

\[
t_k=\frac{k}{F_s},\qquad T=\frac{N_f}{F_s}=\frac{22\,546}{25}=901.84\ \text{s}
\]

### 4.2 Flight boundaries

Seventy-five large-shadow passages were identified. Three between flights 13 and 14 were treated as pre-flight checks, giving 72 provisional blocks. Twenty frames from the central segment of each block were sampled so that one extreme image would not alone determine a flight's value.

### 4.3 Timing caveat

The Spanish CSV fields `video_inicio_s` and `video_fin_s` refer to the Landru79 montage. They are neither real seconds after take-off nor official flight durations. English CSV counterparts are `video_start_s` and `video_end_s`.

## 5. Visual variables and formulas

### 5.1 Visual references

Each sample uses a Harris/Shi–Tomasi-like corner/local-feature estimate after vignette cropping and approximate shadow masking. If \(r_{i,k}\) is the feature count in frame \(k\) of flight \(i\), the representative stored value is:

\[
R_i=\operatorname{median}(r_{i,1},r_{i,2},\ldots,r_{i,20})
\]

The median is less sensitive than the mean to exceptionally bright, dark or compressed frames.

### 5.2 Interquartile range

\[
IQR_i=Q_{3,i}-Q_{1,i}
\]

Here \(Q_1\) and \(Q_3\) are the 25th and 75th percentiles. A high IQR means the feature count varies substantially within the block, not necessarily that the helicopter was unstable.

### 5.3 Spatial coverage

Usable imagery is divided into a 4 × 4 grid. Each usable cell is checked for at least two references:

\[
C_i=100\,\frac{\sum_{c\in U_i}\mathbf{1}(n_{i,c}\geq2)}{|U_i|}
\]

\(U_i\) is the usable-cell set after masking; \(n_{i,c}\) is the feature count associated with cell \(c\); the indicator is 1 when the condition is met, otherwise 0. Coverage distinguishes clustered features from a similar number spread across the image.

### 5.4 Feature percentile

The Spanish `percentil_referencias` field can be reconstructed exactly from the CSV. For \(N=72\), let \(q_i\) be the ascending rank of \(R_i\), using average ranks for ties:

\[
P_i=100\,\frac{q_i-1}{N-1}
\]

The minimum is percentile 0 and the maximum 100. Rounding to one decimal reproduces all published values.

### 5.5 Relative visual score

The score is a normalised composite index for ordering blocks within the montage, not a physical quantity.

**Reproducibility:** the package preserves the output CSV and conceptual description but not the original visual-extraction program, thresholds or exact weights used in `puntuacion_visual`. No retrospective formula is invented here.

Until that program is recovered or reconstructed and validated, the final table, stored feature medians, percentiles, statistical comparisons and acoustic code remain auditable; generating the full visual score from video is **partially reproducible**. Publishing the visual detector with library versions, masks, parameters, coverage aggregation and exact scoring formula is the main methodological task outstanding.

### 5.6 Auxiliary variables

| Original CSV field | Permitted reading | Caution |
|---|---|---|
| `textura` | Auxiliary image tonal variation/structure | Not physical roughness or slope |
| `sombra_pct` | Estimated proportion under the shadow mask | Not height or ground proximity |
| `cambio_visual` | Auxiliary change between samples | Not directly speed |
| `dispersion_sombra` | Within-block variation of the shadow measure | Does not diagnose attitude, rotor or servos |
| `confianza_asignacion` | Editorial confidence in block–flight assignment | Not failure probability or landing safety |

Exact formulas for the four numerical auxiliary variables are also absent from the current package and must not be guessed.

## 6. Statistical comparisons

Spearman rank correlation was used to test whether median feature count simply depended on official distance, altitude, speed or duration:

\[
\rho_s=\operatorname{corr}(\operatorname{rank}(X),\operatorname{rank}(Y))
\]

With no ties it can be written:

\[
\rho_s=1-\frac{6\sum d_i^2}{N(N^2-1)}
\]

Here \(d_i\) is the rank difference. For the 72 flights:

| Official variable vs visual features | \(\rho_s\) | \(p\) |
|---|---:|---:|
| Distance | −0.061 | 0.613 |
| Maximum altitude | −0.017 | 0.891 |
| Maximum speed | −0.127 | 0.287 |
| Duration | −0.046 | 0.703 |

No significant monotonic relationship appears. This does not establish terrain causality; it indicates that montage feature counts are not simply explained by longer, higher or faster flights.

### Final-sequence descriptive result

\[
\operatorname{median}(R_{1\ldots67})=46.5,\qquad\operatorname{median}(R_{68\ldots72})=11.0
\]

For flight 72:

\[
R_{72}=8.0,\quad C_{72}=20.83\%,\quad S_{72}=6.1
\]

Persistently low values across several final flights are more informative than an isolated flight 72 image, but do not establish progressive system degradation.

## 7. Flight 9 and hazard avoidance

### 7.1 What NASA/JPL imagery actually shows

PIA25662 uses flight 9 imagery from 5 July 2021, **reprocessed later** with a capability added in a late-2022 software update. Red marks unsuitable landing regions and green marks candidates. Red numbers, cyan markings and white rectangles are not precisely defined in the public description; this project assigns them no units.

The associated technical pipeline comprises monocular imagery, visual–inertial pose estimation, image-pair selection and Structure-from-Motion depth reconstruction, temporal fusion into a multiresolution elevation map, slope/roughness/quality or uncertainty evaluation, a binary safe/hazardous map, and distance-transform selection of candidates away from obstacles.

### 7.2 Does this match our processing?

The initial prerequisite is shared; algorithms and units differ.

| Aspect | JPL system | Project metric | Correspondence |
|---|---|---|---|
| Visible structure | Reconstruction fails or loses confidence without texture | Counts detectable local features | Strong conceptual overlap |
| Spatial distribution | Important for reconstruction and evaluation | Approximated by 4×4 coverage | Conceptual overlap |
| Image sequence | Fuses images and poses over time | Summarises 20 montage images without metric reconstruction | Different methods |
| 3D terrain | Computes depth and elevation | Does not compute depth | Not equivalent |
| Physical slope/roughness | Direct map criteria | `textura` lacks those units | Not numerically comparable |
| Uncertainty | Part of map quality | No equivalent metric variance | Not comparable |
| Site selection | Generates green candidates after excluding hazards | Does not select landing sites | Different purpose |

For flight 9 the project finds median features 12.5, coverage 25% and score 12.9. A low score alongside green JPL candidates is not contradictory: JPL fuses a sequence into 3D geometry; our index uses a compressed public selection without poses or depth.

Rock groups and relief in PIA25662 largely fall within red shading; green candidates lie on visually more uniform regions. This is qualitative. Pixel-level validation would require original imagery, calibration, poses, parameters and intermediate maps.

> Flight 9's video supports visible terrain structure as a prerequisite for reconstructing surroundings and assessing landing sites. Our metric examines that prerequisite in simplified form; it neither reproduces nor calibrates JPL's hazard-avoidance algorithm.

## 8. Landing close to a rock

The archived reference corresponds to **flight 33**, 24 September 2022 (sol 567): a horizontal flight of about 111 m, maximum altitude 10 m, speed 4.75 m/s and duration about 55 s.

### 8.1 The right question

“Why did Ingenuity see the rock and choose to land there?” assumes more than the evidence supports. Flight 33 preceded the late-2022 hazard-avoidance update, and public documentation does not establish autonomous candidate selection on that flight.

The most plausible interpretation is that the ground team planned a destination; Navcam tracked terrain features to estimate horizontal motion; the laser altimeter measured ground distance; the controller sought to arrive and descend within the expected envelope; and the rock remained close to the gear but apparently outside its effective contact footprint. Successful landing need not have involved classifying that rock as an individual hazard.

### 8.2 Compatible explanations, ordered by plausibility

| Possibility | Assessment |
|---|---|
| Rock outside the four-leg footprint and required margin | High; visual proximity is not contact |
| Lower-resolution destination planning plus normal dispersion placed the gear closer | Plausible |
| Overhead perspective, shadow and lack of local scale exaggerate proximity | Plausible, hard to quantify |
| System detected the rock, evaluated risk and accepted it | Not demonstrated for this flight |
| Ingenuity deliberately preferred a ridge or rock | Not supported by public telemetry |

### 8.3 What cannot yet be calculated

Exact rock-to-foot distances, rock size from a compressed capture, leg-contact order, slope under each foot, displacement from the programmed target, and the map or safety margin available to planners remain unknown. Earlier visual estimates of 25–35 cm rock size and 30–40 cm separation are preliminary approximations, not publishable measurements without calibrated geometry.

The image raises a real engineering question: navigable terrain may permit gear contact despite a nearby obstacle. **Visual navigability, geometric safety and four-point stability are different quantities.** The flight 70 dune capture is a separate reference and must not be confused with flight 33.

## 9. The 31–32 ridges hypothesis

### 9.1 Origin and careful formulation

In the LinkedIn series *Anatomía de la Rotura de una Pala del Ingenuity* (Anatomy of an Ingenuity Blade Failure), Pedro Ramón Montserrat Cabrera noted that numerous take-offs, landings or vertical flights appeared to occur on summits, edges, dune slopes or ridges, even where apparently flatter areas were visible in projection.

One archived post explicitly describes **31 images**. “About 32 ridges” approximates the initial investigation, not 32 independently verified landings. It must also remain separate from an earlier preliminary estimate of “about 25 landings”.

> **Hypothesis L:** the reviewed public imagery shows an apparent recurrence of final positions near crests, ridges or elevated sandy areas. Whether this exceeds terrain availability, route bias, image-selection bias and perspective errors remains untested.

This is the author's editorial observation and research question, **not a NASA/JPL conclusion or proof that Ingenuity autonomously preferred ridges**.

### 9.2 Why the question matters

Three distinct problems intersect: ground-team route planning consistent with Perseverance's progress and available imagery; visual navigation requiring adequate texture; and geometric landing safety determined by slope, roughness, rocks and the four-foot footprint. A ridge may offer contrast and no rocks yet be sloped; a seemingly flat area may lack texture or hide obstacles. This makes the question physically reasonable without proving software bias.

### 9.3 Sources of false patterns

- **Sampling bias:** selected public imagery is not a complete calibrated landing sequence.
- **Pseudoreplication:** multiple photographs of one flight are not multiple landings.
- **Perspective:** monocular overhead views may visually shift a crest or footprint.
- **Availability:** many ridges along a dune route do not establish preference.
- **Prior planning:** pre-update destination choices must not be attributed to later autonomous hazard avoidance.
- **Flexible definitions:** “summit”, “slope”, “near” and “grazing” need objective categories and distances before counting.

### 9.4 Proposed test protocol

The [review template](datos/plantilla_revision_lomas.en.csv) provides one row per flight. Define `crest`, `ridge`, `slope`, `depression`, `flat` and `indeterminate` in advance; use one observation per landing with traceable sol, PDS product, time and source; distinguish planned destination, observed final position and confirmed autonomous candidate; use two observers unaware of the hypothesis and measure agreement; compare ridge landings against the proportion of candidate terrain occupied by ridges; publish negative and indeterminate cases too.

If \(k\) of \(n\) independent landings meet the definition:

\[
\widehat p=\frac{k}{n}
\]

The reference \(p_0\) is not automatically 0.5: it should represent the available terrain already in that category. Without availability, preference cannot be inferred.

### 9.5 Current status

| Claim | Status |
|---|---|
| Author published an apparent recurrence after reviewing 31 images | Documented |
| Several images show positions near ridges, edges or dunes | Qualitative visual observation |
| Exactly 31 or 32 autonomous ridge landings exist | Unverified |
| Ingenuity chose ridges because vision judged them safer | Hypothesis |
| This pattern caused flight 72 blade failure | Not demonstrated |

For aerospace outreach, describe an **initial sample of 31 images**, show cases and counterexamples, and reserve “preference” for a denominator and statistical comparison.

## 10. Flights 62, 68 and 69: maximum speed and possible cumulative loading

### 10.1 Correcting the record

Official maximum ground speed, **10 m/s**, occurred on flights **62, 68 and 69**. Flight 65 is outside this group: about 7 m distance and 1 m/s maximum speed.

| Flight | Date | Distance | Duration | Maximum speed | Relevant purpose |
|---:|---|---:|---:|---:|---|
| 62 | 12 Oct 2023 | 268 m | 121.1 s | 10 m/s | First 10 m/s demonstration, horizontal-flight altitude 18 m |
| 68 | 15 Dec 2023 | 702 m | 131.1 s | 10 m/s | Dedicated system-identification (`Sys-ID`) test |
| 69 | 20 Dec 2023 | 705 m | 135.4 s | 10 m/s | Second Sys-ID test, long out-and-back route |

NASA/JPL describes injecting a sinusoidal frequency sweep into the control input during flights 68 and 69 to induce microscopic pitching during horizontal flight and identify actual vehicle dynamics on Mars. With expected wind, the out-and-back route was intended to provide a headwind leg exceeding **10 m/s airspeed**, within and beyond conditions tested on Earth.

These were deliberate dynamic tests late in operational life, not merely long, fast flights, making their loading history a legitimate technical question.

### 10.2 What physically changes with speed

Ground speed is neither rotor rpm nor a direct stress measurement. Advance ratio is:

\[
\mu=\frac{V_{air}}{\Omega R}
\]

\(V_{air}\) is airspeed, \(\Omega\) rotor angular velocity and \(R\) radius. Increasing \(\mu\) increases relative-speed differences between advancing and retreating blades. Cyclic pitch compensates, and some alternating bending, torsional and aeroelastic loads may increase.

Translation-related dynamic pressure is:

\[
q=\frac12\rho V_{air}^{2}
\]

At constant density, increasing 5 to 10 m/s quadruples this term. It matters for fuselage and translation-related aerodynamic contributions, but **does not mean total blade stress quadrupled**: local blade flow also depends on high rotational speed, azimuth and pitch.

Sys-ID adds small deliberate oscillatory excitations. It does not automatically exceed structural limits. Fast flight does not necessarily use more power than hover: rotorcraft power–speed relationships are non-monotonic and depend on profile, density, wind, attitude and control.

### 10.3 Time, cycles and fatigue: calculable quantities

\[
T_{68+69}=131.1+135.4=266.5\ \text{s}=4.44\ \text{min}
\]

Against 7,731.3 s total logged flight time:

\[
100\frac{266.5}{7731.3}=3.45\%
\]

Using a constant 2,537 rpm only as an approximation:

\[
N_{revolutions}\simeq\frac{rpm\,T}{60}
\]

This gives about 5,121 revolutions in flight 62, 5,543 in flight 68, 5,725 in flight 69 and 11,269 across 68–69. These are **not rotor telemetry or damage-cycle counts** and omit actual rpm variation and load amplitudes.

Fatigue investigation requires at least a load spectrum and material stress–life relation. Miner's cumulative rule provides a conceptual framework:

\[
D=\sum_j\frac{n_j}{N_j}
\]

\(n_j\) is the number of experienced cycles at a stress level, and \(N_j\) the cycles to failure there. Total time alone cannot determine \(D\); a few high-amplitude cycles can outweigh many gentle ones.

### 10.4 Comparison with flight 72

JPL's public assessment of 11 December 2024 attributes the most likely sequence to low texture: loss of features, poor velocity estimation, high horizontal speed at contact, hard impact on a sand ripple's slope, rapid attitude change and blade loads exceeding design limits. JPL says all four blades broke at their weakest section.

| Proposition | Assessment |
|---|---|
| Flights 62, 68 and 69 deliberately expanded the envelope to 10 m/s | Confirmed by NASA |
| Flights 68–69 added dynamic excitations and a profile intended to exceed 10 m/s airspeed on a leg | Documented by NASA/JPL |
| These profiles could produce different cyclic loads from ordinary flight | Physically plausible |
| They caused microdamage or reduced blade strength margin | Not demonstrated by public data |
| They caused flight 72 blade failure | Unsupported; published primary attribution is landing overload |

Flights 68 and 69 were declared successful; flights 70 and 71 followed. No structural anomaly arising from Sys-ID has been published in the cited record. Near-simultaneous failure of all four blades near a weak section is consistent with a common landing overload. Earlier degradation might reduce margin, but confirmation or exclusion requires vibration, pitch commands, rpm, current, temperatures, root loads and material inspection.

> **Hypothesis V:** the high-speed/Sys-ID campaign in flights 62, 68 and 69 may constitute a relevant loading history to compare with structural telemetry. Public data establish envelope expansion, not cumulative damage or causal contribution to flight 72 failure.

The [high-speed flight CSV](datos/vuelos_alta_velocidad_hipotesis.en.csv) preserves the quantities and evidence levels.

## 11. Audio: data, normalisation and spectra

### 11.1 Why the four WAV files have identical sizes

Each flight 4, 5, 6 and 8 PDS WAV has duration 167 s, sampling rate 25,000 samples/s, one channel and stored resolution 32 bits (4 bytes/sample):

\[
167\times25\,000\times1\times4=16\,700\,000\ \text{bytes}
\]

Adding 58 bytes of container header/metadata gives 16,700,058 bytes. Different SHA-256 hashes establish different contents.

### 11.2 Signal preparation

`analisis/comparar_audio.py` converts to floating point where needed, combines channels if necessary and removes the mean:

\[
x_0[n]=x[n]-\overline{x}
\]

Local MP3s are filtered at 60–220 Hz and normalised for listening. Measurements must use the PDS WAVs.

### 11.3 Power spectral density

Welch estimation uses a Hann window, segments up to 65,536 samples, 50% overlap, a 131,072-point FFT and primary display from 60 to 250 Hz. Schematically:

\[
\widehat P_{xx}(f)=\frac1M\sum_{m=1}^{M}\frac{|\operatorname{FFT}(w[n]x_m[n])|^2}{F_s\sum_n w^2[n]}
\]

To make the relative normalisation explicit, let:

\[
L(f)=10\log_{10}(\widehat P_{xx}(f)+\varepsilon),\qquad P_{dB}(f)=L(f)-\max_{60\leq f\leq250}L(f)
\]

Each recording's maximum is set to 0 dB. This compares spectral positions, not absolute acoustic amplitudes.

## 12. Blade-passing frequency and rotor speed

For \(B=2\) blades per rotor and speed \(n\) rpm:

\[
f_{BPF}=B\frac n{60},\qquad n=\frac{60f_{BPF}}B=30f_{BPF}
\]

Examples:

\[
75.8813\ \text{Hz}\times30=2276.44\ \text{rpm}
\]

\[
84.4\ \text{Hz}\times30=2532\ \text{rpm}
\]

The second main component is \(f_2=2f_{BPF}\approx168.8\) Hz. Mathematically this is the second harmonic (`2×BPF`). The paper uses “first harmonic” in the sense of first overtone; this repository states `2×BPF` to avoid ambiguity. The line near 195 Hz belongs to rover equipment.

### Fitting JPL's harmonic comb

For peaks \(f_k\) at harmonics \(k=1,\ldots,K\), a fit constrained through the origin gives:

\[
\widehat f_0=\frac{\sum_{k=1}^{K}kf_k}{\sum_{k=1}^{K}k^2}
\]

\[
RMSE=\sqrt{\frac1K\sum_{k=1}^{K}(f_k-k\widehat f_0)^2}
\]

For the 14 measured peaks: \(\widehat f_0=75.8813\) Hz and \(RMSE=0.018\) Hz. Equivalent speed is 2,276.44 rpm, 0.56 rpm below the displayed 2,277 rpm.

### Two separate checks

The above result uses 14 measured peaks in the JPL video capture. Appendix 3 of the paper independently provides Figure A2 (chamber set-up) and Figure A3 (spectrum, spectrogram and time signal, near-82 Hz spacing with at least 15 visible teeth).

The defensible correspondence is an equivalent harmonic structure generated by the same two-coaxial-rotor architecture. Identity of recording, exact frequency, segment, amplitude or hardware unit is not asserted. Keep `75.8813 Hz × 30 = 2,276.44 rpm` for the analysed video separate from “comb near 82 Hz” for published Figure A3.

## 13. Envelopes and minima

### 13.1 Flight 5

The WAV is resampled to 1,000 samples/s, fourth-order Butterworth filtered at 81.5–87 Hz forwards and backwards, and converted to an analytic envelope:

\[
z(t)=x_f(t)+j\mathcal H\{x_f(t)\},\quad A(t)=|z(t)|,\quad A_{dB}(t)=20\log_{10}(A(t)+\varepsilon)
\]

Gaussian smoothing uses \(\sigma=0.5\) s; the 95th percentile over 20–125 s is subtracted. Reproduced minima occur at `36.3; 46.8; 57.5; 71.7; 88.2; 103.7 s`; intervals are `10.5; 10.7; 14.2; 16.5; 15.5 s`. Lorenz et al. report 36, 47, 57, 72, 88 and 104 s: differences are less than one second.

The current program preserves these as previously measured points; it does not yet contain a fully documented automatic detector with prominence, minimum separation and acceptance criteria.

### 13.2 JPL test comb

The test is resampled to 4,000 samples/s and analysed by STFT: Hann window of 8,192 samples (2.048 s), hop 512 samples (0.128 s), FFT 32,768 points (about 0.122 Hz spacing), fundamental tracking between 70 and 82 Hz, and summed power within ±0.9 Hz of harmonics 1–12.

\[
E_{comb}(t)=\sum_{h=1}^{12}\sum_{|f-hf_0(t)|\leq0.9}|X(f,t)|^2
\]

\[
E_{dB}(t)=10\log_{10}(E_{comb}(t)+\varepsilon)
\]

The 95th percentile over 12–82 s is subtracted. Minima mainly track manoeuvres, orientation, distance, reverberation and automatic gain control, rather than flight 5's organised cadence.

## 14. ΔRPM theory and the acoustic lighthouse

### 14.1 Origin

Lorenz et al. (2023) proposed that a tiny difference between coaxial rotor speeds slowly changes relative blade orientation. The directional emission pattern rotates like a lighthouse, carrying maxima and minima past a fixed observer.

This project does not claim discovery of that mechanism. Its contributions are reproducing flight 5 minima from PDS, comparing them with published Navcam shadows and a JPL ground test, documenting period-to-speed-difference conversion and explaining why minima are not rotor stops.

### 14.2 Algebraic superposition

For two close tones of equal amplitude:

\[
p(t)=A\sin(2\pi f_1t+\phi_1)+A\sin(2\pi f_2t+\phi_2)
\]

A fast oscillation is multiplied by a slow envelope; mean intensity is approximately modulated by:

\[
I(t)\propto\cos^2(\pi\Delta f\,t+\phi)
\]

where \(\Delta f=|f_1-f_2|\). For two-bladed rotors, \(\Delta f_{BPF}=2\Delta n/60\). If the measured interval is a full beat cycle:

\[
\Delta n_{beat}=\frac{30}{T}\quad\text{rpm}
\]

### 14.3 Four-lobe geometric model

The paper's lighthouse model has four principal minimum directions. If its pattern rotates at relative difference \(\Delta n\), four minima pass per relative revolution:

\[
T_{null}\approx\frac{60}{4\Delta n},\qquad\boxed{\Delta n_{lighthouse}\approx\frac{15}{T_{null}}\quad\text{rpm}}
\]

| \(T_{null}\) (s) | \(\Delta n=15/T\) (rpm) |
|---:|---:|
| 10.5 | 1.43 |
| 10.7 | 1.40 |
| 14.2 | 1.06 |
| 16.5 | 0.91 |
| 15.5 | 0.97 |

The descriptive range is approximately 0.9–1.5 rpm, mean 1.15 rpm and median 1.06 rpm, about 0.036–0.056% of nominal 2,537 rpm.

### 14.4 Why a doubled estimate also appears

Full-BPF beating gives \(30/T\), whereas successive lighthouse lobes give \(15/T\). These describe different conventions for the observed interval and must not be mixed. The full-beat interpretation gives about 1.8–2.9 rpm; the four-lobe interpretation supported by shadows gives about 0.9–1.5 rpm.

The repository adopts the latter because minima are compared with successive four-lobe orientations. Changing helicopter–rover angles, possible speed variation and timing uncertainty mean ΔRPM remains an **order-of-magnitude quantitative hypothesis**, never exact telemetry.

### 14.5 What this establishes

| Claim | Status |
|---|---|
| Organised 10–20 s modulation exists in flight 5 | Observed and reproduced |
| Shadow and audio intervals have similar scales | Observed in paper; consistent with reproduction |
| Small asynchrony can generate an acoustic lighthouse | Published, plausible physical model |
| ΔRPM was of order 1 rpm under the four-lobe model | Inference |
| This difference was a fault | Unsupported; below 0.1% and compensable by control |
| Minima mean the rotor stopped | False |
| Modulation caused flight 72's accident | No evidence |

## 15. Current reproducibility

| Component | Status | Available material |
|---|---|---|
| Official flight data | High | CSV and linked sources |
| Map index | High | 72 times, first-stable-label criterion, ±0.1 s precision |
| Feature percentile | Complete | Formula and CSV |
| Spearman correlations | Complete | Formula, 72 records and results |
| Acoustic comparison | High | Linked PDS WAVs, Python code, parameters and derived CSVs |
| Flight 5 envelope | High for curve; partial for automatic minima selection | Code and measured times |
| Visual segmentation | Partial | Boundaries/results; original detector and thresholds missing |
| Visual score | Partial | Published results; exact weights missing |
| Pixel-level comparison with JPL avoidance | Not possible with current public material | Original/intermediate algorithm products missing |
| Rock-side landing reconstruction | Hypothetical | Calibrated geometry/contact telemetry missing |

Publishing the visual generator would do most to turn the carefully documented chronology into a fully reproducible third-party package.

## 16. Most useful technical conclusions

1. The final sequence is broader than one isolated case: feature medians fall from 46.5 in flights 1–67 to 11 in flights 68–72.
2. Texture and continuity differ: flight 53 shows that visible features cannot compensate for image-pipeline or timing failures.
3. Flight 9 supports the principle, not the scale: JPL reconstructs 3D geometry; our index is a simplified prerequisite indicator.
4. Landing near a hazard can be possible: flight 33 distinguishes terrain tracking from stable four-foot placement.
5. Audio independently checks the physics: the test comb closely recovers 2,277 rpm; Mars WAVs retain the 84/168 Hz family.
6. ΔRPM does not indicate failure: flight 5 modulation is consistent with a tiny, order-1-rpm difference under the four-lobe model.
7. Fast flights open a question without resolving the accident: 62/68/69 reached 10 m/s and 68/69 added Sys-ID, but public data do not prove fatigue before flight 72's overload.
8. The project's strength is convergence: records, images, maps, terrain, audio, shadows and papers share a chronology without being misrepresented as telemetry.

## 17. Limitations to accompany publication

The montage is incomplete and discontinuous; block assignments are provisional. Compression, exposure, vignetting, public selection and shadow masks affect metrics. The score is not an Ingenuity flight variable. An overhead image alone provides no calibrated scale, slope or leg-contact order. The feature detector cannot diagnose servos, IMU, vibration, rotor or camera–IMU synchronisation. Acoustic loss can reflect distance, wind or noise, not rotor stoppage. MP3s are previews; measurements require calibrated WAVs. Similarity to NASA/JPL explanations should be called consistency or compatibility unless directly quantified. Ground speed does not directly measure rpm, power, blade stress or fatigue damage.

## 18. Essential sources

- [NASA Science · Ingenuity](https://science.nasa.gov/mission/mars-2020-perseverance/ingenuity-mars-helicopter/)
- [NASA/JPL · flight 72 investigation, 11 December 2024](https://www.jpl.nasa.gov/news/nasa-performs-first-aircraft-accident-investigation-on-another-world/)
- [NASA · The Right Stuff](https://science.nasa.gov/blog/the-right-stuff/)
- [NASA/JPL/Ames · flights 68–69 and Sys-ID](https://science.nasa.gov/blog/unlocking-the-martian-skies-using-ingenuity-as-a-martian-testbed-for-future-rotorcraft/)
- [NASA · maximum-speed flights](https://science.nasa.gov/resource/mars-report-the-most-extreme-flights-of-nasas-ingenuity-mars-helicopter/)
- [NASA/JPL · PIA25662](https://www.jpl.nasa.gov/images/pia25662-ingenuitys-hazard-avoidance-capability/)
- [Schoppmann et al. · Multi-Resolution Elevation Mapping and Safe Landing Site Detection](https://arxiv.org/abs/2111.06271)
- [Proença et al. · Optimizing Terrain Mapping and Landing Site Detection](https://arxiv.org/abs/2205.03522)
- [Lorenz et al. · The sounds of a helicopter on Mars](https://doi.org/10.1016/j.pss.2023.105684)
- [NASA PDS · calibrated SuperCam audio](https://pds-geosciences.wustl.edu/m2020/urn-nasa-pds-mars2020_supercam/data_calibrated_audio/)
- [Sources and method](SOURCES_AND_METHOD.en.md)
- [Hazard and audio analysis](HAZARD_AND_AUDIO_ANALYSIS.en.md)
- [Acoustic analysis code](analisis/comparar_audio.py)
- [Author's LinkedIn profile and blade-failure series](https://www.linkedin.com/in/pedroramon-drones-atsep)

## 19. Recommended citation

> Montserrat Cabrera, Pedro Ramón (2026). *Ingenuity: log ampliado de 72 vuelos, imágenes y audio de Marte. Leyenda, fórmulas y criterios de interpretación* [English edition: Legend, formulas and interpretation criteria]. Fuerteventura, Canary Islands, Spain. https://github.com/pedroramon-estudios/Ingenuity-72-vuelos

Reading, linking and brief attributed quotation are permitted under the repository terms. Public availability does not make original contributions open source. See [LICENSE](LICENSE.en.md) and [NOTICE](NOTICE.en.md).
