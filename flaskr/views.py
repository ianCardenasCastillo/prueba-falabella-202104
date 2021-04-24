from flask import Flask, request, jsonify, Blueprint
from flask import Response

from .models import Patente
from .models import db

bp_patente = Blueprint('patente', __name__, url_prefix='/patente')

@bp_patente.route('/', methods=['GET'])
def get_patente():
    if request.method == 'GET':
        patente_request = request.args.get('patente')       # Se obtiene el parametro patente
        id_request = request.args.get('id')     # Se obtiene el parametro id
        if patente_request is not None and id_request is None:      # Si se ingreso la patente por parametro
            patente_found = Patente.query.filter_by(patente=patente_request.upper()).first()
            if patente_found:
                return jsonify(id=patente_found.id), 200        # Se devuelve la id de la patente
            else:
                return Response(status=204)     # Si no se encuentra la patente se retorna un 204 No Content
        if patente_request is None and id_request is not None:      # Si se ingreso la id por parametro
            patente_found = Patente.query.filter_by(id=id_request).first()
            if patente_found:
                return jsonify(patente=patente_found.patente), 200      # Se devuelve la patente asociada al id
            else:
                return Response(status=204)     # Si no se encuentra el id se retorna un 204 No Content
        return Response(status=400)

bp_matriz = Blueprint('matriz', __name__, url_prefix='/matriz')
@bp_matriz.route('/',methods=["GET"])
def get_sum_matriz():
    if request.method == 'GET':
        r = request.args.get('r')       # rows
        c = request.args.get('c')       # columns
        z = request.args.get('z')
        x = request.args.get('x')
        y = request.args.get('y')
        try:
            # Validaciones
            if int(z) < 1 and int(z) > 1000000:
                return jsonify(error="El parametro Z debe ser mayor a 0 y menor o igual a 1000000"), 200
            if int(r) < 1 or int(c) <1:
                return jsonify(error="Parametros R y/o C deben ser mayores a 0"), 200
            if int(x) < 0 and int(y) < 0:
                return jsonify(error="Parametros X y/o Y deben ser mayores o igual a 0"), 200
            matrizrc=[]     # Matriz para R x C
            if int(r)==1:       # Si r es 1
                matrizrc = [[int(z) for t in range(1,int(c)+1)] for g in range(1,int(r)+1)]      # Se llena la fila con Z
                print(matrizrc)
            else:       # Si r es distinto a 1
                matrizrc = [[int(z)+int(g)-1 for t in range(1,int(c)+1)] for g in range(1,int(r)+1)]     # Se llena cada fila con Z + Row_num(g) - 1
                print(matrizrc)
            matrizxy = [[int(z)+int(g) for t in range(int(x)+1)] for g in range(int(y)+1)]
            print(matrizxy)
            sumatoriaxy = 0
            for fila in matrizxy:
                for elemento in fila:
                    sumatoriaxy += elemento
            return jsonify(resultado=sumatoriaxy), 200
        except ValueError:
            return jsonify(error="Los parametros deben ser enteros"), 200
        except TypeError:
            return jsonify(error="Asegurece de ingresar los parametros r, c, z, x e y"), 200
        
