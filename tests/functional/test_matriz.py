from flaskr import app
import json
import pytest


def test_get_sum_matriz_18_200():
    """
    Se debe obtener una sumatoria de 18 al ingresar
    por parametros r, c, z, x, y:
    R = 4
    C = 3
    Z = 2
    X = 1
    Y = 2
    """
    with app.test_client() as test_client:
        response = test_client.get('/matriz/?r=4&c=3&z=2&x=1&y=2')
        assert response.status_code == 200
        assert json.loads(response.data) == {'resultado':18}

def test_get_sum_matriz_entero_200():
    """
    Se debe obtener un error de entero ingresar
    por parametros r, c, z, x, y:
    R = 4.1
    C = 3
    Z = 2
    X = 1
    Y = 2
    """
    with app.test_client() as test_client:
        response = test_client.get('/matriz/?r=4.1&c=3&z=2&x=1&y=2')
        assert response.status_code == 200
        assert json.loads(response.data) == {'error':'Los parametros deben ser enteros'}

def test_get_sum_matriz_missing_200():
    """
    Se debe obtener un error de parametro que falta ingresar
    por parametros c, z, x, y:
    C = 3
    Z = 2
    X = 1
    Y = 2
    """
    with app.test_client() as test_client:
        response = test_client.get('/matriz/?c=3&z=2&x=1&y=2')
        assert response.status_code == 200
        assert json.loads(response.data) == {'error':'Asegurece de ingresar los parametros r, c, z, x e y'}