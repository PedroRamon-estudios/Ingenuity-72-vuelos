# Publicar la edición bilingüe en el repositorio existente

La web española ya está publicada y conserva esta dirección:

https://pedroramon-estudios.github.io/Ingenuity-72-vuelos/

Esta entrega añade la versión inglesa sin crear otro repositorio ni cambiar la visibilidad.

## Actualización desde GitHub

1. Descarga y descomprime el paquete completo. Dentro deben aparecer `index.html`, `index-en.html`, la documentación y las carpetas `assets`, `datos` y `analisis`.
2. Abre https://github.com/PedroRamon-estudios/Ingenuity-72-vuelos y entra en la rama que ya publica tu web.
3. Pulsa **Add file → Upload files**.
4. Arrastra el contenido descomprimido a la raíz del repositorio. No arrastres la carpeta exterior ni subas únicamente el ZIP: `index-en.html` debe quedar junto a `index.html`.
5. Comprueba que se añaden también las páginas `*.en.html`, los documentos `*.en.md`, los siete CSV `*.en.csv`, `assets/social-card-en.png`, `assets/social-card-en.svg` y `assets/docs/` con sus fuentes y licencia.
6. Escribe como mensaje: `Publicar edición bilingüe de Ingenuity v1.4.0` y pulsa **Commit changes**.
7. Espera a que termine correctamente el despliegue de GitHub Pages en **Actions**. La configuración de Pages que ya funciona no necesita cambiarse.
8. Abre la web, comprueba el selector **Español | English** y visita la nueva dirección inglesa:

   https://pedroramon-estudios.github.io/Ingenuity-72-vuelos/index-en.html

Si la carga web no admite todos los archivos en una sola operación, haz varios grupos conservando las rutas. No borres las carpetas existentes. Otra opción es copiar el contenido del paquete sobre la carpeta del repositorio en GitHub Desktop, revisar los cambios, confirmar y pulsar **Push origin**.

## Comprobación tras la publicación

- Cambia de idioma en ambas direcciones.
- Selecciona vuelos en la gráfica y la tabla: la ficha cambia y el mapa sigue independiente.
- Pulsa vuelos del índice del mapa y mueve su barra de tiempo.
- Escucha los cuatro audios y abre los documentos ingleses y los CSV.
- Comprueba la guía de fórmulas y la portada al compartir.
- Para renovar la vista previa de LinkedIn, usa https://www.linkedin.com/post-inspector/ con la dirección que vayas a compartir.

El enlace español ya puede difundirse. La dirección inglesa debe anunciarse después de completar esta actualización.

## Versión estable

La edición se identifica como **v1.4.0**, para distinguirla de la v1.3 española. Una vez comprobado el despliegue, puede crearse una release con esa etiqueta y adjuntar este ZIP. Preparar el paquete no crea por sí solo una release en GitHub.

## Qué conserva

Los 72 vuelos y sus datos numéricos, las marcas del mapa, los cuatro audios, el vídeo, las imágenes del estudio, los créditos y las condiciones de uso. La corrección de funcionamiento se limita al aviso que aparece si el navegador impide reproducir el mapa: ahora consulta el vuelo del propio mapa, no el del explorador independiente.

La revisión de la publicación anterior está detallada en `REVISION_PUBLICACION.md`.
