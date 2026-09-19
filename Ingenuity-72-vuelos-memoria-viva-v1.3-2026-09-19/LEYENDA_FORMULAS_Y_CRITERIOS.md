# Leyenda, fórmulas y criterios de interpretación

## Ingenuity: log ampliado de 72 vuelos, imágenes y audio de Marte

**Autor del análisis, la selección y el relato:** Pedro Ramón Montserrat Cabrera  
**Lugar:** Fuerteventura, Islas Canarias, España  
**Versión metodológica:** 19 de septiembre de 2026  
**Derechos:** © 2026 Pedro Ramón Montserrat Cabrera. Todos los derechos reservados.

Este documento explica cómo leer la web, qué representa cada variable, qué fórmulas se han podido verificar en los archivos del proyecto y dónde terminan los datos públicos. Está pensado como guía para estudiantes, docentes, divulgadores y personas que deseen examinar o reproducir el trabajo.

El proyecto es un ejercicio personal e independiente de documentación técnica, curiosidad y aprendizaje. Reúne fuentes públicas dispersas bajo una cronología común, pero no es telemetría interna de Ingenuity, no sustituye los análisis de NASA/JPL y no ha sido avalado por esas instituciones.

---

## 1. Regla principal de lectura

Todas las afirmaciones deben clasificarse en uno de estos niveles:

| Nivel | Significado | Ejemplo |
|---|---|---|
| **OBSERVADO** | Dato visible directamente en una imagen, un audio o una fuente oficial. | En el vuelo 72 aparecen pocas referencias distinguibles en el terreno público y NASA/JPL informó de pérdida de seguimiento visual. |
| **REPRODUCIDO** | Resultado obtenido nuevamente con un procedimiento descrito y datos públicos. | Recuperar la frecuencia de 75,8813 Hz del ensayo JPL o los seis mínimos del vuelo 5. |
| **HIPÓTESIS** | Interpretación físicamente posible que todavía necesita telemetría, imágenes originales completas o ensayos adicionales. | Relacionar una geometría concreta del aterrizaje con el orden de rotura de las palas. |

Una coincidencia entre dos fuentes independientes refuerza una explicación, pero no convierte automáticamente una hipótesis en un hecho demostrado.

---

## 2. Qué reúne el log ampliado

| Capa | Procedencia | Uso dentro del proyecto |
|---|---|---|
| Registro de los 72 vuelos | NASA Science / JPL | Fechas, soles, perfiles, distancias, altitudes, velocidades, duraciones e incidencias. |
| Mapa animado de los 72 vuelos | NASA/JPL-Caltech | Contexto espacial y navegación directa hasta el rótulo de cada vuelo. |
| Montaje cronológico Navcam | Jacint Roger (Landru79), usando imágenes públicas | Recorrido visual continuo y base del análisis exploratorio de referencias. |
| Métricas visuales | Elaboración del proyecto | Comparación uniforme y relativa entre bloques del mismo montaje. |
| Audios SuperCam | NASA Planetary Data System | Análisis de los vuelos 4, 5, 6 y 8. |
| Ensayo terrestre | Vídeo público JPL | Comprobación independiente de la peineta armónica y del régimen de rotor. |
| Evitación de peligros | NASA/JPL, PIA25662, y publicaciones técnicas | Comparación conceptual con reconstrucción 3D, pendiente, rugosidad e incertidumbre. |

La aportación propia está en la selección, organización, comparación, relato, código, visualizaciones y resultados derivados. Los hechos, imágenes, audios y materiales de terceros conservan su autoría y condiciones originales.

---

## 3. Leyenda de la gráfica principal

| Elemento | Qué significa | Qué no significa |
|---|---|---|
| Eje horizontal | Número de vuelo, del 1 al 72. | Tiempo continuo ni distancia recorrida. |
| Eje vertical | Puntuación visual relativa de 0 a 100 dentro del montaje analizado. | Contador interno de rasgos de Ingenuity. |
| Punto | Un bloque provisional asociado a un vuelo. | Una muestra instantánea de telemetría. |
| Línea | Unión visual entre vuelos sucesivos para apreciar tendencias. | Evolución continua entre dos vuelos. |
| Punto resaltado | Vuelo seleccionado en el explorador principal. | Vuelo que está reproduciendo necesariamente el mapa. |
| Marca de incidencia | Vuelo con prueba, anomalía o referencia conocida. | Prueba de que la incidencia fue causada por la textura. |
| Marca de audio | Vuelo 4, 5, 6 u 8 con registro SuperCam estudiado. | Grabación completa y audible de todo el vuelo. |
| Zona final | Vuelos 68–72. | Una categoría oficial de NASA. |

### Categorías editoriales de la puntuación

- **Menos de 20:** referencias visuales bajas.
- **De 20 a menos de 45:** referencias reducidas o distribuidas de forma limitada.
- **45 o más:** referencias relativamente abundantes.

Son umbrales internos para facilitar la lectura del mismo conjunto. No son límites de seguridad, navegación o certificación definidos por NASA/JPL.

### Independencia de los dos índices

El explorador principal y el mapa oficial tienen estados independientes:

- los botones superiores, el desplegable, la gráfica y la tabla cambian la ficha y la imagen fija;
- únicamente el índice situado junto al mapa mueve y reproduce el vídeo del mapa;
- al avanzar el mapa, sólo se actualiza su propio índice.

Esta separación permite detenerse en los valores de un vuelo mientras el mapa recorre otro tramo.

---

## 4. Segmentación y muestreo visual

### 4.1 Conversión entre fotograma y tiempo

El montaje analizado tiene:

- \(N_f=22\,546\) fotogramas;
- \(F_s=25\) fotogramas por segundo;
- duración \(T=901,84\ \text{s}\).

Para un fotograma de índice \(k\), su tiempo es:

\[
t_k=\frac{k}{F_s}
\]

La duración se comprueba mediante:

\[
T=\frac{N_f}{F_s}=\frac{22\,546}{25}=901,84\ \text{s}
\]

### 4.2 Delimitación de vuelos

Se identificaron 75 pasos de sombra grande. Tres, situados entre los vuelos 13 y 14, se consideraron comprobaciones previas y no vuelos. El resultado fue una asignación provisional de 72 bloques.

De cada bloque se tomaron 20 fotogramas del tramo central. Se evita así que una única imagen extrema determine por sí sola el valor de todo el vuelo.

### 4.3 Advertencia temporal

Los campos `video_inicio_s` y `video_fin_s` pertenecen al montaje de Landru79. No son segundos reales desde el despegue ni duración oficial del vuelo.

---

## 5. Variables visuales y fórmulas

### 5.1 Referencias visuales

En cada muestra se estimó un número de esquinas o rasgos locales mediante un procedimiento semejante a Harris/Shi–Tomasi, después de recortar el viñeteado y enmascarar aproximadamente la sombra.

Si \(r_{i,k}\) es el número de referencias del fotograma \(k\) perteneciente al vuelo \(i\), el valor representativo almacenado es la mediana:

\[
R_i=\operatorname{mediana}\left(r_{i,1},r_{i,2},\ldots,r_{i,20}\right)
\]

La mediana es menos sensible que la media a un fotograma excepcionalmente claro, oscuro o comprimido.

### 5.2 Rango intercuartílico

La variabilidad de las 20 muestras se resume con:

\[
IQR_i=Q_{3,i}-Q_{1,i}
\]

donde \(Q_1\) es el percentil 25 y \(Q_3\) el percentil 75. Un IQR alto significa que el número de referencias cambia mucho dentro del bloque; no significa necesariamente inestabilidad del helicóptero.

### 5.3 Cobertura espacial

La imagen útil se divide en una cuadrícula 4 × 4. Para cada celda útil se comprueba si contiene al menos dos referencias. La definición general es:

\[
C_i=100\,\frac{\sum_{c\in U_i}\mathbf{1}(n_{i,c}\geq 2)}{|U_i|}
\]

donde:

- \(U_i\) es el conjunto de celdas utilizables después de las máscaras;
- \(n_{i,c}\) es el número de referencias asociado a la celda \(c\);
- \(\mathbf{1}(\cdot)\) vale 1 cuando se cumple la condición y 0 cuando no.

La cobertura distingue dos casos que un contador total puede confundir: muchos rasgos concentrados en un rincón y una cantidad parecida repartida por la imagen.

### 5.4 Percentil de referencias

El campo `percentil_referencias` sí puede reconstruirse exactamente desde el CSV. Para \(N=72\), si \(q_i\) es el rango ascendente de \(R_i\), usando el rango medio cuando existen empates:

\[
P_i=100\,\frac{q_i-1}{N-1}
\]

Así, el valor menor ocupa el percentil 0 y el mayor el 100. Este cálculo reproduce todos los valores publicados después de redondear a una cifra decimal.

### 5.5 Puntuación visual relativa

La puntuación se utiliza como índice sintético normalizado para ordenar los bloques del propio montaje. Debe interpretarse como una comparación relativa, no como una magnitud física.

**Estado de reproducibilidad:** el paquete distribuido conserva el CSV resultante y la descripción conceptual, pero no contiene el programa original de extracción visual, sus umbrales ni la ponderación exacta que combinó las variables en `puntuacion_visual`. Por rigor, este documento no inventa una fórmula retrospectiva.

Hasta que se recupere o reconstruya y valide ese programa, son plenamente auditables la tabla final, la mediana de referencias, su percentil, las comparaciones estadísticas y el código acústico; la generación completa de la puntuación visual desde el vídeo debe considerarse **parcialmente reproducible**.

Esta es la principal mejora metodológica pendiente del repositorio: publicar el detector visual con versiones de librerías, máscaras, parámetros, agregación de cobertura y fórmula exacta de la puntuación.

### 5.6 Variables auxiliares

| Campo | Lectura permitida | Precaución |
|---|---|---|
| `textura` | Variación o estructura tonal auxiliar en la imagen. | No equivale a rugosidad física ni a pendiente. |
| `sombra_pct` | Proporción estimada afectada por la máscara de sombra. | No mide altura ni proximidad al suelo. |
| `cambio_visual` | Cambio auxiliar entre muestras. | No equivale directamente a velocidad. |
| `dispersion_sombra` | Variación de la medida de sombra dentro del bloque. | No diagnostica actitud, rotor o servos. |
| `confianza_asignacion` | Confianza editorial en la asociación bloque–vuelo. | No es probabilidad de fallo ni seguridad de aterrizaje. |

Las fórmulas exactas de estas cuatro variables auxiliares tampoco se conservan en el paquete actual y no deben reconstruirse por conjetura.

---

## 6. Comparaciones estadísticas

Para comprobar si la mediana de referencias dependía simplemente de la distancia, altura, velocidad o duración oficiales, se utilizó la correlación de rangos de Spearman.

Para dos series \(X\) e \(Y\), se sustituyen los valores por sus rangos y se calcula:

\[
\rho_s=\operatorname{corr}\left(\operatorname{rango}(X),\operatorname{rango}(Y)\right)
\]

Cuando no existen empates puede expresarse como:

\[
\rho_s=1-\frac{6\sum d_i^2}{N(N^2-1)}
\]

donde \(d_i\) es la diferencia entre rangos. En este conjunto de 72 vuelos se obtuvieron:

| Variable oficial frente a referencias visuales | \(\rho_s\) | \(p\) |
|---|---:|---:|
| Distancia | −0,061 | 0,613 |
| Altura máxima | −0,017 | 0,891 |
| Velocidad máxima | −0,127 | 0,287 |
| Duración | −0,046 | 0,703 |

No aparece una relación monótona significativa con esas cuatro variables. Esto no demuestra causalidad a favor del terreno; indica que la cantidad de referencias del montaje no se explica simplemente por vuelos más largos, altos o rápidos.

### Resultado descriptivo de la secuencia final

\[
\operatorname{mediana}(R_{1\ldots67})=46,5
\]

\[
\operatorname{mediana}(R_{68\ldots72})=11,0
\]

Para el vuelo 72:

\[
R_{72}=8,0,\qquad C_{72}=20,83\%,\qquad S_{72}=6,1
\]

La persistencia de valores bajos en varios vuelos finales es más interesante que tratar el vuelo 72 como una única imagen aislada. Aun así, no demuestra una degradación progresiva del sistema.

---

## 7. Vuelo 9 y evitación de peligros

### 7.1 Qué muestran realmente las imágenes de NASA/JPL

La animación PIA25662 utiliza imágenes del vuelo 9, realizado el 5 de julio de 2021, pero fueron **reprocesadas después** con una capacidad añadida mediante una actualización de software a finales de 2022.

- rojo: regiones clasificadas como no aptas para aterrizar;
- verde: candidatos de aterrizaje;
- las cifras rojas, marcas cian y rectángulos blancos no están definidos con precisión en la ficha pública y no se les asignan unidades en este proyecto.

La publicación técnica asociada describe esta cadena:

1. secuencia de imágenes monoculares;
2. estimación de pose mediante odometría visual–inercial;
3. selección de pares de imágenes y reconstrucción de profundidad por *Structure from Motion*;
4. fusión temporal en un mapa de elevación multirresolución;
5. evaluación de pendiente, rugosidad y calidad o incertidumbre;
6. mapa binario seguro/peligroso;
7. selección de candidatos alejados de obstáculos mediante transformada de distancia.

### 7.2 ¿Coincide con nuestro procesamiento?

**Coincide en la condición inicial, pero no en el algoritmo ni en las unidades.**

| Aspecto | Sistema descrito por JPL | Métrica del proyecto | Correspondencia |
|---|---|---|---|
| Necesidad de estructura visible | Sí; la reconstrucción falla o pierde confianza en regiones sin textura. | Sí; se cuentan referencias locales detectables. | **Coincidencia conceptual fuerte.** |
| Distribución espacial | Importa para reconstruir y evaluar una zona. | Se aproxima mediante cobertura 4 × 4. | **Coincidencia conceptual.** |
| Uso de una secuencia | Fusiona imágenes y poses a lo largo del tiempo. | Resume 20 imágenes del montaje, sin reconstrucción métrica. | **Métodos distintos.** |
| Relieve 3D | Calcula profundidad y mapa de elevación. | No calcula profundidad. | **No equivalente.** |
| Pendiente y rugosidad físicas | Criterios directos del mapa. | `textura` no tiene esas unidades. | **No comparable numéricamente.** |
| Incertidumbre | Forma parte de la calidad del mapa. | No existe una varianza métrica equivalente. | **No comparable.** |
| Elección del lugar | Genera candidatos verdes tras descartar peligros. | No decide lugares de aterrizaje. | **Finalidad diferente.** |

En el vuelo 9, el proyecto obtuvo 12,5 referencias medianas, 25 % de cobertura y una puntuación relativa de 12,9. Que el valor sea bajo y el reprocesamiento de JPL encuentre candidatos verdes no es una contradicción: JPL fusiona una secuencia para construir geometría 3D, mientras nuestro índice utiliza una selección pública, comprimida y sin pose ni profundidad.

Al inspeccionar los fotogramas de PIA25662 se observa que los grupos de rocas y relieves conservan geometría y aparecen mayoritariamente dentro del sombreado rojo, mientras los candidatos verdes se sitúan sobre regiones visualmente más uniformes. Esa correspondencia es **cualitativa**. Sin las imágenes originales, calibración, poses, parámetros y mapas intermedios no puede hacerse una validación píxel a píxel de nuestro método contra el de vuelo.

### Conclusión defendible

> El vídeo del vuelo 9 confirma que la estructura visual del terreno es una condición necesaria para reconstruir el entorno y evaluar un aterrizaje. Nuestra métrica examina esa condición previa de manera simplificada, pero no reproduce ni calibra el algoritmo de evitación de peligros de JPL.

---

## 8. El aterrizaje próximo a una piedra

La referencia conservada corresponde al **vuelo 33**, efectuado el 24 de septiembre de 2022 (sol 567): vuelo horizontal de unos 111 m, con 10 m de altura máxima, 4,75 m/s y unos 55 s de duración.

### 8.1 La pregunta correcta

No es seguro preguntar «¿por qué Ingenuity vio la piedra y decidió aterrizar allí?». La demostración pública de evitación de peligros fue incorporada mediante una actualización a finales de 2022. El vuelo 33 ocurrió antes y la documentación pública disponible no permite atribuirle esa selección autónoma de candidatos.

La interpretación más probable es:

1. el equipo planificó en Tierra un punto de destino;
2. durante el vuelo, la cámara Navcam estimó el movimiento horizontal siguiendo rasgos del terreno;
3. el altímetro láser aportó la distancia al suelo;
4. el controlador intentó llegar y descender dentro de la envolvente prevista;
5. la piedra quedó cerca del tren, pero aparentemente fuera de la huella efectiva de contacto.

Por tanto, el helicóptero pudo aterrizar correctamente **sin haber clasificado esa piedra como un peligro individual**.

### 8.2 Explicaciones compatibles, ordenadas por plausibilidad

| Posibilidad | Valoración |
|---|---|
| La piedra estaba fuera de la huella de las cuatro patas y del margen realmente necesario. | Alta; proximidad visual no equivale a contacto. |
| El punto fue preseleccionado con información de menor resolución y la dispersión normal dejó el tren más cerca de la piedra. | Plausible. |
| La perspectiva cenital, la sombra y la falta de una escala local hacen parecer menor la separación. | Plausible y difícil de cuantificar. |
| El sistema detectó la piedra, calculó su riesgo y decidió aceptarla. | No demostrado para ese vuelo. |
| Ingenuity eligió deliberadamente una loma o una piedra porque las prefería. | Hipótesis no apoyada por telemetría pública. |

### 8.3 Qué no puede calcularse todavía

- La distancia exacta entre la piedra y cada pata sin escala y geometría calibradas.
- El tamaño exacto de la piedra a partir de una captura comprimida.
- El orden de contacto de las cuatro patas.
- La pendiente local bajo cada apoyo.
- Si el punto de contacto real se desplazó respecto al objetivo programado.
- Qué mapa o margen de seguridad estaba disponible para los planificadores.

Las antiguas estimaciones visuales de unos 25–35 cm de tamaño y 30–40 cm de separación deben considerarse aproximaciones preliminares, no medidas publicables, hasta disponer de una referencia geométrica calibrada.

Esta imagen es valiosa porque plantea una pregunta real de ingeniería: un lugar puede ser navegable y permitir el contacto del tren aunque contenga un obstáculo cercano. **Navegabilidad visual, seguridad geométrica y estabilidad de cuatro apoyos no son la misma magnitud.**

La captura del vuelo 70 sobre dunas es otra referencia del proyecto y no debe confundirse con esta imagen del vuelo 33.

---

## 9. Hipótesis de las 31–32 lomas

### 9.1 Origen y formulación correcta

En la serie de LinkedIn **«Anatomía de la Rotura de una Pala del Ingenuity»**, Pedro Ramón Montserrat Cabrera publicó la observación de que numerosos despegues, aterrizajes o vuelos verticales parecían producirse sobre cimas, aristas, faldas de dunas o lomas, incluso cuando en la proyección de la imagen se apreciaban zonas aparentemente más llanas.

El texto conservado de una de esas publicaciones dice que se revisaron **31 imágenes**. La expresión «unas 32 lomas» debe entenderse, por tanto, como una cifra aproximada de la investigación inicial, no como 32 aterrizajes independientes ya verificados. Tampoco debe mezclarse con otra estimación preliminar, publicada anteriormente, de «unos 25 aterrizajes».

La formulación defendible es:

> **Hipótesis L:** dentro de la selección pública de imágenes revisada se observa una recurrencia aparente de posiciones finales próximas a crestas, lomas o zonas arenosas elevadas. Falta comprobar si esa recurrencia supera la disponibilidad de ese tipo de terreno, el sesgo de la ruta, la selección de imágenes y los errores de perspectiva.

Esta observación es una aportación editorial y una pregunta de investigación del autor. **No es una conclusión publicada por NASA/JPL ni demuestra que Ingenuity “prefiriera” autónomamente las lomas.**

### 9.2 Por qué es una pregunta interesante

La hipótesis enlaza tres problemas que no deben confundirse:

1. **Planificación de ruta:** el equipo de Tierra escogía destinos compatibles con la progresión de Perseverance y con las imágenes disponibles.
2. **Navegación visual:** Ingenuity necesitaba textura suficiente para estimar movimiento respecto al suelo.
3. **Seguridad geométrica:** pendiente, rugosidad, rocas y huella de las cuatro patas determinan si una zona permite posarse.

Una loma puede ofrecer contraste y estar libre de rocas, pero tener pendiente; una zona aparentemente plana puede ser pobre en textura o contener obstáculos. Eso hace que la observación sea físicamente razonable como pregunta, pero no prueba un sesgo del software.

### 9.3 Qué puede producir un falso patrón

- **Sesgo de muestra:** sólo se publicaron determinadas imágenes y no una secuencia calibrada completa de cada aterrizaje.
- **Pseudorreplicación:** varias fotografías del mismo vuelo no equivalen a varios aterrizajes.
- **Perspectiva:** una vista cenital monocular puede desplazar visualmente la cresta o la huella.
- **Disponibilidad:** si gran parte de la ruta atraviesa dunas, encontrar muchas lomas no implica preferencia.
- **Planificación previa:** en los vuelos anteriores a la actualización de finales de 2022 no debe atribuirse a la evitación autónoma de peligros una elección que pudo ser programada desde Tierra.
- **Definición flexible:** «cima», «falda», «cerca» o «rozar» deben convertirse en categorías y distancias objetivas antes de contar.

### 9.4 Protocolo propuesto para comprobarla

El repositorio incorpora `datos/plantilla_revision_lomas.csv` para registrar una fila por vuelo y evitar que el número cambie según la impresión visual. El estudio debería:

1. fijar antes de revisar las imágenes las clases `cresta`, `loma`, `falda`, `depresión`, `plano` e `indeterminado`;
2. usar una sola observación por aterrizaje, con sol, producto PDS, instante y fuente trazables;
3. separar destino planificado, posición final observada y candidato autónomo confirmado;
4. pedir a dos personas que clasifiquen cada caso sin conocer la hipótesis;
5. medir el acuerdo entre observadores;
6. comparar el número de aterrizajes sobre loma con la proporción de superficie candidata que ocupaban las lomas en cada zona;
7. publicar también los casos negativos e indeterminados.

Si (k) de (n) aterrizajes independientes cumplen la definición preestablecida, la proporción descriptiva es:

\[
\widehat p=\frac{k}{n}
\]

Pero el contraste correcto no es necesariamente contra 0,5: el valor de referencia (p_0) debe ser la proporción de terreno disponible que ya pertenecía a esa clase. Sin esa medida de disponibilidad no puede hablarse de preferencia.

### 9.5 Estado actual

| Afirmación | Estado |
|---|---|
| El autor publicó en LinkedIn una recurrencia aparente tras revisar 31 imágenes. | **Documentado.** |
| En varias imágenes se ven posiciones próximas a lomas, aristas o dunas. | **Observación visual cualitativa.** |
| Existen exactamente 31 o 32 aterrizajes autónomos sobre lomas. | **No verificado.** |
| Ingenuity eligió las lomas porque su visión las consideraba más seguras. | **Hipótesis.** |
| Ese supuesto patrón causó la rotura de las palas en el vuelo 72. | **No demostrado.** |

La manera más sólida de difundir esta idea en un canal aeroespacial es presentar la cifra como **muestra inicial de 31 imágenes**, acompañarla de los casos y contraejemplos, y reservar «preferencia» para el momento en que exista un denominador y una comparación estadística.

---

## 10. Vuelos 62, 68 y 69: máxima velocidad y posible carga acumulada

### 10.1 Corrección del registro

La velocidad máxima sobre el suelo de Ingenuity, **10 m/s**, aparece oficialmente en tres vuelos: **62, 68 y 69**. El vuelo 65 no pertenece a este grupo: recorrió aproximadamente 7 m y su velocidad máxima registrada fue 1 m/s.

| Vuelo | Fecha | Distancia | Duración | Velocidad máxima | Finalidad relevante |
|---:|---|---:|---:|---:|---|
| 62 | 12 oct. 2023 | 268 m | 121,1 s | 10 m/s | Primera demostración de 10 m/s, a 18 m de altura de vuelo horizontal. |
| 68 | 15 dic. 2023 | 702 m | 131,1 s | 10 m/s | Ensayo dedicado de identificación de sistemas (`Sys-ID`). |
| 69 | 20 dic. 2023 | 705 m | 135,4 s | 10 m/s | Segundo `Sys-ID`, con otro recorrido largo de ida y vuelta. |

NASA/JPL explica que en los vuelos 68 y 69 se inyectó un barrido sinusoidal de frecuencia en la entrada de control para provocar un «cabeceo» microscópico durante el vuelo horizontal. El objetivo era identificar la dinámica real de la aeronave en Marte. El recorrido de ida y vuelta garantizaba que, con el viento esperado, al menos un tramo se volara de cara al viento y alcanzara una **velocidad respecto al aire superior a 10 m/s**, dentro y más allá de lo ensayado en Tierra.

Esto convierte la observación en una pregunta técnica legítima: los dos vuelos no sólo fueron largos y rápidos, sino ensayos dinámicos deliberados ejecutados al final de la vida operacional del helicóptero.

### 10.2 Qué cambia físicamente al volar más rápido

La velocidad sobre el suelo no debe confundirse con las revoluciones del rotor ni con una medida directa de esfuerzo. En avance, una variable útil es la razón de avance:

\[
\mu=\frac{V_{aire}}{\Omega R}
\]

donde (V_{aire}) es la velocidad respecto al aire, (\Omega) la velocidad angular del rotor y (R) su radio. Al aumentar (\mu), crece la diferencia de velocidad relativa entre la pala que avanza y la que retrocede. El control debe compensarla mediante paso cíclico, y pueden aumentar determinadas cargas alternantes de flexión, torsión y acoplamiento aeroelástico.

La presión dinámica asociada al movimiento de avance sigue:

\[
q=\frac{1}{2}\rho V_{aire}^{2}
\]

Por tanto, pasar de 5 a 10 m/s cuadruplica ese término de presión dinámica si la densidad es la misma. Esto resulta relevante para el fuselaje y las contribuciones aerodinámicas ligadas a la traslación, pero **no significa que la tensión total de las palas se cuadruplicara**: el flujo local de la pala está dominado además por su elevada velocidad de rotación, su posición azimutal y el paso aplicado.

El `Sys-ID` añade pequeñas excitaciones oscilatorias deliberadas. Eso es valioso para identificar el modelo dinámico, pero **no equivale automáticamente a exceder los límites estructurales**. Tampoco puede suponerse que el vuelo rápido consumiera siempre más potencia que el estacionario: la relación potencia–velocidad de un rotorcraft no es monótona y depende del perfil completo, la densidad, el viento, la actitud y el control.

### 10.3 Tiempo, ciclos y fatiga: lo que sí puede calcularse

Los vuelos 68 y 69 acumularon juntos:

\[
T_{68+69}=131{,}1+135{,}4=266{,}5\ \mathrm{s}=4{,}44\ \mathrm{min}
\]

Frente a los 7.731,3 s de vuelo del registro completo, representan aproximadamente:

\[
100\frac{266{,}5}{7.731{,}3}=3{,}45\%
\]

Si se usa únicamente como aproximación un régimen constante de 2.537 rpm, el número de vueltas sería:

\[
N_{vueltas}\simeq \frac{rpm\,T}{60}
\]

lo que da unas 5.121 vueltas en el vuelo 62, 5.543 en el 68, 5.725 en el 69 y 11.269 entre los dos últimos. Estas cifras **no son telemetría de rotor, no equivalen a ciclos de daño y no incorporan las variaciones reales de rpm ni la amplitud de los esfuerzos**.

Una investigación de fatiga necesitaría, como mínimo, un espectro de cargas y una relación tensión–vida del material. Como marco conceptual puede escribirse la regla acumulativa de Miner:

\[
D=\sum_j\frac{n_j}{N_j}
\]

donde (n_j) es el número de ciclos soportados a un nivel de tensión y (N_j) los ciclos hasta fallo para ese nivel. El tiempo total por sí solo no permite obtener (D): pocos ciclos de gran amplitud pueden pesar más que muchos ciclos suaves.

### 10.4 Contraste con el accidente del vuelo 72

La evaluación pública de JPL del 11 de diciembre de 2024 atribuye la cadena más probable a la falta de textura durante el vuelo 72: pérdida de referencias, estimación de velocidad deficiente, alta velocidad horizontal al contacto, impacto duro sobre la pendiente de una ondulación de arena, cambio rápido de actitud y cargas sobre las palas por encima de sus límites de diseño. JPL indica que las cuatro palas se rompieron en su sección más débil.

Con la información pública disponible:

| Proposición | Valoración |
|---|---|
| Los vuelos 62, 68 y 69 ampliaron deliberadamente la envolvente a 10 m/s. | **Confirmado por NASA.** |
| Los vuelos 68 y 69 añadieron excitaciones dinámicas y al menos un tramo por encima de 10 m/s de velocidad respecto al aire. | **Confirmado por NASA/JPL.** |
| Esos perfiles pudieron producir cargas cíclicas distintas de las de un vuelo ordinario. | **Físicamente plausible.** |
| Dejaron microdaño o redujeron el margen resistente de las palas. | **No demostrado con datos públicos.** |
| Fueron la causa de la rotura del vuelo 72. | **No respaldado; la atribución causal principal publicada es la sobrecarga del aterrizaje.** |

Los vuelos 68 y 69 fueron declarados exitosos, e Ingenuity realizó después los vuelos 70 y 71. No se ha publicado una anomalía estructural derivada de los `Sys-ID`. La rotura casi simultánea de las cuatro palas cerca de una sección débil es coherente con un episodio de sobrecarga común durante el aterrizaje; una degradación previa podría reducir el margen, pero no puede confirmarse ni descartarse sin telemetría de vibración, órdenes de paso, rpm, corriente, temperaturas, cargas de raíz e inspección del material.

La formulación científicamente más fuerte para el log es, por tanto:

> **Hipótesis V:** la campaña de alta velocidad y `Sys-ID` de los vuelos 62, 68 y 69 pudo constituir un historial de carga relevante que convendría contrastar con la telemetría estructural. Los datos públicos demuestran la expansión de la envolvente, pero no demuestran daño acumulado ni una contribución causal a la rotura del vuelo 72.

El archivo [`datos/vuelos_alta_velocidad_hipotesis.csv`](datos/vuelos_alta_velocidad_hipotesis.csv) conserva las magnitudes y el nivel de evidencia utilizado en esta comparación.

---

## 11. Audio: datos, normalización y espectro

### 11.1 Por qué los cuatro WAV ocupan lo mismo

Los WAV PDS de los vuelos 4, 5, 6 y 8 tienen la misma estructura:

- duración: 167 s;
- frecuencia de muestreo: 25.000 muestras/s;
- canales: 1;
- resolución almacenada: 32 bits = 4 bytes por muestra.

El tamaño de los datos es:

\[
167\times25\,000\times1\times4=16\,700\,000\ \text{bytes}
\]

Al sumar 58 bytes de cabecera y metadatos del contenedor:

\[
16\,700\,000+58=16\,700\,058\ \text{bytes}
\]

Por eso los cuatro archivos pesan exactamente lo mismo. Sus huellas SHA-256 son diferentes, de modo que su contenido no es idéntico.

### 11.2 Preparación de señal

El programa `analisis/comparar_audio.py` convierte a coma flotante cuando es necesario, combina canales si hubiera más de uno y elimina la media:

\[
x_0[n]=x[n]-\overline{x}
\]

Los MP3 locales están filtrados entre 60 y 220 Hz y normalizados para escuchar. Las mediciones deben realizarse siempre sobre los WAV PDS.

### 11.3 Densidad espectral de potencia

Se usa Welch con:

- ventana Hann;
- segmentos de hasta 65.536 muestras;
- solape del 50 %;
- FFT de 131.072 puntos;
- presentación principal entre 60 y 250 Hz.

De forma esquemática:

\[
\widehat{P}_{xx}(f)=\frac{1}{M}\sum_{m=1}^{M}\frac{|\operatorname{FFT}(w[n]x_m[n])|^2}{F_s\sum_n w^2[n]}
\]

La escala relativa es:

\[
P_{dB}(f)=10\log_{10}\left(\widehat{P}_{xx}(f)+\varepsilon\right)-\max_{60\leq f\leq250}P_{dB}(f)
\]

Cada registro tiene su máximo igualado a 0 dB. Esto permite comparar posiciones espectrales, no amplitudes acústicas absolutas.

---

## 12. Frecuencia de paso de pala y régimen

Si cada rotor tiene \(B=2\) palas y gira a \(n\) rpm:

\[
f_{BPF}=B\frac{n}{60}
\]

Por tanto:

\[
n=\frac{60f_{BPF}}{B}=30f_{BPF}
\]

Ejemplos:

\[
75,8813\ \text{Hz}\times30=2\,276,44\ \text{rpm}
\]

\[
84,4\ \text{Hz}\times30=2\,532\ \text{rpm}
\]

La segunda componente principal esperada es:

\[
f_2=2f_{BPF}\approx168,8\ \text{Hz}
\]

En nomenclatura matemática es el segundo armónico (`2×BPF`). El artículo lo llama *first harmonic*, uso equivalente a «primer sobretono». Para evitar ambigüedad, este repositorio muestra siempre el multiplicador `2×BPF`.

La línea próxima a 195 Hz pertenece a equipos del rover y no debe atribuirse al rotor.

### Ajuste de la peineta armónica JPL

Si los máximos medidos \(f_k\) corresponden a armónicos \(k=1,\ldots,K\), el ajuste forzado al origen es:

\[
\widehat f_0=\frac{\sum_{k=1}^{K}k f_k}{\sum_{k=1}^{K}k^2}
\]

El residuo se resume con:

\[
RMSE=\sqrt{\frac{1}{K}\sum_{k=1}^{K}(f_k-k\widehat f_0)^2}
\]

Para los 14 picos armónicos medidos en la captura del ensayo:

\[
\widehat f_0=75,8813\ \text{Hz},\qquad RMSE=0,018\ \text{Hz}
\]

El régimen equivalente es 2.276,44 rpm, sólo 0,56 rpm por debajo de las 2.277 rpm indicadas en el vídeo.

### Dos comprobaciones diferentes

La cifra anterior procede de 14 picos medidos en la captura del vídeo oficial de JPL. El apéndice 3 del paper aporta una referencia independiente:

- **Figura A2:** fotografía o vista del montaje en la cámara de presión marciana.
- **Figura A3:** espectro, espectrograma y señal temporal, con una separación cercana a 82 Hz y al menos 15 dientes visibles.

La correspondencia defendible es una **estructura armónica equivalente** generada por la frecuencia de paso de pala de la misma arquitectura de dos rotores coaxiales. No se afirma que ambas figuras procedan de la misma grabación ni que deban coincidir en frecuencia exacta, tramo, amplitud o unidades.

Por eso se mantienen separadas estas dos formulaciones:

\[
75,8813\ \text{Hz}\times30=2\,276,44\ \text{rpm}
\]

para el vídeo analizado, y «peine cercano a 82 Hz» para la figura A3 publicada.

---

## 13. Envolventes y mínimos

### 13.1 Vuelo 5

El WAV se reduce a 1.000 muestras/s, se aplica un Butterworth de cuarto orden entre 81,5 y 87 Hz con filtrado hacia delante y hacia atrás, y se calcula la envolvente analítica:

\[
z(t)=x_f(t)+j\mathcal{H}\{x_f(t)\}
\]

\[
A(t)=|z(t)|
\]

\[
A_{dB}(t)=20\log_{10}(A(t)+\varepsilon)
\]

Después se suaviza con un filtro gaussiano de \(\sigma=0,5\ \text{s}\) y se resta el percentil 95 del intervalo 20–125 s.

Los mínimos reproducidos son:

\[
36,3;\ 46,8;\ 57,5;\ 71,7;\ 88,2;\ 103,7\ \text{s}
\]

Sus intervalos sucesivos son:

\[
10,5;\ 10,7;\ 14,2;\ 16,5;\ 15,5\ \text{s}
\]

Los tiempos publicados por Lorenz et al. son 36, 47, 57, 72, 88 y 104 s. La reproducción difiere menos de un segundo.

El programa actual conserva estos mínimos como puntos ya medidos; no contiene todavía un detector automático con prominencia, distancia mínima y criterio de aceptación completamente documentados.

### 13.2 Peine armónico del ensayo JPL

El ensayo se reduce a 4.000 muestras/s y se analiza mediante STFT:

- ventana Hann de 8.192 muestras, equivalente a 2,048 s;
- salto de 512 muestras, equivalente a 0,128 s;
- FFT de 32.768 puntos, con separación aproximada de 0,122 Hz;
- seguimiento de la fundamental entre 70 y 82 Hz;
- suma de potencia en ±0,9 Hz alrededor de los armónicos 1–12.

Para cada tiempo \(t\):

\[
E_{peine}(t)=\sum_{h=1}^{12}\sum_{|f-hf_0(t)|\leq0,9}|X(f,t)|^2
\]

\[
E_{dB}(t)=10\log_{10}(E_{peine}(t)+\varepsilon)
\]

La curva se normaliza restando el percentil 95 entre 12 y 82 s. Sus mínimos se relacionan principalmente con maniobras, orientación, distancia, reverberación y control automático de ganancia; no forman la cadencia organizada del vuelo 5.

---

## 14. Teoría ΔRPM y faro acústico

### 14.1 Origen de la idea

El mecanismo físico fue propuesto por Lorenz et al. (2023): una diferencia muy pequeña entre las velocidades de los dos rotores coaxiales hace que cambie lentamente la orientación relativa de sus palas. El patrón direccional de emisión gira como un faro y un observador fijo atraviesa máximos y mínimos acústicos.

La aportación de este proyecto no es reclamar el mecanismo como un descubrimiento propio, sino:

- reproducir los mínimos del vuelo 5 desde el WAV PDS;
- contrastarlos con las sombras Navcam publicadas;
- compararlos con un ensayo terrestre JPL;
- documentar la conversión entre periodo y diferencia de régimen;
- mostrar por qué los mínimos no deben interpretarse como paradas del rotor.

### 14.2 Superposición algebraica

Para dos tonos próximos de igual amplitud:

\[
p(t)=A\sin(2\pi f_1t+\phi_1)+A\sin(2\pi f_2t+\phi_2)
\]

puede escribirse como una oscilación rápida multiplicada por una envolvente lenta. La intensidad media queda modulada aproximadamente por:

\[
I(t)\propto\cos^2\left(\pi\Delta f\,t+\phi\right)
\]

donde \(\Delta f=|f_1-f_2|\). Si \(f_1\) y \(f_2\) son frecuencias de paso de pala de rotores de dos palas:

\[
\Delta f_{BPF}=\frac{2\Delta n}{60}
\]

Si el intervalo medido representa un ciclo completo de batido:

\[
\Delta n_{batido}=\frac{30}{T}\quad\text{rpm}
\]

### 14.3 Modelo geométrico de cuatro lóbulos

El modelo de faro del artículo tiene cuatro direcciones principales de mínimo. Si el patrón gira a la diferencia relativa \(\Delta n\), pasan cuatro nulos por cada vuelta relativa:

\[
T_{nulo}\approx\frac{60}{4\Delta n}
\]

y por tanto:

\[
\boxed{\Delta n_{faro}\approx\frac{15}{T_{nulo}}\quad\text{rpm}}
\]

Aplicado a los intervalos del vuelo 5:

| \(T_{nulo}\) (s) | \(\Delta n=15/T\) (rpm) |
|---:|---:|
| 10,5 | 1,43 |
| 10,7 | 1,40 |
| 14,2 | 1,06 |
| 16,5 | 0,91 |
| 15,5 | 0,97 |

Resultado descriptivo:

\[
\Delta n\approx0,9\text{–}1,5\ \text{rpm}
\]

con media aproximada de 1,15 rpm y mediana de 1,06 rpm. Frente a un régimen nominal de unas 2.537 rpm representa aproximadamente entre 0,036 % y 0,056 %.

### 14.4 Por qué también aparece una estimación doble

La fórmula algebraica del batido proporciona \(30/T\), mientras el paso entre lóbulos del faro proporciona \(15/T\). No es correcto mezclarlas: describen convenciones diferentes sobre qué ciclo representa el intervalo observado.

- interpretación de **batido BPF completo**: aproximadamente 1,8–2,9 rpm;
- interpretación **geométrica de cuatro lóbulos**, apoyada por las sombras: aproximadamente 0,9–1,5 rpm.

El repositorio adopta la segunda como estimación principal porque los mínimos se comparan con orientaciones sucesivas del patrón de cuatro lóbulos. Aun así, la trayectoria cambia el ángulo helicóptero–rover, el régimen no tiene por qué ser constante y los tiempos tienen incertidumbre. Por ello, ΔRPM debe publicarse como **orden de magnitud e hipótesis cuantitativa**, nunca como telemetría exacta.

### 14.5 Qué demuestra y qué no

| Afirmación | Estado |
|---|---|
| Existe modulación organizada de 10–20 s en el vuelo 5. | Observado y reproducido. |
| Los intervalos de sombras y audio son de escala semejante. | Observado en el artículo y compatible con la reproducción. |
| Una pequeña asincronía puede producir un faro acústico. | Modelo físico publicado y plausible. |
| ΔRPM estuvo aproximadamente en el orden de 1 rpm bajo el modelo de cuatro lóbulos. | Inferencia. |
| Esa diferencia era una avería. | No apoyado; sería menor del 0,1 % y compensable por control. |
| Los nulos significan que el rotor se detuvo. | Falso. |
| La modulación causó el accidente del vuelo 72. | Sin evidencia. |

---

## 15. Grado actual de reproducibilidad

| Parte | Estado | Material disponible |
|---|---|---|
| Datos oficiales de los vuelos | Alto | CSV y fuentes enlazadas. |
| Índice del mapa | Alto | 72 tiempos, criterio del primer rótulo estable y precisión ±0,1 s. |
| Percentil de referencias | Completo | Fórmula y CSV. |
| Correlaciones de Spearman | Completo | Fórmula, 72 registros y resultados. |
| Comparación acústica | Alto | WAV PDS enlazados, código Python, parámetros y CSV derivados. |
| Envolvente del vuelo 5 | Alto para la curva; parcial para selección automática de mínimos | Código y tiempos medidos. |
| Segmentación visual | Parcial | Límites y resultados, pero faltan detector y umbrales originales. |
| Puntuación visual | Parcial | Resultado publicado; falta ponderación exacta. |
| Comparación píxel a píxel con evitación JPL | No posible con el material público actual | Faltan productos originales e intermedios del algoritmo. |
| Reconstrucción del aterrizaje junto a la piedra | Hipotética | Falta geometría calibrada y telemetría de contacto. |

Publicar también el generador visual es la acción que más elevaría el proyecto desde una cronología técnica muy cuidada hasta un paquete completamente reproducible por terceros.

---

## 16. Conclusiones técnicas más interesantes

1. **La secuencia final no parece un caso aislado:** la mediana de referencias baja de 46,5 en los vuelos 1–67 a 11 en los vuelos 68–72.
2. **Textura y continuidad son problemas diferentes:** el vuelo 53 demuestra que una escena con rasgos no basta si la cadena de imágenes o sus tiempos fallan.
3. **El vuelo 9 confirma el principio, no la escala:** JPL también depende de información visual distribuida, pero transforma una secuencia en geometría 3D; nuestro índice es un indicador previo y simplificado.
4. **Un aterrizaje puede ser posible junto a un peligro cercano:** la imagen del vuelo 33 recuerda que seguir el terreno y colocar cuatro patas de forma estable son problemas relacionados, pero distintos.
5. **El audio valida la física por otra vía:** la peineta del ensayo reproduce 2.277 rpm con gran precisión y los WAV marcianos conservan la familia de 84/168 Hz.
6. **ΔRPM no indica fallo:** la modulación del vuelo 5 es compatible con una diferencia diminuta entre rotores, del orden de 1 rpm bajo el modelo de cuatro lóbulos.
7. **Los vuelos rápidos abren una línea nueva, pero no cierran el accidente:** 62, 68 y 69 alcanzaron 10 m/s; 68 y 69 añadieron `Sys-ID`, pero los datos públicos no prueban fatiga previa a la sobrecarga del vuelo 72.
8. **La fuerza del proyecto es la convergencia:** registro, imágenes, mapa, terreno, audio, sombras y publicaciones técnicas pueden consultarse bajo una misma cronología sin confundirlos con telemetría.

---

## 17. Límites que deben acompañar cualquier publicación

- El montaje no contiene todos los fotogramas originales ni es una grabación continua.
- La asignación de bloques es provisional.
- La compresión, exposición, viñeteado, selección pública y máscara de sombra afectan las métricas.
- La puntuación visual no es una variable de vuelo de Ingenuity.
- Una imagen cenital no proporciona por sí sola escala, pendiente ni orden de contacto de las patas.
- El detector de referencias no diagnostica servos, IMU, vibraciones, rotor ni sincronización cámara–IMU.
- Una pérdida acústica puede deberse a distancia, viento o ruido; no demuestra que el rotor se detuviera.
- Los MP3 son previsualizaciones; las medidas deben volver a los WAV calibrados.
- La similitud con una explicación de NASA/JPL debe expresarse como coherencia o compatibilidad, salvo que exista una comparación cuantitativa directa.
- La velocidad sobre el suelo no mide directamente rpm, potencia, tensión de pala ni daño por fatiga.

---

## 18. Fuentes esenciales

- [NASA Science · Ingenuity Mars Helicopter](https://science.nasa.gov/mission/mars-2020-perseverance/ingenuity-mars-helicopter/)
- [NASA/JPL · investigación pública del vuelo 72, 11 de diciembre de 2024](https://www.jpl.nasa.gov/news/nasa-performs-first-aircraft-accident-investigation-on-another-world/)
- [NASA · The Right Stuff: expansión de la envolvente y vuelo 62](https://science.nasa.gov/blog/the-right-stuff/)
- [NASA/JPL/Ames · vuelos 68–69 y campaña Sys-ID](https://science.nasa.gov/blog/unlocking-the-martian-skies-using-ingenuity-as-a-martian-testbed-for-future-rotorcraft/)
- [NASA · velocidades máximas de los vuelos 62, 68 y 69](https://science.nasa.gov/resource/mars-report-the-most-extreme-flights-of-nasas-ingenuity-mars-helicopter/)
- [NASA/JPL · Ingenuity’s Hazard Avoidance Capability, PIA25662](https://www.jpl.nasa.gov/images/pia25662-ingenuitys-hazard-avoidance-capability/)
- [Schoppmann et al. · Multi-Resolution Elevation Mapping and Safe Landing Site Detection](https://arxiv.org/abs/2111.06271)
- [Proença et al. · Optimizing Terrain Mapping and Landing Site Detection](https://arxiv.org/abs/2205.03522)
- [Lorenz et al. · The sounds of a helicopter on Mars](https://doi.org/10.1016/j.pss.2023.105684)
- [NASA PDS · audio calibrado SuperCam](https://pds-geosciences.wustl.edu/m2020/urn-nasa-pds-mars2020_supercam/data_calibrated_audio/)
- [`FUENTES_Y_METODO.md`](FUENTES_Y_METODO.md)
- [`ANALISIS_HAZARD_AUDIO_JPL.md`](ANALISIS_HAZARD_AUDIO_JPL.md)
- [`analisis/comparar_audio.py`](analisis/comparar_audio.py)
- [Pedro Ramón Montserrat Cabrera · perfil de LinkedIn y serie «Anatomía de la Rotura de una Pala del Ingenuity»](https://www.linkedin.com/in/pedroramon-drones-atsep)

---

## 19. Cita recomendada

> Montserrat Cabrera, Pedro Ramón (2026). *Ingenuity: log ampliado de 72 vuelos, imágenes y audio de Marte. Leyenda, fórmulas y criterios de interpretación*. Fuerteventura, Islas Canarias, España. https://github.com/pedroramon-estudios/Ingenuity-72-vuelos

La consulta, el enlace y la cita breve con atribución están permitidos en los términos del repositorio. La publicación pública no convierte las aportaciones originales en código abierto. Consulte `LICENSE` y `NOTICE.md`.
