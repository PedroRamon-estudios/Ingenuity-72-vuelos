# Fuentes, método y límites

## Qué reúne esta página

La cronología cruza cinco niveles de información:

1. **Datos oficiales de los vuelos:** número, sol, fecha, distancia, altura máxima, velocidad y duración.
2. **Contexto espacial:** animación oficial NASA/JPL-Caltech de la localización de los 72 vuelos.
3. **Continuidad visual:** montaje cronológico de imágenes públicas Navcam elaborado por Jacint Roger (Landru79).
4. **Análisis visual exploratorio:** segmentación mediante pasos de sombra y resultados uniformes de referencias locales, cobertura y puntuación visual relativa; la fórmula completa de la puntuación no se conserva en este paquete y se declara parcialmente reproducible.
5. **Registro acústico:** WAV calibrados de SuperCam asociados a los vuelos 4, 5, 6 y 8, con previsualizaciones y espectrogramas derivados.
6. **Contrastes independientes:** demostración de evitación de peligros y ensayo terrestre de JPL, separados de la telemetría de vuelo.
7. **Preguntas abiertas:** aterrizaje junto a una roca, ΔRPM, la hipótesis publicada de las 31–32 lomas y el historial de carga de los vuelos 62, 68 y 69 a 10 m/s.

## Mapa oficial de los 72 vuelos

- Recurso: `See Ingenuity's Flight Map: 72 Helicopter Flights on Mars`.
- Publicación: 18 de abril de 2024.
- Crédito: NASA/JPL-Caltech.
- Cobertura declarada: localización de los 72 vuelos realizados durante casi tres años.
- Integración: copia local ligera del vídeo oficial, con enlaces a las fichas de NASA Science y JPL.
- Navegación: sólo el índice situado junto al mapa lleva el reproductor al rótulo correspondiente. Los botones, la gráfica, el desplegable y la tabla del explorador mantienen una selección fija e independiente.
- Tabla auditable: [`datos/mapa_oficial_72_vuelos_tiempos.csv`](datos/mapa_oficial_72_vuelos_tiempos.csv).
- El archivo UHD descargable ocupa 639,35 MB y no se copia en el repositorio.

La animación añade contexto espacial a la cronología, pero no se usa para medir coordenadas, escala o distancias. No se presenta como telemetría bruta ni sustituye el Flight Log.

Las 72 marcas se obtuvieron revisando el máster UHD oficial a 10 fotogramas por segundo y anotando el primer fotograma estable en el que aparece cada rótulo `Flight Number`. La precisión de muestreo es de ±0,1 s; la búsqueda efectiva del reproductor puede variar ligeramente por los fotogramas clave del MP4 y el navegador. No se repartió la duración total de forma proporcional: los vuelos finales permanecen más tiempo en pantalla que gran parte de los anteriores.

## Método aplicado al montaje

- Archivo procesado: 22.546 fotogramas.
- Frecuencia: 25 fotogramas por segundo.
- Duración: 901,84 segundos.
- Pasos de sombra grande detectados: 75.
- Tres pasos situados entre los vuelos 13 y 14 fueron tratados como comprobaciones previas, no como vuelos.
- Bloques provisionales asignados: 72.
- Muestra por bloque: 20 fotogramas del tramo central.
- Referencias visuales: aproximación basada en esquinas o rasgos locales detectables después de recortar el viñeteado y enmascarar la sombra estimada.
- Cobertura: proporción de celdas útiles de una cuadrícula 4 × 4 que contienen al menos dos referencias.
- Puntuación: medida relativa normalizada dentro del propio montaje.

## Capa acústica

- Archivo de autoridad: colección `mars2020_supercam/data_calibrated_audio` del NASA Planetary Data System.
- Sesiones integradas: vuelos 4 (sol 69), 5 (sol 76), 6 (sol 91) y 8 (sol 120).
- Formato PDS actual: WAV calibrado `p02`, mono, 25.000 muestras por segundo y 167 segundos por sesión.
- Previsualización local: MP3 mono a 44,1 kHz, filtrado entre 60 y 220 Hz y normalizado. Sirve para escuchar, no para medir.
- Espectrograma local: misma escala para las cuatro sesiones, de 0 a 250 Hz.
- Referencias de lectura: 84 Hz corresponde a la frecuencia de paso de pala de Ingenuity; 168 Hz es su segundo armónico (`2×BPF`). La señal cercana a 195 Hz pertenece a la bomba térmica del rover y no debe atribuirse al helicóptero.

El artículo de Lorenz et al. reproduce identificadores `p01` para algunas sesiones. El archivo PDS disponible actualmente sirve productos reprocesados `p02`; el CSV del proyecto registra las direcciones actuales y las etiquetas XML correspondientes.

### Contraste con el ensayo terrestre de JPL

Fuente audiovisual: [NASA Ingenuity Mars Helicopter Testing Media Reel](https://www.youtube.com/watch?v=nAQxNd3uBN0&t=148s), canal oficial JPLraw, duración 3:58. El ensayo comienza en 2:28. La web incrusta ese reproductor oficial y no redistribuye la grabación de pantalla empleada en el análisis.

La captura aportada contiene audio AAC mono a 48 kHz y muestra un régimen de 2.277 rpm. Se extrajo la pista a WAV sin cambiar el contenido y se midió la densidad espectral en el tramo estable. Los catorce máximos realmente medidos se ajustaron a múltiplos enteros de una frecuencia fundamental: `75,8813 Hz`, equivalente a `2.276,44 rpm`, con residuo RMS de `0,018 Hz`.

El apéndice 3 de Lorenz et al. constituye una comprobación diferente. La figura A2 muestra el montaje de vuelo estacionario en la cámara de presión marciana; la figura A3 presenta el espectro, el espectrograma y la señal temporal. En A3 se distingue una peineta cercana a 82 Hz con al menos 15 dientes visibles. La equivalencia está en el tipo de estructura armónica gobernada por la frecuencia de paso de pala, no en que sea la misma grabación, el mismo tramo, la misma unidad ni una copia píxel a píxel.

Para comparar mínimos temporales se siguió conjuntamente la energía de los armónicos 1–12 mediante STFT. En el vuelo 5 se filtró la banda 81,5–87 Hz, se calculó su envolvente y se suavizó a una escala de 0,5 s. Los seis mínimos reproducen los tiempos publicados con diferencias inferiores a un segundo.

La comparación usa frecuencias y tiempos relativos, no niveles acústicos absolutos. AAC, YouTube, la captura móvil, la reverberación del recinto y el control automático de ganancia impiden calibrar amplitudes frente a los WAV PDS.

### Sincronización

La tabla A3 y el apéndice del paper advierten que los relojes del rover y SuperCam pueden presentar diferencias de decenas de segundos. Por eso el sitio mantiene el tiempo propio de la grabación y no afirma una correspondencia exacta audio–imagen. Para construirla habría que leer las cabeceras de imagen y audio, aplicar sus desplazamientos y documentar la incertidumbre resultante.

## Cómo debe interpretarse

### Observado

Información visible directamente en las imágenes públicas o publicada oficialmente en el registro de vuelos.

### Reproducido

Resultados que pueden volver a calcularse aplicando el mismo procedimiento al montaje: segmentación, referencias, cobertura y puntuación relativa.

### Hipótesis

Interpretaciones que conectan terreno, navegación, aterrizaje o posibles mejoras de diseño. Sirven para formular preguntas, pero no sustituyen la telemetría interna.

La llamada hipótesis de las **31–32 lomas** procede de una serie de publicaciones del autor en LinkedIn. El archivo histórico menciona de forma exacta una revisión de 31 imágenes; «unas 32» es una aproximación posterior. Ese número no equivale todavía a 31 o 32 aterrizajes independientes ni demuestra una preferencia autónoma. La revisión formal debe completarse con [`datos/plantilla_revision_lomas.csv`](datos/plantilla_revision_lomas.csv), registrando un caso por vuelo, contraejemplos y terreno disponible.

La **hipótesis V** registra otra pregunta surgida al comparar la secuencia final: los vuelos 62, 68 y 69 fueron los únicos que alcanzaron 10 m/s, y 68–69 fueron ensayos dinámicos `Sys-ID`. NASA confirma la expansión deliberada de la envolvente, las excitaciones de control y una velocidad respecto al aire superior a 10 m/s en al menos un tramo previsto. El proyecto no dispone, sin embargo, de cargas de raíz, vibraciones, órdenes de paso, rpm y temperaturas para calcular daño acumulado; por ello se clasifica como posible historial de carga, no como causa demostrada del vuelo 72.

## Límites esenciales

- El montaje no contiene todos los fotogramas originales de todos los vuelos ni constituye una grabación continua.
- La puntuación no es el contador interno de rasgos usado por Ingenuity.
- La selección pública, la compresión, el viñeteado, la exposición y la asignación provisional de bloques pueden afectar a las medidas.
- La textura visible no permite diagnosticar servos, rotor, vibraciones ni sincronización cámara–IMU.
- Una zona aparentemente libre de piedras no demuestra que sea horizontal o estable para las cuatro patas.
- Un fotograma representativo no permite reconstruir el orden exacto de contacto de las patas.
- Las diferencias observadas permiten seleccionar casos para una revisión más profunda; no demuestran por sí solas una avería progresiva.
- El audio filtrado puede ocultar componentes y cambiar niveles relativos; cualquier análisis debe volver al WAV PDS.
- Detectar una frecuencia de rotor no permite deducir por sí solo el estado de servos, control o estructura.
- Contar imágenes próximas a lomas sin medir el terreno alternativo disponible no permite inferir una preferencia de selección.
- Una velocidad máxima sobre el suelo no permite deducir directamente esfuerzo de pala, potencia, margen estructural ni fatiga acumulada.

## Fuentes principales

- [NASA Science · Ingenuity Mars Helicopter y Flight Log](https://science.nasa.gov/mission/mars-2020-perseverance/ingenuity-mars-helicopter/)
- [NASA Science · mapa de los 72 vuelos de Ingenuity](https://science.nasa.gov/resource/see-ingenuitys-flight-map-72-helicopter-flights-on-mars/)
- [NASA/JPL · vídeo del mapa de los 72 vuelos](https://www.jpl.nasa.gov/videos/see-ingenuitys-flight-map-72-helicopter-flights-on-mars/)
- [NASA Mars 2020 · archivo de imágenes públicas](https://mars.nasa.gov/mars2020/multimedia/raw-images/)
- [Jacint Roger · Landru79](https://www.youtube.com/@landru79)
- [NASA/JPL · investigación oficial del vuelo 72](https://www.jpl.nasa.gov/news/nasa-performs-first-aircraft-accident-investigation-on-another-world/)
- [NASA · The Right Stuff: expansión de la envolvente y vuelo 62](https://science.nasa.gov/blog/the-right-stuff/)
- [NASA/JPL/Ames · campaña Sys-ID de los vuelos 68 y 69](https://science.nasa.gov/blog/unlocking-the-martian-skies-using-ingenuity-as-a-martian-testbed-for-future-rotorcraft/)
- [NASA · vuelos de máxima velocidad 62, 68 y 69](https://science.nasa.gov/resource/mars-report-the-most-extreme-flights-of-nasas-ingenuity-mars-helicopter/)
- [NASA · Flight Control and Aerodynamic Performance](https://science.nasa.gov/blog/what-were-learning-about-ingenuitys-flight-control-and-aerodynamic-performance/)
- [NASA/JPL · Hazard Avoidance Capability](https://www.jpl.nasa.gov/images/pia25662-ingenuitys-hazard-avoidance-capability/)
- [JPLraw · NASA Ingenuity Mars Helicopter Testing Media Reel](https://www.youtube.com/watch?v=nAQxNd3uBN0&t=148s)
- [Schoppmann et al. · Multi-Resolution Elevation Mapping and Safe Landing Site Detection](https://arxiv.org/abs/2111.06271)
- [Proença et al. · Optimizing Terrain Mapping and Landing Site Detection](https://arxiv.org/abs/2205.03522)
- [Lorenz et al., “The sounds of a helicopter on Mars” (2023)](https://doi.org/10.1016/j.pss.2023.105684)
- [NASA PDS · archivo calibrado de audio SuperCam](https://pds-geosciences.wustl.edu/m2020/urn-nasa-pds-mars2020_supercam/data_calibrated_audio/)
- [NASA Science · escucha procesada del vuelo 4](https://science.nasa.gov/resource/listen-to-nasas-ingenuity-mars-helicopter-in-flight/)
- [Pedro Ramón Montserrat Cabrera · publicaciones de Ingenuity en LinkedIn](https://www.linkedin.com/in/pedroramon-drones-atsep)

Las direcciones exactas de los cuatro WAV y sus etiquetas se mantienen en [`datos/audio_ingenuity_pds.csv`](datos/audio_ingenuity_pds.csv).

El contraste completo con el vídeo de evitación y el ensayo terrestre se documenta en [`ANALISIS_HAZARD_AUDIO_JPL.md`](ANALISIS_HAZARD_AUDIO_JPL.md).

Las fórmulas, la evaluación del vuelo 9, el aterrizaje del vuelo 33, la hipótesis de las lomas y la teoría ΔRPM se reúnen en [`LEYENDA_FORMULAS_Y_CRITERIOS.md`](LEYENDA_FORMULAS_Y_CRITERIOS.md).

## Créditos

Imágenes y datos de misión: **NASA/JPL-Caltech** y los equipos científicos correspondientes.

Montaje cronológico: **Jacint Roger (Landru79)**.

Análisis, selección y relato: **Pedro Ramón Montserrat Cabrera**, Fuerteventura, Islas Canarias, España.

Este es un proyecto personal e independiente de divulgación y consulta pública. No está afiliado ni ha sido avalado por NASA/JPL. Los materiales de terceros conservan sus condiciones de uso originales.

## Derechos sobre las aportaciones originales

**© 2026 Pedro Ramón Montserrat Cabrera — Fuerteventura, Islas Canarias, España. Todos los derechos reservados.** El acceso público permite consultar, enlazar y citar el trabajo con atribución; no concede una licencia de código abierto. Las condiciones completas y la separación entre aportaciones originales y materiales de terceros figuran en [`LICENSE`](LICENSE) y [`NOTICE.md`](NOTICE.md).
