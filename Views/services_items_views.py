from models.service_item import ServiceItem, ServiceItems

@staticmethod
def service_item_list():
    return ServiceItems.listar()

@staticmethod
def service_item_list_id(id):
    return ServiceItems.listar_id(id)

@staticmethod
def service_item_register(id, service_id, products, procedures, total):
    c = ServiceItem(id, service_id, products, procedures,)
    ServiceItems.inserir(c)
    return c

@staticmethod
def include_procedure(service_item_id, procedure_id):
    s = ServiceItems.listar_id(service_item_id)
    novo = ServiceItem(s.id, s.service_id, s.products, s.procedures, s.total)
    novo.procedures.append(procedure_id)
    ServiceItems.atualizar(novo)

@staticmethod
def include_product(service_item_id, product_id, quantity):
    s = ServiceItems.listar_id(service_item_id)
    novo = ServiceItem(s.id, s.service_id, s.products, s.procedures, s.total)
    for i in range(quantity):
        novo.products.append(product_id)
    ServiceItems.atualizar(novo)

@staticmethod
def service_item_edit(id, instance):
    c = ServiceItem(id, instance)
    ServiceItems.atualizar(c)

@staticmethod
def service_item_delete(id):
    c = ServiceItem(id, "")
    ServiceItems.excluir(c)

def update_total(procedure, cost):
    ServiceItems.atualizar_total(procedure, cost)