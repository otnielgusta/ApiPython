from flask import jsonify, request, Response
from flask_restx import Api, Resource


from server import server

mydb = server.mydb

class Cliente(Resource):
    def get(self):        
        cursor = mydb.cursor()
        
        query = ("select cl.idCliente, cl.nome, cl.sobrenome, cl.email, c.nome, e.nome from cliente as cl inner join cidade as c on c.idCidade = cl.idCidade inner join estado as e on e.idEstado = c.idEstado")
        try:
            cursor.execute(query)
            result = cursor.fetchall()
        except:
            return "Ocorreu um erro"
        finally:    
            cursor.close()    
            
        return jsonify(result)
    