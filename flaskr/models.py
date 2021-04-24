from flask_sqlalchemy import SQLAlchemy

from flaskr import app

db = SQLAlchemy(app)

class Patente(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    patente = db.Column(db.String(80), unique=True, nullable=False)
    def __repr__(self):
        return '<Patente %r>' % self.patente
    @property
    def serialize(self):        # Propiedad que entrega el modelo como un Json
        """Return object data in easily serializable format"""
        return {
            'id'     : self.id,
            'patente': self.patente
        }

db.drop_all()       # Se alimina toda la base de datos para un trabajo limpio
db.create_all()     # Se crea la base de datos con la tabla patente