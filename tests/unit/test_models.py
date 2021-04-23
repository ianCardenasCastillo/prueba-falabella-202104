from flaskr.models import Patente
from flaskr import app

def test_new_patente():
    patente = Patente(patente="GFC000")
    assert patente.patente == 'GFC000'

def test_patente_serialize():
    patente = Patente(patente="GFC000")
    assert patente.serialize == {'id': None, 'patente': 'GFC000'}

