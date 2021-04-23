from flask_sqlalchemy import SQLAlchemy

from flaskr import app

db = SQLAlchemy(app)

class Patente(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    patente = db.Column(db.String(80),unique=True, nullable=False)
    def __repr__(self):
        return '<Patente %r>' % self.patente
    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id'     : self.id,
           'patente': self.patente
       }

db.drop_all()
db.create_all()

# patente = Patente(patente='AAAA0000')
# db.session.add(patente)
# db.session.commit()