import json
from models.user import User, Users
class Recepcionist:
    def __init__(self, user_id, id, cpf):
        self.user_id = user_id
        self.id = user_id
        self.cpf = cpf


    def __str__(self):
        return f"{self.id}"

class Recepcionists:
    objetos = [] # atributo de classe
    @classmethod
    def inserir(cls, obj):
        # abre a lista do arquivo
        cls.abrir()
        #aqui eu de alguma forma devo receber o user cirado e pegar o id dele para igualar com o id de recepcionist.obj
        # insere o objeto na lista
        cls.objetos.append(obj)
        # salva a lista no arquivo
        cls.salvar()
    @classmethod
    def listar(cls):
        # abre a lista do arquivo
        cls.abrir()
        # retorna a lista para a UI
        return cls.objetos
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        # percorre a lista procurando o id    
        for x in cls.objetos:
            if x.id == id: return x
        return None
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            #x.nome = obj.nome
            #x.email = obj.email
            #x.fone = obj.fone
            cls.salvar()        
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.salvar()
    @classmethod
    def salvar(cls):
        # open - cria e abre o arquivo recepcionists.json
        # vars - converte um objeto em um dicionário
        # dump - pega a lista de objetos e salva no arquivo
        with open("recepcionists.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        # esvazia a lista de objetos
        cls.objetos = []
        try:
            with open("recepcionists.json", mode="r") as arquivo:
                # abre o arquivo com a lista de dicionários -> recepcionists_json
                recepcionists_json = json.load(arquivo)
                # percorre a lista de dicionários
                for obj in recepcionists_json:
                    # recupera cada dicionário e cria um objeto
                    c = Recepcionist(obj["user_id"], obj["id"], obj["cpf"])
                    # insere o objeto na lista
                    cls.objetos.append(c)    
        except FileNotFoundError:
            pass