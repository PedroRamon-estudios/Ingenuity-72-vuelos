# Actualizar GitHub con la edición 1.4.2

La web ya está publicada en español e inglés. Este paquete completo corrige los rótulos de las gráficas inglesas y actualiza la documentación.

## Paso a paso

1. Descarga el ZIP y descomprímelo en una carpeta nueva.
2. Abre tu [repositorio Ingenuity-72-vuelos](https://github.com/PedroRamon-estudios/Ingenuity-72-vuelos), en la rama que utiliza tu publicación actual.
3. Pulsa **Add file → Upload files**. No utilices «Create new file».
4. Sube los archivos y carpetas que hay dentro del ZIP, a la raíz del repositorio. `index.html` e `index-en.html` deben quedar en el mismo nivel que ahora. No subas solamente el ZIP ni una carpeta exterior que englobe todo.
5. Si GitHub limita la cantidad de archivos, haz la carga en grupos: primero `assets`, después `datos` y `analisis`, y después los archivos de la raíz. Conserva sus rutas. Deja los dos `index` para la última carga si divides la actualización.
6. Escribe **Actualizar Ingenuity a v1.4.2: español e inglés revisados** y pulsa **Commit changes** en cada carga.
7. Espera a que termine correctamente el último despliegue de GitHub Pages en **Actions**.
8. Abre [la web española](https://pedroramon-estudios.github.io/Ingenuity-72-vuelos/) y [la inglesa](https://pedroramon-estudios.github.io/Ingenuity-72-vuelos/index-en.html). Pulsa **Ctrl + F5** si ves una copia antigua.

Los archivos con el mismo nombre y la misma ruta se actualizan. Los nuevos se añaden. No se duplican por volver a subirlos correctamente. No cambies los nombres ni añadas sufijos como «(1)» a los archivos del sitio.

## Qué comprobar

- El pie de ambas páginas muestra **Edición 1.4.2** o **Edition 1.4.2**.
- El selector Español | English cambia de idioma.
- La figura del vuelo 9 y las dos gráficas acústicas están rotuladas en inglés al abrir la página inglesa.
- Los documentos de método y fórmulas se abren como páginas legibles en ambos idiomas.
- El mapa salta al vuelo elegido y la ficha del explorador permanece independiente.
- Los cuatro audios cargan y los CSV se descargan.

Las comprobaciones del paquete están en [Revisión de publicación](REVISION_PUBLICACION.md). Preparar y descargar este ZIP no actualiza por sí solo GitHub: la nueva edición aparece cuando se completa la carga y el despliegue.

## Alternativa con GitHub Desktop

Copia el contenido descomprimido sobre la carpeta local del repositorio, conservando las rutas. Revisa los cambios, confirma el commit y pulsa **Push origin**. No es necesario crear otro repositorio ni cambiar la configuración de Pages que ya funciona.

## Difusión

Puedes compartir una sola dirección: el visitante elige el idioma en la propia web. No tiene que descargar ni ejecutar un HTML. Ambos enlaces siguen siendo los mismos. Si la vista previa de LinkedIn conserva una imagen antigua, vuelve a consultar la dirección mediante su [Post Inspector](https://www.linkedin.com/post-inspector/).
