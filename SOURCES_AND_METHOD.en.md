# Sources, method and limitations

[Español](FUENTES_Y_METODO.md) · [English explorer](index-en.html)

## What this page brings together

The timeline combines seven layers of information:

1. **Official flight data:** number, sol, date, distance, maximum altitude, speed and duration.
2. **Spatial context:** NASA/JPL-Caltech's official animation locating all 72 flights.
3. **Visual continuity:** Jacint Roger's (Landru79) chronological montage of public Navcam images.
4. **Exploratory visual analysis:** segmentation using shadow passages, and uniformly calculated local features, coverage and relative visual scores. The complete score formula is not preserved in this package; it is declared partially reproducible.
5. **Acoustic record:** calibrated SuperCam WAV files associated with flights 4, 5, 6 and 8, with derived previews and spectrograms.
6. **Independent comparisons:** JPL's hazard-avoidance demonstration and ground test, kept separate from flight telemetry.
7. **Open questions:** landing beside a rock, ΔRPM, the published 31–32 ridges hypothesis and the loading history of flights 62, 68 and 69 at 10 m/s.

## Official map of all 72 flights

- Resource: *See Ingenuity's Flight Map: 72 Helicopter Flights on Mars*.
- Published: 18 April 2024.
- Credit: NASA/JPL-Caltech.
- Stated coverage: locations of all 72 flights over almost three years.
- Integration: lightweight local copy of the official video, linking to NASA Science and JPL.
- Navigation: only the index beside the map seeks to the corresponding flight label. The explorer's buttons, chart, dropdown and table retain a fixed, independent selection.
- Auditable table: [map timestamps](datos/mapa_oficial_72_vuelos_tiempos.en.csv).
- The downloadable UHD file is 639.35 MB and is not copied into the repository.

The animation supplies spatial context. It is not used to measure coordinates, scale or distances, is not raw telemetry and does not replace the Flight Log.

The 72 markers were obtained by reviewing the official UHD master at 10 frames per second and noting the first stable frame showing each `Flight Number` label. Sampling precision is ±0.1 s; effective seeking may vary slightly with MP4 keyframes and the browser. The total duration was not distributed proportionally: the final flights remain on screen longer than most earlier ones.

## Method applied to the montage

- Processed file: 22,546 frames at 25 frames per second, lasting 901.84 seconds.
- Large-shadow passages detected: 75.
- Three passages between flights 13 and 14 were treated as pre-flight checks.
- Provisional assigned blocks: 72.
- Sample per block: 20 frames from the central segment.
- Visual references: a corner/local-feature approximation after cropping the vignette and masking the estimated shadow.
- Coverage: proportion of usable cells in a 4 × 4 grid containing at least two features.
- Score: a relative measure normalised within this montage.

## Acoustic layer

- Authoritative archive: NASA Planetary Data System collection `mars2020_supercam/data_calibrated_audio`.
- Included sessions: flight 4 (sol 69), flight 5 (sol 76), flight 6 (sol 91) and flight 8 (sol 120).
- Current PDS format: calibrated `p02` WAV, mono, 25,000 samples per second, 167 seconds per session.
- Local preview: mono MP3 at 44.1 kHz, filtered from 60 to 220 Hz and normalised. For listening, not measurement.
- Local spectrogram: the same 0–250 Hz range for all four sessions.
- Interpretation: 84 Hz is Ingenuity's blade-passing frequency; 168 Hz is its second harmonic (`2×BPF`). The signal near 195 Hz belongs to the rover's thermal pump, not the helicopter.

Lorenz et al. list `p01` identifiers for some sessions. The currently available PDS archive serves reprocessed `p02` products; the project CSV records current addresses and corresponding XML labels.

### Comparison with JPL's ground test

Audiovisual source: [NASA Ingenuity Mars Helicopter Testing Media Reel](https://www.youtube.com/watch?v=nAQxNd3uBN0&t=148s), official JPLraw channel, duration 3:58. The test begins at 2:28. The site embeds that official player and does not redistribute the screen recording used in the analysis.

The supplied capture contains mono AAC audio at 48 kHz and displays 2,277 rpm. Its audio was extracted to WAV without changing the content, and spectral density was measured during the stable segment. The fourteen actually measured peaks were fitted to integer multiples of a fundamental frequency: `75.8813 Hz`, equivalent to `2,276.44 rpm`, with an RMS residual of `0.018 Hz`.

Appendix 3 of Lorenz et al. provides a different check. Figure A2 shows the hovering set-up in the Mars-pressure chamber; Figure A3 presents the spectrum, spectrogram and time signal. A3 shows a comb near 82 Hz with at least 15 visible teeth. The equivalence concerns the type of harmonic structure governed by blade-passing frequency, not identity of recording, segment, hardware unit or pixels.

Temporal minima were compared by tracking the combined energy of harmonics 1–12 with an STFT. For flight 5, the 81.5–87 Hz band was filtered, its envelope calculated and smoothed over 0.5 s. The six minima reproduce the published times within less than one second.

The comparison uses frequencies and relative times, not absolute acoustic levels. AAC, YouTube, the mobile capture, chamber reverberation and automatic gain control prevent amplitude calibration against PDS WAV files.

### Synchronisation

Table A3 and the paper's appendix warn of offsets of tens of seconds between the rover and SuperCam clocks. The site therefore retains each recording's own time and makes no claim of exact audio–image correspondence. Establishing it requires reading image and audio headers, applying their offsets and documenting the resulting uncertainty.

## Interpretation

### Observed

Information directly visible in public imagery or officially published in the flight record.

### Reproduced

Results recalculated by applying a described procedure to public material. The output table can be audited; full regeneration of visual features, coverage and score remains limited by the missing original extraction program and parameters, as documented below.

### Hypothesis

Interpretations connecting terrain, navigation, landing or possible design improvements. They frame questions but do not replace internal telemetry.

The **31–32 ridges hypothesis** originated in the author's LinkedIn series. The historical archive explicitly mentions 31 images; “about 32” was a later approximation. This does not yet mean 31 or 32 independent landings or establish an autonomous preference. The formal review must use the [review template](datos/plantilla_revision_lomas.en.csv), recording one case per flight, counterexamples and available terrain.

**Hypothesis V** records another question arising from the final sequence: flights 62, 68 and 69 were the only flights to reach 10 m/s, and 68–69 were dynamic `Sys-ID` tests. NASA documents deliberate envelope expansion, control excitations and intended airspeed above 10 m/s on at least one leg. The project lacks root loads, vibration, pitch commands, rpm and temperatures needed to calculate cumulative damage; it therefore treats this as a possible loading history, not an established cause of flight 72.

## Essential limitations

- The montage neither includes every original frame nor constitutes continuous footage.
- The score is not Ingenuity's internal feature count.
- Public selection, compression, vignetting, exposure and provisional block assignment can affect measurements.
- Visible texture cannot diagnose servos, rotors, vibration or camera–IMU synchronisation.
- An apparently rock-free area is not necessarily level or stable for all four feet.
- A representative frame cannot reconstruct the exact contact order of the landing legs.
- Differences can identify cases for deeper review; they do not independently establish progressive failure.
- Filtered audio may hide components and alter relative levels; analysis must return to the PDS WAV.
- Detecting a rotor frequency alone cannot establish servo, control or structural condition.
- Counting images near ridges without measuring available alternatives cannot establish selection preference.
- Maximum ground speed does not directly determine blade stress, power, structural margin or accumulated fatigue.

## Main sources

- [NASA Science · Ingenuity and Flight Log](https://science.nasa.gov/mission/mars-2020-perseverance/ingenuity-mars-helicopter/)
- [NASA Science · 72-flight map](https://science.nasa.gov/resource/see-ingenuitys-flight-map-72-helicopter-flights-on-mars/)
- [NASA/JPL · 72-flight map video](https://www.jpl.nasa.gov/videos/see-ingenuitys-flight-map-72-helicopter-flights-on-mars/)
- [Mars 2020 public image archive](https://mars.nasa.gov/mars2020/multimedia/raw-images/)
- [Jacint Roger · Landru79](https://www.youtube.com/@landru79)
- [NASA/JPL · official flight 72 investigation](https://www.jpl.nasa.gov/news/nasa-performs-first-aircraft-accident-investigation-on-another-world/)
- [NASA · The Right Stuff: envelope expansion and flight 62](https://science.nasa.gov/blog/the-right-stuff/)
- [NASA/JPL/Ames · flights 68–69 Sys-ID campaign](https://science.nasa.gov/blog/unlocking-the-martian-skies-using-ingenuity-as-a-martian-testbed-for-future-rotorcraft/)
- [NASA · maximum-speed flights 62, 68 and 69](https://science.nasa.gov/resource/mars-report-the-most-extreme-flights-of-nasas-ingenuity-mars-helicopter/)
- [NASA · Flight Control and Aerodynamic Performance](https://science.nasa.gov/blog/what-were-learning-about-ingenuitys-flight-control-and-aerodynamic-performance/)
- [NASA/JPL · Hazard Avoidance Capability](https://www.jpl.nasa.gov/images/pia25662-ingenuitys-hazard-avoidance-capability/)
- [JPLraw · testing media reel](https://www.youtube.com/watch?v=nAQxNd3uBN0&t=148s)
- [Schoppmann et al. · Multi-Resolution Elevation Mapping and Safe Landing Site Detection](https://arxiv.org/abs/2111.06271)
- [Proença et al. · Optimizing Terrain Mapping and Landing Site Detection](https://arxiv.org/abs/2205.03522)
- [Lorenz et al. · The sounds of a helicopter on Mars (2023)](https://doi.org/10.1016/j.pss.2023.105684)
- [NASA PDS · calibrated SuperCam audio](https://pds-geosciences.wustl.edu/m2020/urn-nasa-pds-mars2020_supercam/data_calibrated_audio/)
- [NASA Science · processed flight 4 audio](https://science.nasa.gov/resource/listen-to-nasas-ingenuity-mars-helicopter-in-flight/)
- [Pedro Ramón Montserrat Cabrera · LinkedIn posts](https://www.linkedin.com/in/pedroramon-drones-atsep)

Exact WAV and XML addresses are retained in the [audio catalogue](datos/audio_ingenuity_pds.en.csv). The full comparisons are in [Hazard and audio analysis](HAZARD_AND_AUDIO_ANALYSIS.en.md); formulas, flight 9, flight 33, ridges and ΔRPM are in [Legend, formulas and criteria](LEGEND_FORMULAS_AND_CRITERIA.en.md).

## Credits

Mission imagery and data: **NASA/JPL-Caltech** and the relevant scientific teams. Chronological montage: **Jacint Roger (Landru79)**. Analysis, selection and narrative: **Pedro Ramón Montserrat Cabrera**, Fuerteventura, Canary Islands, Spain.

An independent personal project for science communication and public study, with no NASA/JPL affiliation or endorsement. Third-party materials retain their original terms.

## Rights in original contributions

**© 2026 Pedro Ramón Montserrat Cabrera — Fuerteventura, Canary Islands, Spain. All rights reserved.** Public access permits reading, linking and attributed quotation; it does not grant an open-source licence. See [terms](LICENSE.en.md) and [attribution](NOTICE.en.md).
