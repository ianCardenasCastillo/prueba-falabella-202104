[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

[![Generic badge](https://img.shields.io/badge/coverage-96%25-green)](https://shields.io/)


# Prueba Tecnica Falabella
Prueba tecnica de Falabella realizada con Python Flask y una base de datos SQLite

## Endpoints

### Saludo a Falabella /hello
Saludando a Falabella
GET: /hello
```
Hola Falabella!
```

### Patentes /patente

Obtener Patente by Id 
GET: /patente/?id=1
```
{
    "patente": "AAAA000"
}
```

Obtener Id by Patente
GET: /patente/?patente=AAAA000
```
{
    "id": 1
}
```

_Patentes desde el AAAA000 hasta el ZZZZ999, en esta colección se omite las patentes con dominios ÑÑÑÑ_
_Un total de 26000 patentes_

### Matriz XY /matriz

Obtener sumatoria Matriz X Y
GET: /matriz/?r=4&c=3&z=2&x=1&y=2
```
{
    "resultado": 18
}
```


## Comenzando
Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

### Pre-Requisitos 📋
A continuación se detallaran lo que se requiere para ejecutar el servicio de patentes

### Ejecución Local Windows

Para ejecutar la aplicación en forma local se debe instalar [Python 3.9.4](https://www.python.org/downloads/)

Posteriormente ejecutar 'pip3 install -r requirements.txt' para instalar todas las dependencias del proyecto
```
pip3 install -r requirements.txt
```

Finalmente ejecutar 'flask run' para levantar el servicio, debe aparecer el siguiente mensaje
```
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Ahora ingresando a http://127.0.0.1:5000/hello accedera al mensaje de bienvenida

### Ejecución Docker

Para ejecutar la aplicación mediante docker debe instalar [Docker](https://docs.docker.com/docker-for-windows/install/) 

Posteriormente en la carpeta donde esta ubicado el archivo docker-compose.yaml ejecutar 'docker-compose build' para construir la imagen
```
docker-compose build
```
_Si es primera ves que descarga la imagen de python puede que se demore unos minutos dependiendo de las caracteristicas del equipo._

Luego de construir la imagen ejecute 'docker-compose up' para ejecutar un contenedor con la imagen creada con anterioridad, debe aparecer el siguiente mensaje

```
Recreating app ... done
Attaching to app
app    |  * Environment: production
app    |    WARNING: This is a development server. Do not use it in a production deployment.
app    |    Use a production WSGI server instead.
app    |  * Debug mode: off
app    |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```
Ahora ingresando a http://127.0.0.1:5000/hello accedera al mensaje de bienvenida

_Si ejecuta el servicio con docker no es necesario instalar python en su equipo local_

### Ejecución de pruebas

Para ejecutar las pruebas en forma local se debe instalar [Python 3.9.4](https://www.python.org/downloads/)

Posteriormente ejecutar 'pytest' para instalar todas las dependencias del proyecto
```
pytest
```
Debera obtener el siguiente output
```
========================= test session starts =========================
platform win32 -- Python 3.9.4, pytest-6.2.3, py-1.10.0, pluggy-0.13.1
rootdir: E:\Personal-Ian\prueba
collected 12 items

tests\functional\test_matriz.py ...            [ 25%]
tests\functional\test_patente.py .......       [ 83%]
tests\unit\test_models.py ..                   [100%] 

========================= 12 passed in 1.31s ==========================
```

### Ejecución coverage
Para ejecutar las pruebas en forma local se debe instalar [Python 3.9.4](https://www.python.org/downloads/)

Posteriormente ejecutar 'coverage run -m pytest' para instalar todas las dependencias del proyecto
```
coverage run -m pytest
```
Luego ejecutar 'coverage report'
```
coverage report
```

Debera obtener el siguiente output
```
Name                               Stmts   Miss  Cover
------------------------------------------------------
flaskr\__init__.py                    17      0   100%
flaskr\helpers\__init__.py            21      0   100%
flaskr\models.py                      13      1    92%
flaskr\views.py                       54      5    91%
tests\__init__.py                      0      0   100%
tests\functional\__init__.py           0      0   100%
tests\functional\test_matriz.py       18      0   100%
tests\functional\test_patente.py      35      0   100%
tests\unit\__init__.py                 0      0   100%
tests\unit\test_models.py              8      0   100%
------------------------------------------------------
TOTAL                                166      6    96%
```

## Construido con 🛠️

* [Visual Studio Code](https://code.visualstudio.com/download) - Editor de Texto
* [Python 3.9.4](https://www.python.org/downloads/) - Interpretador
* [Docker](https://docs.docker.com/docker-for-windows/install/) - Orquestador de contenedores

## Autores ✒️

* **Ian Cárdenas Castillo** - *Desarrollo y Documentación* - [Ian Cárdenas C](https://github.com/ianCardenasCastillo)

---
⌨️ con ❤️ por [Ian Cárdenas C](https://github.com/ianCardenasCastillo) 😊