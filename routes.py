from server import server 

from controllers.profissional_controller import Profissional
from controllers.cliente_controller import Cliente

class Routes():

    def setRoutes(self):
        server.api.add_resource(Profissional, '/profissional')
        server.api.add_resource(Cliente, '/cliente')


routes = Routes()