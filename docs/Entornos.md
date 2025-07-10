# Laboratorio de gestión de configuración: entornos

Ingeniería de Software III / Actualidad Informática  
Lic. en Sistemas de Información / Analista en Sistemas de Computación  
FCEQyN - UNaM

---

## Parte 1 - Manejo de entornos

### Descripción del ejemplo

Se parte de la base de un proyecto que va a ser desarrollado con Python. El framework a utilizar será FastAPI para el backend y tendrá persistencia en una base de datos PostgreSQL.

### Pasos iniciales

Para instalar una (o más) librerías, es conveniente generar un entorno virtual. En este contexto, es un espacio donde se instalan las librerías del proyecto y no modifican la instalación general del equipo.

En Python, existen varias alternativas para esto, en este caso se va a utilizar la librería **venv** que viene integrada al lenguaje en su paquetería estándar.

Para comenzar se debe contar con una instalación de Python y Pip. El comando a ejecutar es:

~~~ bash
python -m venv .venv --prompt="nombre_proyecto"
~~~

En este comando, se estaría utilizando la librería venv para generar un entorno virtual que sería almacenado en el directorio **.venv** (_que se deberá agregar al .gitignore_) y se define (opcionalmente) el nombre para mostrar desde la terminal para cuando se esté empleando el entorno en cuestión.

A partir de ahí, se debe acceder y activar el entorno con el comando (_podrá variar de un sistema operativo a otro_):

~~~ bash
source .venv/bin/activate
~~~

### Manejo de dependencias

Con el entorno activado en la terminal / powershell se puede pasar a hacer la instalación de los paquetes necesarios:

~~~ bash
python -m pip install [librería]
~~~
Donde **[librería]** podría ser: "fastapi[standard]" (incluyendo las comillas en este caso particular).
Para poder replicar este entorno, se puede exportar el conjunto de dependencias del mismo mediante un comando:

~~~ bash
python -m pip freeze > requirements.txt
~~~

Eso va a generar un archivo .txt con todas las librerías y sus respectivas versiones instaladas en el entorno en cuestión. Ese archivo podrá ser uitlizado como fuente para replicar el entorno en otro equipo, por ejemplo:

~~~ bash
python -m venv .venv --prompt="nombre_proyecto_en_otro_equipo"
source .venv/bin/activate
python -m pip install -r requirements.txt
~~~

## Parte 2 - Dockerización de la aplicación

### Pre-requisitos

* Instalar docker. [Tutorial](https://docs.docker.com/get-docker/)

### Descripción del ejemplo

La idea es tomar como base el caso del la sección anterior y pasar a utilizar Docker para su distribución. Esto va a generar que se replique el mismo entorno con independencia de la plataforma base a utilizar.

### Generación de una imagen

Docker funciona con contenedores e imágenes. Un **contenedor** es una instancia de una imagen que se encuentra (generalmente) en ejecución; la imagen es una especie de "receta" para construir ese contenedor.

Para generar imágenes, se tienem que crear archivos de tipo **Dockerfile** que tienen toda la especificación de los pasos a seguir para la construcción de la imagen que posteriormente será utilizada. 

Por ejemplo, para este caso continuando con el uso de FastAPI:

~~~ Dockerfile

FROM python:3.13-alpine

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requerimientos al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación al contenedor
COPY . .

# Expone el puerto en el que correrá la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["fastapi", "dev", "api/app.py", "--host", "0.0.0.0", "--port", "8000"]
~~~

Qué es eso?

* `python:3.13-alpine` sirve para indicar la imagen base sobre la que se va a trabajar.
* `WORKDIR /app` indica que esa ubicación será en la que se van a ejecutar los siguientes comandos del archivo.
* `COPY requirements.txt .` hace la copia del archivo definido de la ubicación actual a la imagen. En este caso va a ser en la ubicación definida en el paso previo.
* `RUN pip3 install --no-cache-dir -r requirements.txt` es la orden para ejecutar la instalación de las dependencias del proyecto en la imagen.
* `COPY . .` hace la copia del contenido del directorio actual a la imagen.
* `EXPOSE 8000` expone el puerto en el que correrá la aplicación.
* `CMD ["fastapi", "dev", "api/app.py", "--host", "0.0.0.0", "--port", "8000"]` es el comando a ejecutarse al iniciar un contenedor con la imagen, en este caso la llamada a iniciar la API.

En este momento, después de generar el archivo, se podría generar una imagen con sus características, para eso se tiene que ejecutar el siguiente comando (**estando en la misma ubicación** del Dockerfile):

~~~ bash
docker build -t fastapi-app .
~~~

Posteriormente, se puede ejecutar el contenedor con el siguiente comando:

~~~ bash
docker run -it --rm -p 8000:8000 fastapi-app
~~~

Qué hicimos ahí?

* `docker run` sirve para ejecutar un contenedor.
* `--rm` indica que se elimina apenas lo terminamos de usar, no "queda guardado" para usarlo después.
* `-it` indica que el contenedor va a "tomar" la terminal en donde estamos ejecutando el comando y vamos a poder interactuar con él.
* `-p 8000:8000` es la indicación que en el host el puerto 8000 va a estar conectado (forwarding) con el puerto 8000 del contenedor (que tiene el EXPOSE previamente).
* `fastapi-app` es el nombre de la imagen con base en la que se va a generar el contenedor.

En qué resulta todo eso?

Tenemos el proyecto ejecutándose en una configuración idéntica en todas las estaciones de trabajo de los _devs_. Pero esto es muy básico y estático, veamos algo más elaborado.

---

### Actualizando e independizando la imagen

No tiene sentido tener que actualizar la imagen ante cada cambio. En lugar de eso, se puede cambiar la forma en la que se instancia el contenedor para generar un volumen específico donde estén los archivos actualizados. 

Para eso, se debe cambiar nuestro Dockerfile:

~~~ Dockerfile
# Usa una imagen base oficial de Python
FROM python:3.13-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requerimientos al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que correrá la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación en modo desarrollo
CMD ["fastapi", "dev", "api/app.py", "--host", "0.0.0.0", "--port", "8000"]
~~~

Notese que **no se están copiando los archivos del código de la aplicación**, solamente el de requeriminetos. Entonces, _volviendo a generar la imagen_, se debe cambiar la ejecución del contenedor a:

~~~ bash
docker run -d -p 8000:8000 -v $(pwd):/app fastapi-app
~~~

Qué hay de nuevo?

* `-v $(pwd):/app` indica que queremos montar un **volumen** en el contenedor, que es básicamente la forma de dar persistencia a los archivos. En este caso hace que se refleje el contenido de la carpeta actual (`$(pwd)` en la ubicación `/app`).

## Parte 3 - Agregando servicios

Generalmente, una aplicación o proyecto no va a tener un único servicio en ejecución, es posible que se requiera una base de datos, un gestor de cache, separar frontend de backend, un balanceador de carga, entre otros. Para esos casos, un Dockerfile solo no es suficiente y se requiere pasar a definir un conjunto de servicios que van a estar en ejecución. En estos casos, se debe pasar a usar **Docker Compose** para que cada servicio esté en su propio contenedor.

### Definición de los servicios

Por ejemplo, si fuera necesario utilizar una base de datos se va a tener que generar un archivo `docker-compose.yml` con este contenido:

~~~ yaml
services:
  api:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    volumes:
      - .:/app  # Monta el código local para desarrollo
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres

  db:
    image: postgres:15
    container_name: postgres_db
    ports:
      - "5432:5432"
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
~~~

Qué tiene este archivo?
1. **Servicio api**:
   - Construye la imagen usando el Dockerfile en el directorio actual.
   - Expone el puerto `8000` para acceder a la API.
   - Genera un volumen para copiar el código local a la ubicación del contenedor definida previamente (`.:/app`).
   - Define una variable de entorno `DATABASE_URL` para que la API se conecte al contenedor/servicio de PostgreSQL.
2. **Servicio `db`**:
   - Se define que se va a usar la imagen oficial de PostgreSQL (`postgres:15`).
   - Especifica las variables de entorno `POSTGRES_USER`, `POSTGRES_PASSWORD` y `POSTGRES_DB` para las credenciales que requiere el servicio.
   - Expone el puerto `5432` para acceder que se pueda usar el mismo puerto del host para acceder a la base de datos.
   - Genera un volumen persistente (`postgres_data`) para almacenar los datos de la base de datos aun cuando los contenedores se apaguen.
3. **Volumen `postgres_data`**:
   - Asegura que los datos de la base de datos se mantengan incluso si el contenedor se elimina.

El paso siguiente va a ser construir e instanciar los contenedores:

~~~ bash
docker compose up --build
~~~

### Ajustes de seguridad

Como entre los integrantes del equipo este archivo **docker-compose.yml** sería compartido a través del repositorio de código que tengan asociado al proyecto, __no sería una buena práctica__ de seguridad dejar en texto plano las credenciales de acceso al motor (inclusive si se usa solo de forma local).

Para subsanar este tema, se podría usar un archivo `.env` con la definición de las variables de entorno, por ejemplo:

~~~ yml
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
~~~

En ese archivo, se pueden definir las credenciales a utilizar y se lo agrega a .gitignore para no compartirlo. Con esos cambios, el archivo de definición de servicios quedaría de la siguiente manera:

~~~ yaml
services:
  api:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    volumes:
      - .:/app  # Monta el código local para desarrollo
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}
    env_file:
      - .env

  db:
    image: postgres:15
    container_name: postgres_db
    ports:
      - "5432:5432"
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    env_file:
      - .env

volumes:
  postgres_data:
~~~

Esto sería un **esquema inicial** para trabajar la gestión de entornos en un proyecto de software.

---

## Fuentes

* [FreeCodeCamp - Tutorial inicial de docker para devs](https://www.freecodecamp.org/news/docker-101-fundamentals-and-practice-edb047b71a51/)