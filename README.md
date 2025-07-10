# IS3 - Proyecto de gestión de eventos (2025)

Este proyecto tiene por objetivo servir como base para el desarrollo de las prácticas de la asignatura a lo largo del cursado. Es el espacio desde donde la cátedra va a ir colocando el material de referencia que se utiliza en los demos o similares y que podrá ser utilizado por los estudiantes para el desarrollo de los diferentes TPs.

A medida que se avance en cada tema, se va a ir incorporando una descripción y un detalle de los elementos más relevantes en este espacio:

## Gestión de incidencias

Se generó un proyecto en la misma plataforma GitHub donde se pasaron las historias de usuario del TP2. Ese proyecto se fue generando y trabajando en clase para representar la instancia de inicio del proyecto de desarrollo con una eespecie de Sprint 0 y la ejecución de las acciones de: estimación, priorización, planificación de alto nivel, definición de una iteración y trabajo sobre los items generados.

El proyecto se puede observar en [este enlace](https://github.com/users/tinxo/projects/13).

## Gestión de entornos

En este caso, se empezó por el desarrollo del paso a paso que se podría seguir para la gestión de entornos de ejecución de un proyecto, el documento de referencia se encuentra en la carpeta [docs](docs/Entornos.md). Considerando un proyecto que va a utilizar FastAPI en su backend con una base de datos PostgreSQL. La progresión fue la siguiente:
1. Gestionar dependencias de librerías con el módulo venv de Python.
2. Generar un [Dockerfile](Dockerfile) para una imagen de Docker a utilizar para el proyecto (principalmente backend en esta instancia).
3. Generar un archivo yml [docker-compose](docker-compose.yml) para definir los servicios del backend (la API) y de persistencia (base de datos PostgreSQL y PgAdmin para visualización).

## Gestión de calidad

En este tema se tratan dos aspectos: [pruebas](docs/Pruebas.md) y [observabilidad](docs/Observabilidad.md) del producto. Se han generado documentos guía al respecto.

### Pruebas

Para el abordaje del tema de testing se mantiene el mismo escenario, pero se incluyen algunos ejemplos básicos para contextualizar en la carpera **examples**:
- [Calculos.py](examples/calculos.py): una función simple de suma con algunas validaciones.
- [Liquidaciones.py](examples/liquidacion.py): un conjunto de funciones para liquidar el sueldo de un empleado promedio.

Los tests propiamente dichos, se han generado en la carpeta **test** los archivos que ejecutan las pruebas y en una carpeta denominada **features** lo necesario para la implementación de BDD.

### Observabilidad

