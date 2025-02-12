import json

class ServiceItem:
    def __init__(self, id, qtd, preco, service_id, product_id, procedure_id):
        self.id = id # atributos de instância
        self.qtd = qtd
        self.preco = preco
        self.service_id = service_id
        self.product_id = product_id
        self.procedure_id = procedure_id

    def __str__(self):
        return f"Quantidade: {self.qtd} - Preço R$: {self.preco} - Id Serviço: {self.service_id} - Id Produto: {self.product_id} - Id Procedimento: {self.procedure_id}"

class ServiceItems:
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
        with open("services_items.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        # esvazia a lista de objetos
        cls.objetos = []
        try:
            with open("services_items.json", mode="r") as arquivo:
                # abre o arquivo com a lista de dicionários -> objetos_json
                objetos_json = json.load(arquivo)
                # percorre a lista de dicionários
                for obj in objetos_json:
                    # recupera cada dicionário e cria um objeto
                    c = ServiceItem(
                        obj["id"],
                        obj["qtd"],
                        obj["preco"],
                        obj["service_id"],
                        obj["product_id"],
                        obj["procedure_id"],
                    )
                    # insere o objeto na lista
                    cls.objetos.append(c)    
        except FileNotFoundError:
            pass
    