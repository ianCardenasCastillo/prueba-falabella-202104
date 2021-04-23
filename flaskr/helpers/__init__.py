from flaskr.models import db
from flaskr.models import Patente
import string


def populate():
    numbers = [*range(0, 1000, 1)]
    alphabet = list(string.ascii_lowercase)     # Obtiene todo el alfabeto exceptuando la letra ñ
    patentes = []
    for i in alphabet:      # Recorro el alfabeto
        if i != 'ñ':        # Si existe la ñ se salta
            for e in numbers:       # Por cada letra se itera 999 veses desde el 0 hasta el 999
                first_part = str(i)*4       # Se repite la letra 4 veces para el formato AAAA o BBBB
                second_part = e     # Se define la parte numerica
                if len(str(e))==2:      # Si el numero tiene un largo de 2 digitos
                    second_part = '0'+str(e)        # anteponemos un 0
                if len(str(e))==1:# Si el numero tiene un largo de 1 digitos
                    second_part = '00'+str(e)       # anteponemos 2 ceros
                pat = str(first_part)+str(second_part)      # se concatena
                patente = Patente(patente=pat.upper())      # se crea el objeto patente
                patentes.append(patente) 
    db.session.bulk_save_objects(patentes)      # Se realiza un bulk de objetos
    db.session.commit()     # Se confirman los cambios
