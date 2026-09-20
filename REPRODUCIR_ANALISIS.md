# Reproducción del análisis y alcance de los resultados

[English](REPRODUCING_ANALYSIS.en.md) · [Explorador](index.html)

## Gráficas acústicas en español e inglés

Las figuras de espectros y mínimos se regeneraron para la edición 1.4.2 a partir de los cuatro WAV calibrados PDS `p02` y de la captura original del ensayo JPL aportada al estudio. Las versiones inglesas traducen títulos, ejes, leyendas y fases; utilizan los mismos cálculos y registros.

1. Instalar Python y las versiones de las bibliotecas registradas:

   ```sh
   python -m pip install -r analisis/requirements.txt
   ```

2. Descargar los cuatro WAV desde las direcciones `pds_wav` del archivo `datos/audio_ingenuity_pds.csv`. Guardarlos en una carpeta de trabajo como `flight4.wav`, `flight5.wav`, `flight6.wav` y `flight8.wav`.

3. Para repetir exactamente la comparación terrestre, se necesita la captura original de 94,848 segundos, con audio AAC mono de 48.000 muestras/s. No se redistribuye en este paquete. La fuente pública es el vídeo JPLraw enlazado en el análisis. Una descarga distinta de YouTube puede tener otra codificación o referencia temporal y no garantiza el mismo resultado. Extraer el audio de la captura original, sin recortar ni cambiar su frecuencia de muestreo:

   ```sh
   ffmpeg -i CAPTURA.mp4 -vn -c:a pcm_f32le trabajo/jpl-test-audio.wav
   ```

4. Ejecutar desde la raíz del proyecto:

   ```sh
   python analisis/comparar_audio.py --pds-dir trabajo --jpl-wav trabajo/jpl-test-audio.wav --output figuras --language es
   python analisis/comparar_audio.py --pds-dir trabajo --jpl-wav trabajo/jpl-test-audio.wav --output figuras --language en
   ```

Las huellas SHA-256 de los WAV utilizados y las versiones de las bibliotecas están en `analisis/inputs.json`. Los MP3 de escucha no sustituyen a los WAV para este cálculo.

## Qué hace el programa

Calcula espectros normalizados mediante Welch, la envolvente filtrada del vuelo 5 y la energía conjunta de los armónicos del ensayo terrestre. Las ventanas, bandas y normalizaciones figuran en el código. El idioma cambia los rótulos y los nombres de salida, no los cálculos.

Los marcadores de mínimos y las fases del ensayo son anotaciones previamente medidas: se introducen explícitamente en `JPL_DIPS`, `F5_NULLS` y `JPL_PHASES`. El programa no detecta automáticamente esos tiempos ni vuelve a calcular el ajuste de los catorce picos de la tabla. El análisis acústico documenta esos resultados por separado.

## Métrica visual

Se conservan los resultados tabulados, los percentiles y las comprobaciones estadísticas. El programa original de extracción visual, sus umbrales y los pesos exactos de la puntuación no están incluidos. Su reproducción integral sigue siendo parcial. No se ha sustituido el procedimiento ausente por una fórmula nueva.

Los hechos oficiales, las observaciones y las hipótesis mantienen su distinción. Esta revisión editorial no convierte las hipótesis del estudio en conclusiones oficiales sobre el accidente.
