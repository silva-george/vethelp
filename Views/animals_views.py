from models.animal import Animal, Animals

@staticmethod
def animal_list():
    return Animals.listar()

@staticmethod
def animal_list_id(id):
    return Animals.listar_id(id)

@staticmethod
def animal_list_user_id(user_id):
    animal_user_list = []
    animals = Animals.listar()
    for animal in animals:
        if animal.user_id == user_id:
            animal_user_list.append(animal)
    return animal_user_list

@staticmethod
def animal_register(user_id, id, name, race, gender):
    c = Animal(user_id, id, name, race, gender)
    Animals.inserir(c)
    return c

@staticmethod
def animal_edit(id, instance):
    c = Animal(id, instance)
    Animals.atualizar(c)

@staticmethod
def animal_delete(id):
    c = Animal(id, "")
    Animals.excluir(c)

