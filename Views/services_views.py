from Views.animals_views import animal_list_id
from models.service import Service, Services
from Views.users_views import get_user_name, get_user_fone, get_user_email

@staticmethod
def service_list():
    return Services.listar()

@staticmethod
def service_list_id(id):
    return Services.listar_id(id)

@staticmethod
def service_list_user_id(user_id):
    return Services.listar_services_client_id(user_id)
@staticmethod
def service_list_animal_id(animal_id):
    return Services.listar_services_animal_id(animal_id)
@staticmethod
def service_list_vet_id(vet_id):
    services = []
    for service in Services.listar():
        if service.vet_id == vet_id:
            services.append(service)
    return services
@staticmethod
def service_request(vet_id, service_id):
    s = service_list_id(vet_id, service_id)
    if s.status == "open" and s.vet_id == None:
        s.vet_id = vet_id
        Services.atualizar(s)

@staticmethod
def service_details(id):
    s = service_list_id(id)
    if s:
        print("ID: ", s.id)
        print (f"Receptionist:\n ID:  {s.receptionist_id} - Name: {get_user_name(s.receptionist_id)}")
        print (f"Vet:\n ID:  {s.vet_id} - Name: {get_user_name(s.vet_id)}")
        print (f"Client:\n ID:  {s.client_id} - Name: {get_user_name(s.client_id)}")
        print (f"Animal:\n ID:  {animal_list_id(s.animal_id)}")
        print (f"Description: {s.description}")
        print (f"created at: {s.date}")
        print (f"Status: {s.status}")
    else:
        print("Service not found")
@staticmethod
def service_register(id, receptionist_id, vet_id, client_id, animal_id, description, date, status):
    c = Service(id, receptionist_id, vet_id, client_id, animal_id, description, date, status)
    Services.inserir(c)
    return c

@staticmethod
def service_edit(id, instance):
    c = Service(id, instance)
    Services.atualizar(c)
@staticmethod
def service_update_status (service_id, status):
    service = service_list_id(service_id)
    s = Service(service_id, service.receptionist_id, service.vet_id, service.client_id, service.animal_id, service.service_items, service.description, service.date, status)
    Services.atualizar(s)

@staticmethod
def service_delete(id):
    c = Service(id, "")
    Services.excluir(c)

