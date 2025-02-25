from models.product import Product,  Products


@staticmethod
def product_list():
    return Products.listar()

@staticmethod
def product_list_id(id):
    return Products.listar_id(id)

@staticmethod
def product_create(name, description, price, stock):
    c = Product(0, name, description, price, stock)
    return Products.inserir(c)
    

@staticmethod
def product_edit(product_id, name, description, price, stock):
    c = Product(product_id, name, description, price, stock)
    Products.atualizar(c)

@staticmethod
def product_update_stock(id, stock):
    c = product_list_id(id)
    c.stock = stock
    Products.atualizar(c)
@staticmethod
def product_delete(id):
    c = Product(id, "")
    Products.excluir(c)