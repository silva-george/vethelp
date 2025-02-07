
from models.user import User, Users
from models.receptionist import Recepcionist, Recepcionists
from models.vet import Vet, Vets
from models.cilent import Client, Clients
from models.animal import Animal, Animals

def main():
    c = User(1, "João", "j@j.com", "123", "123")
    Users.inserir(c)
    r = Recepcionist(c.id, c.id, "cpf12356")
    Recepcionists.inserir(r)

    lista = Recepcionists.listar()
    print("recepcionists: ",*lista)

    por_id = Recepcionists.listar_id(5)
    print(por_id)


    v = User(1, "Vwt", "vet@vet.com", "1233232", "123456")
    Users.inserir(v)
    vet = Vet(v.id, v.id, "123456", "crm123456")
    Vets.inserir(vet)

    lista = Vets.listar()
    print("vets: ",*lista)

    por_id = Vets.listar_id(1)
    print(por_id)


    a = User(1, "cliente", "j@j.com", "123", "123")
    Users.inserir(a)
    client = Client(a.id, a.id, "123456", "rua do bolo, 0")
    Clients.inserir(client)

    lista = Clients.listar()
    print("clients: ",*lista)

    clinet_id = Clients.listar_id(1)
    print(clinet_id)

    animal = Animal(clinet_id, 1, "animal", "race", "gender")
    Animals.inserir(animal)

    lista = Animals.listar()
    print("animais: ",*lista)


main()