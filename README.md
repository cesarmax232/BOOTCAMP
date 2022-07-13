Link del conjunto de datos utilizado en el proyecto:
https://drive.google.com/file/d/1E1FCwOLL6I88InuuQQqcxsLIhsQXdkWg/view?usp=sharing

# Titulo del Proyecto
Una pequeña descripción sobre su proyecto. Responder lo siguiente: ¿Qué hace el proyecto? ¿De que se trata? ¿Qué componentes tiene?

(Agregar esta sección en el caso de que el proyecto este compuesto por varios repositorios)

# BOOTCAMP
Proyecto final del BOOTCAMP de visión artificial orientado a los ODS

# Motivación
Una breve descripción de la motivación detrás del proyecto. Responder lo siguiente: ¿por qué existe el proyecto? ¿Qué problema soluciona el proyecto?

# Capturas de pantalla
Incluir logos o capturas de pantalla de las interfaces mas relevantes del proyecto.

# Tecnologías/Frameworks utilizados
Ejemplo) - ESP32

Arduino
Amazon IoT
Atom

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
