Link del conjunto de datos utilizado en el proyecto:
https://drive.google.com/file/d/1E1FCwOLL6I88InuuQQqcxsLIhsQXdkWg/view?usp=sharing

Link del video:
https://www.canva.com/design/DAFGKOT44nk/G3tJTfMTsxuNX8uYsp6Rgg/watch?utm_content=DAFGKOT44nk&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink

# CONTENEDORES INTERACTIVOS PARA RECICLAJE CON VISION ARTIFICIAL
Proyecto final del BOOTCAMP de visión artificial orientado a los ODS 11 (Ciudades y comunidades sostenibles), ODS 12 (Producción y consumo responsables) y ODS 17 (Alianzas para lograr los objetivos).

El proyecto tiene la finalidad de mejorar e incentivar los habitos de reciclaje y conciencia ambiental en los ciudadanos.

El funcionamiento comienza cuando el usuario coloca un residuo en el área de detección, el cual por medio de una camara toma una imagen del residuo y mediante Deep Learning realiza la clasificación a uno de los 3 contenedores (Plastico, Papel-Cartón, General). El sistema le avisa al ciudadano en que contenedor debe depositar el residuo.    
 
Componente Hardware: base o área donde se coloca el residuo para su clasificación, conformada por (Raspberry, PICAM, Iluminación Led, Estructura de madera)

Componente Software: Pagina WEB donde se muestra el resultado de clasificación y procesamiento de imagenes.

# Motivación
En ciudades de paises en vias de desarrollo como La Paz y El Alto todavia existe una deficiente clasificación de los residuos, por los ciudadanos, a pesar de las iniciativas ambientales de reciclaje (como las islas verdes), por lo que en las esquinas de las calles se observa gran acumulación de residuos que pueden ser aprovechables y reutilizables.

Con la gran variedad de materiales, el ciudadano que tiene el habito de reciclar tambien puede confundirse en como realizar un correcta clasificación de su residuo, por lo que tambien se convierte en una problematica a resolver.

# Capturas de pantalla
Se incluye una captura de pantalla de la interface del proyecto, el cual se encarga de tomar fotos y crear el DATASET:

![alt text](https://github.com/cesarmax232/BOOTCAMP/blob/main/Imagen5.png?raw=true)

Se incluye una captura de pantalla de la interface de visualización del proyecto, el cual se encarga de mostrar el resultado de clasificación y las imagenes en tiempo real:

![alt text](https://github.com/cesarmax232/BOOTCAMP/blob/main/Imagen4.png?raw=true)

# Tecnologías/Frameworks utilizados
- Raspberry PI 3B
- PI OS BULLSEYE
- TensorFlow Lite
- Java Script
- Python3
- Broker Mosquitto
- OpenCV
- Numpy

# Funcionalidades mas importantes
las funcionalidades mas interesantes de tu proyecto son:
 - Permite clasificar residuos de tipo plastico, papel y carton. Si el objeto o residuo no pertenece a ninguno de los anteriores entonces se lo clasifica a un contenedor general.
 - Posee clasificación automatica con detección de movimiento mediante tecnicas clasicas de vision artificial.
 - La inferencia se realiza en la misma placa Raspberry donde se ejecuta todo el codigo incluido la interfaz WEB.
 - Se aplica tecnicas vistas en el BOOTCAMP para mejorar las imagenes tomadas por la camara y que la iluminación del ambiente no afecte demasiado a la clasificación.
 - La interfaz WEB muestra la imagen en tiempo real de la camara sin procesar, otra imagen en tiempo real del resultado del algoritmo de detección de movimiento y otra imagen que muestra la imagen procesada y mejorada la cual es usada para la clasificación. En la misma interfaz se muestran circulos luminosos los cuales indican a cual contenedor se debe depositar el residuo. 

# Hiperparametros

train_data -> batch_size=54

validation_data -> batch_size=9

test_data -> batch_size=9

loss -> categorical_crossentropy

optimizer -> adam

epochs -> 10

steps_per_epoch -> 6

validation_steps -> 6

# Metricas y Resultados

El resultado del entrenamiento se muestra en la siguiente imagen, en donde se observa como converge la perdida y la presicion va en aumento con cada epoca. Se tiene en mismo resultado tanto para los datos de entrenamiento y validación:

![alt text](https://github.com/cesarmax232/BOOTCAMP/blob/main/Imagen1.png?raw=true)

La matriz de confusion en la siguiente imagen señala que 14 instancias no fueron clasificadas correctamente en los datos de prueba o test:

![alt text](https://github.com/cesarmax232/BOOTCAMP/blob/main/Imagen2.png?raw=true)

Se muestra tambien las metricas F1-SCORE y RECALL en la siguiente imagen:

![alt text](https://github.com/cesarmax232/BOOTCAMP/blob/main/Imagen3.png?raw=true)

Por ultimo se calcula la metrica LOG-LOSS SCORE: 0.12, y la presicion del modelo alcanza: 95.3%

# Trabajos Relacionados
Entre los trabajos más relacionados con el objetivo del proyecto podemos comentar los siguientes:
- Desarrollo de un contenedor y clasificador automático de material reciclable como estrategia de economía circular en el contexto educativo
Universidad de la amazonia
Edna Yahile Salinas Osuna, Jhonier David Anacona Ortiz, Oscar Fabián Patino Perdoho, Edwin Eduardo Hillán Rojas
Página web: https://www.redalyc.org/journal/852/85269429009/html/ 
Objetivo. Caracterizar los residuos mediante el desarrollo de un contenedor con un clasificador de plásticos empleando una red neuronal 

- Contenedores de reciclaje interactivos con IoT 
Universidad autónoma de Occidente
Daniel Delgado Rodriguez, Juan Fernando Guerrero Figueroa
Objetivo. Identificación de residuos a través de una red convolucional en ordenador de placa reducida 

- Diseño e Implementación de un Sistema Autónomo de Detección y Clasificación de Residuos 
Universidad de La Laguna
Alberto Méndez García, Stefano Fernando Panzeri Reyes
Objetivo. Identificación de residuos a través de una red neuronal para luego ser empujado al cubo correspondiente del residuo

# Métodos
En la siguiente imagen se muestran las etapas y el enfoque utilizado para resolver la problematica:

- La primera etapa es crear el dataset y para esto se desarrolla una interfaz para capturar y guardar las imagenes.
- Con el dataset creado se pasa a la etapa de entrenamiento, esto se realiza en COLAB con GPU.
- Reentrenando el modelo hasta conseguir resultados aceptables, se pasa a exportar el modelo al formato TFLITE.
- El modelo TFLITE y el codigo de despliegue se implementan en la Raspberry.
- Se pasa a la etapa de funcionamiento donde se implementa el algoritmo de detección de movimiento y procesamiento para mejorar y acondicionar la imagen de la camara de la Raspberry.
- La ultima etapa conlleva el desarrollo de una interfaz WEB para visualizar los resultados de clasificación.   

![alt text](https://github.com/cesarmax232/BOOTCAMP/blob/main/Imagen6.PNG?raw=true)

# Resultados Experimentales
En la etapa de clasificación se realizó pruebas con diferentes plasticos, papeles y cartones de forma satisfactoria con las metricas descritas anteriormente. Estas pruebas se realizan en tiempo real y en condiciones reales con diferente iluminación ambiente.

Al momento de realizar la clasificación notamos que se tiene inconvenientes en ciertos residuos. ejemplo: objetos metalicos cubiertos con papel o papeles forrados con plastico. Esto se podria solucionar adicionanado sensores electronicos para detectar el material del residuo.

La detección de movimiento funciona correctamente siempre y cuando la luz ambiente o ruido exterior no provoquen falsos positivos. Para mitigar los efectos del ruido o cambios de luminosidad se decidió instalar iluminación LED propia dentro el área de detección.

El modelo utilizado es Mobilenet ya que no tiene inconvenientes al momento de exportar al formato TFLITE como sucedió con el modelo EFFICIENTNET

# Creditos
- Cesar Huanca
- Freddy Barrios
- Alex Toro
- Miguel Guevara

# Licencia
The MIT License

Copyright (c) 2020 CAAF-VISION

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
