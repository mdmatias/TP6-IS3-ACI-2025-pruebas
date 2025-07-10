# Gestión de calidad del producto software: pruebas

Ingeniería de Software III / Actualidad Informática  
Lic. en Sistemas de Información / Analista en Sistemas de Computación  
FCEQyN - UNaM

## Introducción

La mayoría de los lenguajes tienen una (o más librerías) para realizar pruebas vía código.
En este caso, se va a continuar trabajando bajo Python utilizando la librería PyTest.

Referencia: [Effective Python Testing With pytest](https://realpython.com/pytest-python-testing/)

## Tests unitarios y de integración

Los archivos de **test** tienen que estar en una carpeta con ese mismo nombre para que puedan ser identificados y ejecutados de forma automática. Además de tener en su nombre de archivo el prefijo "test_". Tanto esta carpeta como la del código a probar deberían ser módulos por lo que se agrega un archivo **__init__.py**.

Los tests en sí van a ser funciones que van a hacer la invocación a una función (para el caso de tests unitarios) o varias funciones entrelazadas (para el caso de tests de integración). En cualquier caso, se busca que se obtenga el valor correcto al ejecutar la función en sí, para ello se utiliza la instrucción **assert** que realiza esta comparación y, en caso correcto, el test _pasa_ (PASS) y en caso que la comparación no sea correcta _falla_ (FAIL).

En el ejemplo se hace uso de un decorador de funciones para parametrizar un test con varios casos de entradas de datos.

Para ejecutar los ejemplos, se tiene que ejecutar (_dentro del entorno de ejecución local_):

~~~ bash
pytest                  # Ejecuta todos los test que encuentre en la carpeta test
pytest test/archivo.py  # Ejecuta todos los tests de ese archivo en particular
~~~

## Aplicacción de BDD

El Desarrollo Guiado por Comportamiento es una extensión de TDD (_Test Driven Development_) que, en este escenario, permite escribir especificaciones en lenguaje natural y ejecutar pruebas automatizadas basadas en ellas. Para ello se utiliza un DLS (_Domain Specific Language_) como **Gherkin** que podría ser utiilzado para re-escribir los criterios de aceptación de una historia de usuario. La sintaxis es algo como esto:

~~~ gherkin
Feature: [Nombre de la funcionalidad]
  Scenario: [Escenario particular]
    Given [contexto inicial]
    When [acción]
    Then [resultado esperado]
~~~

La estructura de carpetas del proyecto tiene que ser algo como lo siguiente:

~~~ bash
features/
│
├── {funcionalidad}.feature         # Archivo Gherkin de la {funcionalidad}
├── steps/
│   └── {funcionalidad}_steps.py    # Implementación de los pasos en Python para la {funcionalidad}
~~~

En esta nueva carpeta de **steps** se tienen archivos (en este caso en Python) para implementar los tests, por ejemplo [steps.py](../features/steps/suma_steps.py) implementa la lógica en Python que conecta cada frase del [.feature](../features/suma.feature) con funciones para probarla:

~~~ python
@given('tengo los números {a} y {b}')
def step_given_tengo_los_numeros(context, a, b):
    context.a = a
    context.b = b
~~~

Es importante notar que cada paso generado tiene una función que usa un decorador indicando su relación con el tipo de paso (@given, @when, @then) y la descripción del texto esperado en la definición.
La variable **context** sirve como contenedor para compartir datos entre pasos del mismo escenario.

Para ejecutar los ejemplos, se tiene tener instalada la librería y ejecutarla (_dentro del entorno de ejecución local_):

~~~ bash
python -m pip install behave
behave                  # Ejecuta los archivos de la carpeta features
~~~ 

## Obtener un reporte de cobertura de tests de nuestro código

Para saber qué tanto código de nuestro proyecto está siendo testeado por nuestra bateria de casos de prueba existen herramientas para obtener un reporte de cobertura (coverage). En este mismo entorno, se podrá instalar la librería **coverage** que puede generar reportes tanto a la terminal como a una salida html.

Para instalar la librería (_recordar tener activado el entorno_):

~~~ bash
python -m pip install coverage
~~~ 

Para ejecutarla tenemos dos pasos a seguir, el segundo con una opción según la salida deseada:

~~~ bash
# Primer paso, ejecutar los tests
coverage run -m pytest      # Para ejecutar los tests de PyTest y obtener la cobertura
coverage run -m behave      # Para ejecutar los tests de BDD y obtener la cobertura
# Paso 2, generar los reportes
coverage report             # Salida a la terminal
coverage htmk               # Salida a una nueva carpeta de htmlcov con un index.html
~~~