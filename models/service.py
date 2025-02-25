import json

class Service:
    def __init__(self, id, receptionist_id, vet_id, client_id, animal_id, description, date, status):
        self.id = id # atributos de instância
        self.receptionist_id = receptionist_id
        self.vet_id = vet_id
        self.client_id = client_id
        self.animal_id = animal_id
        self.description = description
        self.date = date
        self.status = status

    def __str__(self):
        return f"Id: {self.id} - Recepcionist id: {self.receptionist_id} - Vet id: {self.vet_id} - Client ID: {self.client_id} - Animal id: {self.animal_id} - Description: {self.description} - Date: {self.date} - Status: {self.status}"


class Services:
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
        return cls.objetos
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        # percorre a lista procurando o id    
        for x in cls.objetos:
            if x.id == id: 
                return x
        return None
    @classmethod
    def listar_services_animal_id(cls, id):
        cls.abrir()
        services = []
        # percorre a lista procurando o id    
        for x in cls.objetos:
            if x.animal_id == id: 
                services.append(x)
            return services
        return None
    @classmethod
    def listar_services_vet_id(cls, id):
        cls.abrir()
        services = []
        # percorre a lista procurando o id    
        for x in cls.objetos:
            if x.vet_id == id: 
                services.append(x)
            return services
        return None
    @classmethod
    def listar_services_client_id(cls, id):
        cls.abrir()
        services = []
        # percorre a lista procurando o id    
        for x in cls.objetos:
            if x.client_id == id: 
                services.append(x)
            return services
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
        # open - cria e abre o arquivo services.json
        # vars - converte um objeto em um dicionário
        # dump - pega a lista de objetos e salva no arquivo
        with open("/vethelp/db/services.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        # esvazia a lista de objetos
        cls.objetos = []
        try:
            with open("/vethelp/db/services.json", mode="r") as arquivo:
                # abre o arquivo com a lista de dicionários -> objetos_json
                objetos_json = json.load(arquivo)
                # percorre a lista de dicionários
                for obj in objetos_json:
                    # recupera cada dicionário e cria um objeto
                    c = Service(
                        obj["id"],
                        obj["receptionist_id"],
                        obj["vet_id"],
                        obj["client_id"],
                        obj["animal_id"],
                        obj["description"],
                        obj["date"],
                        obj["status"],
                    )
                    # insere o objeto na lista
                    cls.objetos.append(c)    
        except FileNotFoundError:
            pass
    