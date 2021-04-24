import os

from flask import Flask

app = Flask(__name__, instance_relative_config=True)

app.config ['SQLALCHEMY_DATABASE_URI'] = \
'sqlite:///'+app.instance_path+'/falabella.sqlite3'

app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from .helpers import populate
from . import models, views


app.register_blueprint(views.bp_patente)        # Rutas de patentes
app.register_blueprint(views.bp_matriz)     # Rutas de matriz
populate()      # Se pobla la base de datos

@app.route('/hello')
def hello():
    return 'Hola Falabella!'







