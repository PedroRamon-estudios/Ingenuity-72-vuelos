# Revisión de la edición 1.4.2 — 20 de septiembre de 2026

## Estado de publicación

La edición bilingüe 1.4.1 está publicada. Se comprobaron sus 82 archivos públicos y todos coincidían con el paquete anterior. Esta entrega 1.4.2 contiene las correcciones posteriores, comprobadas localmente. Debe subirse a GitHub para actualizar la publicación; esta preparación no ha realizado un commit, un push ni un despliegue en la cuenta del autor.

## Correcciones

- Regeneradas las dos gráficas acústicas con todos sus rótulos en inglés, a partir de los WAV PDS y la captura original JPL del estudio.
- Conservada la figura inglesa corregida del vuelo 9, incluidos su título y la nota sobre números rojos y marcadores cian.
- Añadidas páginas HTML españolas para la documentación, con las fórmulas renderizadas y fuentes locales.
- Actualizados los textos que presentaban la edición inglesa como todavía inexistente.
- Añadidas instrucciones de reproducción, versiones de dependencias y huellas de las entradas acústicas.
- Añadido el número de edición al pie de ambas portadas para identificar la actualización.
- Conservados los datos de los 72 vuelos, las marcas temporales del mapa, los audios y el vídeo, las imágenes españolas, los créditos y las condiciones de uso.

## Pruebas funcionales

Se ejecutaron en español e inglés los 72 botones del explorador, los 72 botones del mapa, las 72 posiciones temporales simuladas, el desplegable, la tabla, la gráfica y los seis filtros. También se comprobó el aviso de reproducción bloqueada. No se detectaron errores JavaScript en estas pruebas. Los filtros devuelven 72, 6, 14, 4, 15 y 5 vuelos, respectivamente.

## Pruebas en navegador

Se abrió el paquete local con Chromium 153, bajo una subruta de servidor, y la portada inglesa también como archivo local. Ambas portadas cargan el vídeo de 69,1 segundos y los cuatro audios de 167 segundos. Se comprobó la búsqueda y reproducción del mapa, el mantenimiento de la ficha del vuelo 33 al cambiar el mapa y el salto a la marca del vuelo 72. Las portadas no presentan desbordamiento horizontal a 390 píxeles. La guía inglesa renderiza 75 expresiones matemáticas; la española, 81, por su distinta distribución editorial.

Estas pruebas se refieren al paquete preparado. No certifican todos los navegadores ni la disponibilidad futura de los reproductores externos.

## Datos y figuras

La revisión previa contrastó los 72 vuelos con el registro oficial de NASA en sol, distancia horizontal, altura máxima, velocidad máxima y duración, sin discrepancias. Esos valores se conservan en esta edición. También se verificaron los percentiles, las medianas y las correlaciones de Spearman publicadas.

Las dos figuras acústicas se recalcularon desde las entradas originales. La regeneración española coincide con las figuras publicadas salvo diferencias mínimas de renderizado. La opción de idioma cambia los textos y los nombres de salida, sin cambiar el cálculo. Las entradas no se sustituyeron por los MP3 de escucha.

## Alcance y límites

La puntuación visual sigue siendo parcialmente reproducible porque no se conserva en el paquete su programa original completo. Las fases y los mínimos señalados en las figuras acústicas son anotaciones previas introducidas en el código; el programa no los detecta automáticamente ni recalcula el ajuste de catorce picos. Véanse las [instrucciones de reproducción](REPRODUCIR_ANALISIS.md).

En la comprobación pública anterior, 30 de 37 enlaces externos respondieron. Cuatro páginas JPL, el DOI del artículo, ScienceDirect y LinkedIn devolvieron restricciones o errores de acceso automático. No se clasificaron como enlaces rotos. Se conservan las fuentes originales y sus créditos.

La revisión funcional y editorial no constituye una nueva validación científica de todas las interpretaciones ni transforma las hipótesis en conclusiones oficiales.
