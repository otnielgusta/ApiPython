from flask import jsonify, request, Response
from flask_restx import Api, Resource

from models.profissional_model import ProfissionalModel

from server import server

mydb = server.mydb

class Profissional(Resource):
    def get(self):        
        cursor = mydb.cursor()
        
        query = ("select cl.idProfissional, cl.nome, cl.sobrenome, cl.email, c.nome, e.nome from profissional as cl inner join cidade as c on c.idCidade = cl.idCidade inner join estado as e on e.idEstado = c.idEstado")
        try:
            cursor.execute(query)
            result = cursor.fetchall()
        except:
            return "Ocorreu um erro"
        finally:    
            cursor.close()    
            
        return jsonify(result)
    
    def post(self):
        cursor = mydb.cursor()
        profissional = ProfissionalModel()
        profissional.fromJson(request.json)
        print(profissional)

        try:
            query = ("insert into profissional(nome, sobrenome, email, codFormacao, idCidade, senha, foto) values(%s,%s,%s,%s,%s,%s,%s)")
            parametros = (profissional.nome, profissional.sobrenome, profissional.email, profissional.codFormacao, profissional.idCidade, profissional.senha, profissional.foto)
            cursor.execute(query, parametros)
            return Response("{'status_code':200}", status=200, mimetype='application/json')
        except:
            return False
        finally:
            cursor.close()

cliente = Profissional()
      
