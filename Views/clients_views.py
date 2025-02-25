from models.client import Client, Clients

@staticmethod
def client_list():
    return Clients.listar()

@staticmethod
def client_list_id(id):
    return Clients.listar_id(id)

@staticmethod
def client_register(user_id, client_id, cpf, adress):
    c = Client(user_id, client_id, cpf, adress)
    Clients.inserir(c)
    return c

@staticmethod
def client_edit(id, instance):
    c = Client(id, instance)
    Clients.atualizar(c)

@staticmethod
def client_delete(id):
    c = Client(id, "")
    Clients.excluir(c)

