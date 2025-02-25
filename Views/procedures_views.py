from models.procedure import Procedure,  Procedures


@staticmethod
def procedure_list():
    return Procedures.listar()

@staticmethod
def procedure_list_id(id):
    return Procedures.listar_id(id)

@staticmethod
def procedure_create(name, description, price):
    c = Procedure(0, name, description, price)
    Procedures.inserir(c)

@staticmethod
def procedure_edit(id, instance):
    c = Procedure(id, instance)
    Procedures.atualizar(c)

@staticmethod
def procedure_delete(id):
    c = Procedure(id, "", "")
    Procedures.excluir(c)