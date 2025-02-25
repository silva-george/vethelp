from models.vet import Vet, Vets


@staticmethod
def vet_list():
    return Vets.listar()

@staticmethod
def vet_list_id(id):
    return Vets.listar_id(id)

@staticmethod
def vet_create(user_id, id, cpf, crm):
    c = Vet(user_id, id, cpf, crm)
    Vets.inserir(c)
    return c

@staticmethod
def vet_edit(id, instance):
    c = Vet(id, instance)
    Vets.atualizar(c)

@staticmethod
def vet_delete(id):
    c = Vet(id, "")
    Vets.excluir(c)
