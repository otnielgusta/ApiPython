class ProfissionalModel():
    pass
    nome = ""
    sobrenome = ""
    email = ""
    codFormacao = ""
    idCidade = ""
    senha = ""
    foto = ""
  
        
        

    def fromJson(self, json):
        self.nome = json['nome']
        self.sobrenome = json['sobrenome']
        self.email = json['email']
        self.codFormacao = json['codFormacao']
        self.idCidade = json['idCidade']
        self.senha = json['senha']
        self.foto = json['foto']
