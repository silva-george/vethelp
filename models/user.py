import json
class User:
    def __init__(self, id, nome, email, fone, senha, user_type = None):
        self.id = id # atributos de instância
        self.nome = nome
        self.email = email
        self.fone = fone
        self.senha = senha
        self.user_type = user_type
    def __str__(self):
        return f" ID: {self.id} - Nome: {self.nome} - Email {self.email} - Fone {self.fone} - Cargo {self.user_type}"

class Users:
    objetos = [] # atributo de classe
    @classmethod
    def inserir(cls, obj):
        # abre a lista do arquivo
        cls.abrir()
        # calcula o id do objeto
        id = 0
        for x in cls.objetos:
            if x.id > id: id = x.id
        obj.id = id + 1    
        # insere o objeto na lista
        cls.objetos.append(obj)
        # salva a lista no arquivo
        cls.salvar()
        return obj
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
        with open("/vethelp/db/users.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        # esvazia a lista de objetos
        cls.objetos = []
        try:
            with open("/vethelp/db/users.json", mode="r") as arquivo:
                # abre o arquivo com a lista de dicionários -> users_json
                users_json = json.load(arquivo)
                # percorre a lista de dicionários
                for obj in users_json:
                    # recupera cada dicionário e cria um objeto
                    c = User(
                        obj["id"],
                        obj["nome"],
                        obj["email"],
                        obj["fone"],
                        obj["senha"],
                        obj["user_type"],
                    )
                    # insere o objeto na lista
                    cls.objetos.append(c)    
        except FileNotFoundError:
            pass
    


