from models.receptionist import Recepcionist, Recepcionists


@staticmethod
def receptionist_list():
    return Recepcionists.listar()

@staticmethod
def receptionist_list_id(id):
    return Recepcionists.listar_id(id)

@staticmethod
def receptionist_create(user_id, id, cpf):
    c = Recepcionist(user_id, id, cpf)
    Recepcionists.inserir(c)

@staticmethod
def receptionist_edit(id, instance):
    c = Recepcionist(id, instance)
    Recepcionists.atualizar(c)

@staticmethod
def receptionist_delete(id):
    c = Recepcionist(id, "")
    Recepcionists.excluir(c)
