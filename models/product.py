import json
class Product:
    def __init__(self, id, name, description, price, stock):
        self.id = id # atributos de instância
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
    def __str__(self):
        return f"{self.id} - {self.name} - {self.description} - {self.stock} - R${self.price:.2f}"

class Products:
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
        return cls.objetos[:]
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        # percorre a lista procurando o id    
        for x in cls.objetos:
            if x.id == id: 
                return x
        return None
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()        
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.salvar()
    @classmethod
    def detalhes(cls, id):
        x = cls.listar_id(id)
        if x != None:
            return f"Id: {x.id} - Name: {x.name} - Description: {x.description} - Price: R${x.price:.2f} - Stock: {x.stock}"
    @classmethod
    def salvar(cls):
        # open - cria e abre o arquivo clientes.json
        # vars - converte um objeto em um dicionário
        # dump - pega a lista de objetos e salva no arquivo
        with open("/vethelp/db/products.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        # esvazia a lista de objetos
        cls.objetos = []
        try:
            with open("/vethelp/db/products.json", mode="r") as arquivo:
                # abre o arquivo com a lista de dicionários -> clientes_json
                objetos_json = json.load(arquivo)
                # percorre a lista de dicionários
                for obj in objetos_json:
                    # recupera cada dicionário e cria um objeto
                    c = Product(obj["id"], obj["name"], obj["description"], obj["price"], obj["stock"])
                    # insere o objeto na lista
                    cls.objetos.append(c)    
        except FileNotFoundError:
            pass
    


