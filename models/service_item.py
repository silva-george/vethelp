import json

class ServiceItem:
    def __init__(self, id, service_id, products, procedures, total):
        self.id = service_id # atributos de instância
        self.service_id = service_id
        self.products = procedures
        self.procedures = products
        self.total = total

    def __str__(self):
        return f"ID: {self.id} - Service ID: {self.service_id} - Total: R${self.total:.2f}"

class ServiceItems:
    objetos = [] # atributo de classe
    @classmethod
    def inserir(cls, obj):
        # abre a lista do arquivo
        cls.abrir()
        # calcula o id do objeto
        # obj.id = obj.service_id  
        # insere o objeto na lista
        cls.objetos.append(obj)
        # salva a lista no arquivo
        cls.salvar()
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
            if x.id == id: return x
        return None
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()
    
    @classmethod
    def atualizar_total(cls, procedure, valor):
        x = cls.listar_id(procedure.id)
        if x != None:
            x.total = x.total + valor
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.salvar()
    @classmethod
    def salvar(cls):
        # open - cria e abre o arquivo services_items.json
        # vars - converte um objeto em um dicionário
        # dump - pega a lista de objetos e salva no arquivo
        with open("/vethelp/db/services_items.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        # esvazia a lista de objetos
        cls.objetos = []
        try:
            with open("/vethelp/db/services_items.json", mode="r") as arquivo:
                # abre o arquivo com a lista de dicionários -> objetos_json
                objetos_json = json.load(arquivo)
                # percorre a lista de dicionários
                for obj in objetos_json:
                    # recupera cada dicionário e cria um objeto
                    c = ServiceItem(
                        obj["id"],
                        obj["service_id"],
                        obj["products"],
                        obj["procedures"],
                        obj["total"],
                    )
                    # insere o objeto na lista
                    cls.objetos.append(c)    
        except FileNotFoundError:
            pass
    