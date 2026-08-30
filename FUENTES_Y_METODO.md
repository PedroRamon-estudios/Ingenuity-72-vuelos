# Fuentes, método y límites

## Qué reúne esta página

La cronología cruza tres niveles de información:

1. **Datos oficiales de los vuelos:** número, sol, fecha, distancia, altura máxima, velocidad y duración.
2. **Continuidad visual:** montaje cronológico de imágenes públicas Navcam elaborado por Jacint Roger (Landru79).
3. **Análisis reproducido:** segmentación mediante pasos de sombra y cálculo uniforme de referencias locales, cobertura y puntuación visual relativa.

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

## Cómo debe interpretarse

### Observado

Información visible directamente en las imágenes públicas o publicada oficialmente en el registro de vuelos.

### Reproducido

Resultados que pueden volver a calcularse aplicando el mismo procedimiento al montaje: segmentación, referencias, cobertura y puntuación relativa.

### Hipótesis

Interpretaciones que conectan terreno, navegación, aterrizaje o posibles mejoras de diseño. Sirven para formular preguntas, pero no sustituyen la telemetría interna.

## Límites esenciales

- El montaje no contiene todos los fotogramas originales de todos los vuelos ni constituye una grabación continua.
- La puntuación no es el contador interno de rasgos usado por Ingenuity.
- La selección pública, la compresión, el viñeteado, la exposición y la asignación provisional de bloques pueden afectar a las medidas.
- La textura visible no permite diagnosticar servos, rotor, vibraciones ni sincronización cámara–IMU.
- Una zona aparentemente libre de piedras no demuestra que sea horizontal o estable para las cuatro patas.
- Un fotograma representativo no permite reconstruir el orden exacto de contacto de las patas.
- Las diferencias observadas permiten seleccionar casos para una revisión más profunda; no demuestran por sí solas una avería progresiva.

## Fuentes principales

- [NASA Science · Ingenuity Mars Helicopter y Flight Log](https://science.nasa.gov/mission/mars-2020-perseverance/ingenuity-mars-helicopter/)
- [NASA Mars 2020 · archivo de imágenes públicas](https://mars.nasa.gov/mars2020/multimedia/raw-images/)
- [Jacint Roger · Landru79](https://www.youtube.com/@landru79)
- [NASA/JPL · investigación oficial del vuelo 72](https://www.jpl.nasa.gov/news/nasa-performs-first-aircraft-accident-investigation-on-another-world/)
- [NASA · Flight Control and Aerodynamic Performance](https://science.nasa.gov/blog/what-were-learning-about-ingenuitys-flight-control-and-aerodynamic-performance/)
- [NASA/JPL · Hazard Avoidance Capability](https://www.jpl.nasa.gov/images/pia25662-ingenuitys-hazard-avoidance-capability/)
- [Lorenz et al., “The sounds of a helicopter on Mars” (2023)](https://doi.org/10.1016/j.pss.2023.105684)
- [NASA Planetary Data System · Mars 2020](https://pds-geosciences.wustl.edu/missions/mars2020/)

## Créditos

Imágenes y datos de misión: **NASA/JPL-Caltech** y los equipos científicos correspondientes.

Montaje cronológico: **Jacint Roger (Landru79)**.

Análisis, selección y relato: **Pedro Ramón Montserrat Cabrera**.

Este es un proyecto personal e independiente de divulgación y aprendizaje abierto. No está afiliado ni ha sido avalado por NASA/JPL. Los materiales de terceros conservan sus condiciones de uso originales.
