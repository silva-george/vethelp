from models.user import User, Users

@staticmethod
def user_auth(email, password):
    for u in Users.listar():
        if u.email == email and u.senha == password:
            u = { "id" : u.id, "nome" : u.nome, "email" : u.email, "fone" : u.fone, "user_type" : u.user_type }
            return u
    return None


@staticmethod
def admin_create():
    if not Users.listar():
        c = User(1, "Admin", "admin", "123", "123", "admin")
        Users.inserir(c)
@staticmethod
def user_list():
    return Users.listar()

@staticmethod
def user_list_id(id):
    return Users.listar_id(id)

@staticmethod
def user_register(name, email, phone, password, user_type ):
    c = User(0, name, email, phone, password, user_type)

    return Users.inserir(c)

@staticmethod
def user_edit(id, instance):
    c = User(id, instance)
    Users.atualizar(c)

@staticmethod
def user_delete(id):
    c = User(id, "")
    Users.excluir(c)


def get_user_name(id):
    u = Users.listar_id(id)
    return u.nome

def get_user_email(id):
    u = Users.listar_id(id)
    return u.email


def get_user_fone(id):
    u = Users.listar_id(id)
    return u.fone
def get_user_type(id):
    u = Users.listar_id(id)
    return u.user_type