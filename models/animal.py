import json
from models.user import User, Users
class Animal:
    def __init__(self, user_id, id, name, race, gender):

        self.user_id = user_id
        self.id = user_id
        self.name = name
        self.race = race
        self.gender = gender

    def __str__(self):
        return f"{self.id}"

class Animals:
    objetos = [] # atributo de classe
    @classmethod
    def inserir(cls, obj):
        # abre a lista do arquivo
        cls.abrir()
        id = 0
        for x in cls.objetos:
            if x.id > id: id = x.id
        obj.id = id + 1 
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
        # open - cria e abre o arquivo animals.json
        # vars - converte um objeto em um dicionário
        # dump - pega a lista de objetos e salva no arquivo
        with open("animals.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        # esvazia a lista de objetos
        cls.objetos = []
        try:
            with open("animals.json", mode="r") as arquivo:
                # abre o arquivo com a lista de dicionários -> animals_json
                animals_json = json.load(arquivo)
                # percorre a lista de dicionários
                for obj in animals_json:
                    # recupera cada dicionário e cria um objeto
                    c = Animal(obj["user_id"], obj["id"], obj["name"], obj["race"], obj["gender"])
                    # insere o objeto na lista
                    cls.objetos.append(c)    
        except FileNotFoundError:
            pass