from flaskr import app
import json
import pytest

def test_hola_falabella():
    """
    Se debe obtener un Hola Falabella! al acceder a
    /hello
    """
    with app.test_client() as test_client:
        response = test_client.get('/hello')
        assert response.status_code == 200
        assert b"Hola Falabella!" in response.data

def test_get_patente_by_id_200():
    """
    Se debe obtener un status 200 y la patente AAAA000
    vinculada al id 1 en la base de datos,
    se utiliza la url /patente con el parametro id
    en 1 
    """
    with app.test_client() as test_client:
        response = test_client.get('/patente/?id=1')
        assert response.status_code == 200
        assert json.loads(response.data) == {'patente':"AAAA000"}

def test_get_patente_by_id_204():
    """
    Se debe obtener un status 204 NO CONTENT
    al buscar la patente por el id 28888,.
    se utiliza la url /patente con el parametro id
    en 28888 
    """
    with app.test_client() as test_client:
        response = test_client.get('/patente/?id=28888')
        assert response.status_code == 204

def test_get_id_by_patente_lower_200():
    """
    Se debe obtener un status 200 y el id 26000
    vinculada al a la patente zzzz999 en la base de datos,
    se utiliza la url /patente con el parametro patente
    en zzzz999 
    """
    with app.test_client() as test_client:
        response = test_client.get('/patente/?patente=zzzz999')
        assert response.status_code == 200
        assert json.loads(response.data) == {'id':26000}

def test_get_id_by_patente_upper_200():
    """
    Se debe obtener un status 200 y el id 26000
    vinculada al a la patente ZZZZ999 en la base de datos,
    se utiliza la url /patente con el parametro patente
    en ZZZZ999 
    """
    with app.test_client() as test_client:
        response = test_client.get('/patente/?patente=ZZZZ999')
        assert response.status_code == 200
        assert json.loads(response.data) == {'id':26000}

def test_get_id_by_patente_lower_204():
    """
    Se debe obtener un status 204
    se utiliza la url /patente con el parametro patente
    en abcd999 
    """
    with app.test_client() as test_client:
        response = test_client.get('/patente/?patente=abcd999')
        assert response.status_code == 204

def test_get_id_by_patente_upper_204():
    """
    Se debe obtener un status 204
    se utiliza la url /patente con el parametro patente
    en ABCD999 
    """
    with app.test_client() as test_client:
        response = test_client.get('/patente/?patente=ABCD999')
        assert response.status_code == 204




