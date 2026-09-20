# Revisión de la edición v1.4.1 — 20 de septiembre de 2026

Se ha corregido la figura del vuelo 9 en la web y en el análisis inglés: título y nota explicativa aparecen ahora en inglés. La edición española conserva su imagen original. Los fotogramas, tiempos y marcas NASA/JPL permanecen intactos. Se repitieron las pruebas funcionales de los controles y se revisó visualmente la figura corregida. El nuevo intento de abrir Chromium no pudo completarse por un fallo de arranque del navegador en el entorno de revisión; las comprobaciones de navegador descritas más abajo corresponden a la edición anterior.

# Revisión de publicación — 19 de septiembre de 2026

## Resultado de la comparación con GitHub Pages

Dirección revisada: https://pedroramon-estudios.github.io/Ingenuity-72-vuelos/

Los **33 archivos públicos** del ZIP español v1.3 entregado coinciden byte por byte con los descargados de GitHub Pages. Se compararon el HTML, README, documentación, LICENSE, NOTICE, CITATION, los siete CSV, el programa de análisis, imágenes, cuatro MP3 y vídeo MP4.

El ZIP contiene además `.gitignore` y `.nojekyll`, que no se incluyeron en esa comparación HTTP. La comprobación acredita el contenido servido por la web; no es una inspección del historial de commits, de ramas privadas ni de la configuración de la cuenta.

SHA-256 del `index.html` español publicado y del ZIP de partida:

`da5638c7f497c95a998a7cf23faf27b39e0f11abf8e34e76ddb83afe3ef042e3`

## Edición bilingüe v1.4.1 preparada

- Selector Español | English.
- Página inglesa con los 72 vuelos, notas, controles, mensajes, accesibilidad y metadatos.
- Siete documentos en inglés, disponibles en Markdown y HTML; guía con 75 expresiones matemáticas renderizadas localmente.
- Siete CSV ingleses con datos numéricos idénticos a los originales.
- Portada inglesa de 1200 × 630 para enlaces compartidos.
- Figuras analíticas originales conservadas; pies y claves de ejes, colores y fases disponibles en inglés.
- Autoría, copyright, Fuerteventura y créditos de terceros conservados.
- Corrección del aviso de bloqueo de reproducción: usa la selección del mapa y no la del explorador.
- Aclaración documental de que la extracción visual completa sigue siendo parcialmente reproducible, pues no se conserva el detector original ni sus parámetros.

## Pruebas de funcionamiento

Se ejecutó el JavaScript de las dos páginas y se comprobaron:

| Prueba | Español | Inglés |
|---|---|---|
| 72 botones del explorador | Correcto | Correcto |
| 72 botones del mapa y sus marcas | Correcto | Correcto |
| Índice en las 72 posiciones de reproducción simuladas | Correcto | Correcto |
| Selección mediante desplegable, tabla y gráfica | Correcto | Correcto |
| Seis filtros | Correcto | Correcto |
| Independencia entre explorador y mapa | Correcto | Correcto |
| Aviso cuando se rechaza la reproducción | Correcto | Correcto |
| Errores JavaScript detectados | Ninguno | Ninguno |

Los filtros devuelven 72 vuelos totales, 6 verticales, 14 con incidencia/prueba, 4 con audio, 15 con puntuación baja y 5 en la secuencia final.

## Revisión en Chromium

Se abrieron ambas páginas bajo una subruta de un servidor local y la inglesa también directamente como archivo:

- Vídeo MP4 cargado: 69,1 s; reproducción y búsqueda comprobadas.
- Cuatro audios cargados: 167 s cada uno, sin errores de carga.
- La ficha del vuelo 33 permaneció seleccionada al reproducir otro vuelo en el mapa y saltar al vuelo 72.
- Imágenes sin fallos de carga.
- Revisión visual a 1440 px y 390 px; sin desbordamiento horizontal de la página a 390 px.
- Guía inglesa revisada con las fórmulas renderizadas.
- Portada inglesa renderizada y revisada.

Las pruebas de navegador se realizaron sobre el paquete local. Los reproductores externos y las descargas científicas remotas no se reprodujeron exhaustivamente en esta revisión. Se conservan sus direcciones y créditos. La comprobación funcional no constituye una nueva validación científica de los análisis.

## Conservación de datos

Todos los archivos multimedia originales mantienen exactamente sus bytes. Los valores numéricos y las miniaturas de los 72 vuelos coinciden en ambos idiomas con el original. Los siete CSV ingleses conservan todas las celdas numéricas; cambian las cabeceras y los textos descriptivos.

## Estado de publicación

La **versión española v1.3 está publicada y comprobada**. La **edición bilingüe v1.4.1 está preparada para subir**. Esta entrega no ha realizado un commit, un push, una release ni un despliegue en la cuenta de GitHub.

Las instrucciones están en `ACTUALIZAR_GITHUB.md`. Tras subir los archivos, hay que comprobar que el despliegue termina correctamente antes de anunciar la dirección inglesa.
