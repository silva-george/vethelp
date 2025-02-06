
from models.user import User, Users

def create (self, nome, email, fone, senha):
    r = User(nome="teste", email="email@teste", fone="555", senha="123456")
    print("user name", r.name)

def main():

    create()

main()