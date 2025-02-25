import datetime
import getpass
from Views import (
    clients_views,
    procedures_views,
    products_views,
    recepcionists_views,
    services_items_views,
    services_views,
    animals_views,
    users_views,
    vets_views,
)
from models.procedure import Procedure, Procedures

class UI:
    # dados do usuário logado
    user_id = 0
    user_nome = ""
    user_type = ""
#SECTION LOGIN
    @staticmethod
    def login_user():
        print("\nMake login to continue:")
        print("Tipe your email: ")
        email = input()
        print("Tipe your password: ")
        password = getpass.getpass()
        user = users_views.user_auth(email, password)
        if user == None:
            print("\n!!!  Wrong user or password  !!!")
            print("Verify if your email and password are correct and try again \n")
            return UI.login_user()
        else:
            UI.user_id = user["id"]
            UI.user_nome = user["nome"]
            UI.user_type = user["user_type"]
            print(f"\n ----------Welcome, {UI.user_nome}----------\n ")
            try:
                if UI.user_type == "receptionist":
                    return UI.menu_receptionist()
                elif UI.user_type == "vet":
                    return UI.menu_vet()
                elif UI.user_type == "admin":
                    return UI.menu_admin()
            except Exception as e:
                print(e)
                print(
                    "This User dont have permissions to use this system, contact the admin")
                print("clinic@vethelp.com or (84) 9999-9999")
                return UI.logout()

    @staticmethod
    def logout():
        UI.user_id = 0
        UI.user_nome = ""
        UI.user_type = None
        UI.main()

#ADMIN --------------------------------------------
    @staticmethod
    def menu_admin():
        print("\n----------Users Management----------")
        print(" 1 - Insert a new Receptionist\n 2 - Insert a new Vet\n 3 - Edit a User-\n 4 - Remove a User")

        print("\n----------Produtos Management----------")
        print(" 5 - Insert a Product\n 6 - List Products\n 7 - Update a Product\n 8 - Delete a Product")

        print("\n----------Procedure Management----------")
        print(" 9 - Insert a Procedure\n 10 - List Procedures\n 11 - Update a Procedure\n 12 - Delete a Procedure")
        
        print("0 - Logout, 99 - END")

        op = int(input("\nChose an option: "))
        if op == 0:
            UI.logout()
        elif op == 1:
            UI.receptionist_register()
            UI.menu_admin()
        elif op == 2:
            UI.vet_register()
            UI.menu_admin()
        elif op == 3:
            UI.user_update()
            UI.menu_admin()
        elif op == 4:
            UI.user_delete()
            UI.menu_admin()
        elif op == 5:
            UI.product_register()
            UI.menu_admin()
        elif op == 6:
            UI.product_list()
            UI.menu_admin()
        elif op == 7:
            UI.product_update()
            UI.menu_admin()
        elif op == 8:
            UI.product_delete()
            UI.menu_admin()
        elif op == 9:
            UI.procedure_register()
        elif op == 10:
            UI.procedure_list()
            UI.menu_admin()
        elif op == 11:
            UI.procedure_update()
            UI.menu_admin()
        elif op == 12:
            UI.procedure_delete()
            UI.menu_admin()
        elif op == 99:
            print("Goodbye")
            UI.logout()
        else:
            print("Invalid option, back to menu")
            UI.menu_admin()


#RECEPCIONIST -------------------------------------------
    @staticmethod
    def menu_receptionist():
        print(f"\n Loged as {UI.user_nome}, chose a option and press enter:\n")
        print("1 - Client Register")
        print("2 - Client List")
        print("3 - Animal Register")
        print("4 - Animal List")
        print("5 - Service Register")
        print("6 - Service List")
        print("7 - Service List by ID")

        print("99 - Exit")

        op = int(input("\nInforme uma opção: "))
        if op == 1:
            UI.cliente_register()
            UI.menu_receptionist()
        elif op == 2:
            UI.cliente_list()
            UI.menu_receptionist()
        elif op == 3:
            UI.animal_register()
            UI.menu_receptionist()
        elif op == 4:
            UI.animal_list()
            UI.menu_receptionist()
        elif op == 5:
            UI.service_register()
            UI.menu_receptionist()
        elif op == 6:
            UI.service_list()
            UI.menu_receptionist()
        elif op == 7:
            UI.service_list_id()
            UI.menu_receptionist()

        elif op == 99:
            UI.logout()
        else:
            print("\n invalid option, tipe 1 to try again or 99 to exit")
            op = int(input("\nType a option and press enter: "))
            if op != 1 and op != 99:
                print("Invalid option, you will be redirected to menu")
                return UI.menu_receptionist()
            elif op == 1:
                return UI.menu_receptionist()
            elif op == 99:
                return UI.logout()


    @staticmethod
    def receptionist_register():
        try:
            print("\n----------Register a new receptionist-----------\n")

            print("\n Receptionist name: ")
            name = input()
            print("\n Receptionist email: ")
            email = input()
            print("\n Receptionist phone: ")
            phone = input()
            password = None
            user_type = "receptionist"
            print("\n Receptionist CPF: ")
            cpf = input()

            
            user = users_views.user_register(name, email, phone, password, user_type)
            receptionist = recepcionists_views.receptionist_create(user.id, user.id, cpf)

            print(f"\n Receptionist {receptionist} created with success!!\n")

        except Exception as e:
            print(e)
            print("\nChoose 1 to try again or 99 to exit")
            op = int(input("\nType a option and press enter: "))
            if op != 1 and op != 99:
                print("Invalid option, back to menu")
                UI.menu_receptionist()
            elif op == 1:
                UI.cliente_register()
            else:
                UI.menu_receptionist()

        

# CLIENTS -------------------------------------------
    def cliente_register():
        try:
            print("\n----------Register a new Client-----------\n")

            print("\nClient name: ")
            name = input()
            print("\nClient email: ")
            email = input()
            print("\nClient phone: ")
            phone = input()
            password = None
            user_type = "client"
            print("\nClient CPF: ")
            cpf = input()
            print("\nClient Adress: ")
            adress = input()

            user = users_views.user_register(name, email, phone, password, user_type)

            client = clients_views.client_register(user.id, user.id, cpf, adress)

            print(f"\nClient {client} created with success!!\n")

        except Exception as e:
            print(e)
            print("\nChoose 1 to try again or 99 to exit")
            op = int(input("\nType a option and press enter: "))
            if op != 1 and op != 99:
                print("Invalid option, back to menu")
                UI.menu_receptionist()
            elif op == 1:
                UI.cliente_register()
            else:
                UI.menu_receptionist()

    @staticmethod
    def cliente_list():
        clients = clients_views.client_list()
        if not clients:
            print("No clients registered")
            UI.menu_receptionist()
        else:
            print("Clients List: ")
            for client in clients:
                print(
                    f"ID: {client.id} - Name: {users_views.get_user_name(client.id)} CPF: {client.cpf} - Adress: {client.adress}"
                )
    
    @staticmethod
    def client_list_id():
        print("Type the id of the client: ")
        clients = clients_views.client_list()
        cleints_list = []
        for client in clients:
            print(f"ID: {client.id} - CPF: {client.cpf}")
            cleints_list.append(client.id)
        id = int(input())
        if id not in cleints_list:
            print("Invalid id, back to menu")
            UI.menu_receptionist()
        else:
            client = clients_views.client_list_id(id)

# ANIMAL: -------------------------------------------

    @staticmethod
    def animal_register():
        try:
            print("----------Register a new Animal----------- \n")
            print("\nTipe the id of the animal owner: ")
            print("Clients ida: ")
            clients = clients_views.client_list()
            clients_list = []
            for client in clients:
                print(f"ID: {client.id} - CPF: {client.cpf}")
                clients_list.append(client.id)
            user_id = int(input())
            if user_id not in clients_list:
                print("Invalid id, back to menu")
                UI.menu_receptionist()

            print("\nAnimal name: ")
            name = input()
            print("\nAnimal race: ")
            race = input()
            print("\nAnimal gender: ")
            gender = input()
            id = None

            animal = animals_views.animal_register(user_id, id, name, race, gender)

            print(f"\n Animal {animal.name} created with success!!")
            UI.menu_receptionist()

        except Exception as e:
            print(e)
            print("\nChoose 1 to try again or 99 to exit")
            op = int(input("\nType a option and press enter: "))
            if op != 1 and op != 99:
                print("Invalid option, back to menu")
                UI.menu_receptionist()
            elif op == 1:
                UI.cliente_register()
            else:
                UI.menu_receptionist()

    @staticmethod
    def animal_list():
        animals = animals_views.animal_list()
        if not animals:
            print("No animals registered")
            UI.menu_receptionist()
        else:
            print("Animals List: \n")
            for animal in animals:
                print(
                    f"ID: {animal.id} - Name: {animal.name} - Race: {animal.race} - Gender: {animal.gender}")
            UI.menu_receptionist()

# SERVICE ----------

    @staticmethod
    def service_register():
        try:
            id = None
            receptionist_id = UI.user_id
            print("----------Register a new Service----------- \n")
            print("Clients ids: ")
            clients = clients_views.client_list()
            for client in clients:
                print(f"ID: {client.id} - CPF: {client.cpf}")
            print("\nWhat is the client id?")
            client_id = int(input())
            print("\n")

            animals = animals_views.animal_list_user_id(client_id)
            if not animals:
                print("This Client has no animals registered")
                UI.menu_receptionist()
            else:    
                print("\n Animals of this client: ")
                client_animals_ids =[]
                for animal in animals:
                    print(
                        f"ID: {animal.id} - Name: {animal.name} - Race: {animal.race} - Gender: {animal.gender}")
                    client_animals_ids.append(animal.id)
            print("\nWhat is the animal id?")
            animal_id = int(input())
            if animal_id not in client_animals_ids:
                print("Invalid id, back to menu")
                UI.menu_receptionist()
            print("\n")

            print("\nDescription: ")
            description = input()
            print("\nVet response: ")

            print("\nChose a vet for this service: ")
            vets = UI.vet_list()
            vets_ids = []
            if not vets:
                print("No vets registered")
                UI.menu_receptionist()
            else:
                for vet in vets:
                    print(f"ID: {vet.id} - Name: {users_views.get_user_name(vet.id)}")
                    vets_ids.append(vet.id)
            print("\nTipe the vet id: ")
            vet_id = int(input())
            if vet_id not in vets_ids:
                print("Invalid id, back to menu")
                UI.menu_receptionist()
            date = str(datetime.datetime.now())
            status = "open"
            service = services_views.service_register(
                id,
                receptionist_id,
                vet_id,
                client_id,
                animal_id,
                description,
                date,
                status,
            )
            serice_item = services_items_views.service_item_register(service.id, service.id, [], [], 0)
            print(f"\n Service {service} created with success!!")
            UI.menu_receptionist()

        except Exception as e:
            print(e)
            print("\nChoose 1 to try again or 99 to exit")
            op = int(input("\nType a option and press enter: "))
            if op != 1 and op != 99:
                print("\nInvalid option, back to menu")
                UI.menu_receptionist()
            elif op == 1:
                UI.service_register()
            else:
                UI.menu_receptionist()

    @staticmethod
    def service_list():
        services = services_views.service_list()
        if not services:
            print("No services registered")
            if UI.user_type == "receptionist":
                UI.menu_receptionist()
            elif UI.user_type == "vet":
                UI.menu_vet()
        else:
            print("\n Services List: ")
            for service in services:
                print(
                    f"ID: {service.id} - Animal id: {service.animal_id} - Vet id: {service.vet_id} - Description: {service.description} - Date: {service.date} - Status: {service.status}"
                )
            print("\n For Service details tipe the Service ID: ")
            UI.service_details(int(input()))
    @staticmethod
    def service_list_id():
        print("What is the service id?")
        print("Tipe 0 if you want see the list of any key to proced")
        op = int(input())
        if op == 0:
            UI.service_list()
        else:
            pass
        print("\nType the ID of the service you want to see: ")
        service_id = int(input())
        service = services_views.service_list_id(service_id)
        if service != None:
            print(f"Service {service_id} details: ")
            print(service)
        else:
            print("Service not found")

    def service_update_status():
        services = services_views.service_list_vet_id(UI.user_id)
        if not services:
            print("No services registered for yur ID")
            if UI.user_type == "receptionist":
                UI.menu_receptionist()
            elif UI.user_type == "vet":
                UI.menu_vet()
        else:
            print("\n Your Services List: ")
            for service in services:
                print(
                    f"ID: {service.id} - Description: {service.description} - Date: {service.date} - Status: {service.status}"
                )
            print("What is the service id?")
            service_id = int(input())
            print("Chose the status for apply to this service:")
            print("1 - open, 2 - closed, 3 - canceled")
            status = int(input())
            if status != 1 and status != 2 and status != 3:
                print("Invalid status, tipe 0 to try again or any key to exit")
                op = int(input("\nType a option and press enter: "))
                if op != 0:
                    if UI.user_type == "receptionist":
                        UI.menu_receptionist()
                    elif UI.user_type == "vet":
                        UI.menu_vet()
                else:
                    UI.service_update_status()
            else:
                if status == 1:
                    status = "open"
                elif status == 2:
                    status = "closed"
                else:
                    status = "canceled"
                services_views.service_update_status(service_id, status)
                print(f"\n Service {service_id} updated with success!!")
            if UI.user_type == "receptionist":
                UI.menu_receptionist()
            elif UI.user_type == "vet":
                UI.menu_vet()

    def service_list_by_id():
        services = services_views.service_list_vet_id(UI.user_id)
        if not services:
            print("No services registered for yur ID")
            return []
        else:
            print("\n Your Services List: ")
            for service in services:
                print(
                    f"ID: {service.id} - Description: {service.description} - Date: {service.date} - Status: {service.status}"
                )
            return services

    def service_list_client_id():
        services = services_views.service_list_client_id(UI.user_id)
        if not services:
            print("No services registered for yur ID")
        return services

    def service_list_animal_id():
        services = services_views.service_list_animal_id(UI.user_id)
        return services
    
    def service_details(service_id):
        return services_views.service_details(service_id)


# SERVICE_ITEM ---------------------------------------------------------------

    @staticmethod
    def service_item_create():
        try:
            services_ids =[]
            print("\n----------Register a new Service Item----------- \n")
            services = UI.service_list_by_id()
            if not services:
                print("No services found for your ID")
                return UI.menu_vet()
            else:
                for service in services:
                    services_ids.append(service.id)

            print("\n What is the service id you want to add a item?")
            service_id = int(input())
            if service_id not in services_ids:
                print("Invalid service id, tipe 0 to try again or any number to exit")
                op = int(input())
                if op != 0:
                    return UI.menu_vet()
                else:
                    return UI.service_item_create()

            print("\nWhat do you want to add?")
            print("1 - Product")
            print("2 - Procedure")

            op2 = int(input())

            if op2 != 1 and op2 != 2:
                print("\nInvalid option, try again")
                return UI.service_item_create()
            elif op2 == 1:
                print("\n Products in stock: ")
                UI.product_list()
                print("\n What is the product id?")
                product_id = int(input())
                product = UI.product_list_id(product_id)
                print("\n What is the quantity of this product?")
                quantity = int(input())
                while quantity > product.stock or quantity <= 0:
                    print("\n Quantity can't be bigger than stock or less than 0, try again") 
                    print("\n What is the quantity of this product?")
                    quantity = int(input())
                services_items_views.include_product(service_id,product, quantity)
                services_items_views.update_total(services_items_views.service_item_list_id(service_id), product.price * quantity)
                print("\nProduct added with success!!")
                return UI.menu_vet()
            
            elif op2 == 2:
                print("Procedures list:")
                UI.procedure_list()
                print("\n What is the procedure id?")
                procedure_id = int(input())
                procedure = UI.procedure_list_id(procedure_id)
                services_items_views.include_procedure(service_id,procedure)
                print("\nProcedure added with success!!")
                return UI.menu_vet()


        except Exception as e:
            print(e)
            print("\nChoose 1 to try again or 99 to exit")
            op = int(input("\nType a option and press enter: "))
            if op != 1 and op != 99:
                print("\nInvalid option ")
                UI.menu_vet()
            elif op == 1:
                UI.service_item_create()
            else:
                UI.menu_vet()

# PRODUCTS ---------------------------------------------------------------


    @staticmethod
    def product_register():
        try:
            print("----------Register a new Product----------- \n")
            print("\nProduct name: ")
            name = input()
            print("\nProduct description: ")
            description = input()
            print("\nProduct price: ")
            price = float(input())
            print("\nProduct stock: ")
            stock = int(input())
            product = products_views.product_create(name, description, price, stock)
            print(f"\n Product {product.name} created with success!!")
            UI.menu_admin()
        except Exception as e:
            print(e)
            UI.menu_admin()
    @staticmethod
    def product_list():
        products = products_views.product_list()
        for product in products:
            print(
                f"ID: {product.id} - Name: {product.name} - Description: {product.description} - Qantity in stock: {product.stock}"
            )
        next = input("Press enter to continue")
        return products

    @staticmethod
    def product_list_id(product_id):
        product = products_views.product_list_id(product_id)
        print(
            f"ID: {product.id} - Name: {product.name} - Description: {product.description} - Qantity in stock: {product.stock}"
        )
        return product


    
    @staticmethod
    def product_update():
        UI.product_list()
        print("\n What is the product id you want to edit?")
        product_id = int(input())
        print("\nProduct name: ")
        name = input()
        print("\nProduct description: ")
        description = input()
        print("\nProduct price: ")
        price = float(input())
        print("\nProduct stock: ")
        stock = int(input())
        products_views.product_edit(product_id, name, description, price, stock)
        print("\nProduct updated with success!!")
    
    @staticmethod
    def product_delete():
        UI.product_list()
        print("\n What is the product id you want to delete?")
        product_id = int(input())
        products_views.product_delete(product_id)
        print("\nProduct deleted with success!!")
    
    @staticmethod
    def product_update_stock():
        UI.product_list()
        print("\n What is the product id you want to update stock?")
        product_id = int(input())
        print("\nProduct stock: ")
        stock = int(input())
        products_views.product_update_stock(product_id, stock)
        print("\nProduct stock updated with success!!")

# PROCEDURES ---------------------------------------------------------------

    @staticmethod
    def procedure_register():
        try:
            print("----------Register a new Procedure----------- \n")
            print("\nProcedure name: ")
            name = input()
            print("\nProcedure description: ")
            description = input()
            print("\nProcedure price: ")
            price = float(input())
            procedure = procedures_views.procedure_create(name, description, price)
            print(f"\n Procedure {procedure.name} created with success!!")
            UI.menu_admin()
        except Exception as e:
            print(e)
            UI.menu_admin()

    @staticmethod
    def procedure_list():
        procedures = procedures_views.procedure_list()
        if not procedures:
            print("No procedures registered")
            return []
        else:
            for procedure in procedures:
                print(
                    f"ID: {procedure.id} - Name: {procedure.name} - Description: {procedure.description}"
                )
            next = input("Press enter to continue")
        return procedures

    @staticmethod
    def procedure_list_id(procedure_id):
        procedure = procedures_views.procedure_list_id(procedure_id)
        print(
            f"ID: {procedure.id} - Name: {procedure.name} - Description: {procedure.description}"
        )
        return procedure

    @staticmethod
    def procedure_delete():
        UI.procedure_list
        print("\n What is the procedure id you want to delete?")
        procedure_id = int(input())
        procedures_views.procedure_delete(procedure_id)
        print("\nProcedure deleted with success!!")

    @staticmethod
    def procedure_update():
        UI.procedure_list
        print("\n What is the procedure id you want to update?")
        procedure_id = int(input())
        print("\nProcedure name: ")
        name = input()
        print("\nProcedure description: ")
        description = input()
        print("\nProcedure price: ")
        price = float(input())
        procedures_views.procedure_update(procedure_id, name, description, price)
        print("\nProcedure updated with success!!")




# VET ---------------------------------------------------------------
    @staticmethod
    def menu_vet():
        print(f"\n Loged as {UI.user_nome}, chose a option and press enter:\n")
        print("1 - Services List")
        print("2 - My Services")
        print("3 - Edit a service status")
        print("4 - Add a service item to a service")
        print("99 - Exit")

        op = int(input("\nInforme uma opção: "))

        if op == 1:
            UI.service_list()
            UI.menu_vet()
        elif op == 2:
            UI.service_list_by_id()
            UI.menu_vet()
        elif op == 3:
            UI.service_update_status()
            UI.menu_vet()
        elif op == 4:
            UI.service_item_create()
            UI.menu_vet()
        elif op == 99:
            UI.logout()

    @staticmethod
    def vet_list():
        vets = vets_views.vet_list()
        return vets

    @staticmethod
    def vet_list_id():
        vets = vets_views.vet_list_id(UI.user_id)
        for vet in vets:
            print(f"Vet ID: {vet.id} - CRM {vet.crm}")

    @staticmethod
    def vet_register():
        try:
            print("\n----------Register a new vet-----------\n")

            print("\nVet name: ")
            name = input()
            print("\nVet email: ")
            email = input()
            print("\nVet phone: ")
            phone = input()
            password = ""
            user_type = "vet"
            print("\nVet CPF: ")
            cpf = input()
            print("\nVet CRM: ")
            crm = input()

            user = users_views.user_register(name, email, phone, password, user_type)
            vet = vets_views.vet_create(user.id, user.id, cpf, crm)

            print(f"\nVet {vet} created with success!!\n")

        except Exception as e:
            print(e)
            print("\nChoose 1 to try again or 99 to exit")
            op = int(input("\nType a option and press enter: "))
            if op != 1 and op != 99:
                print("Invalid option, back to menu")
                UI.menu_receptionist()
            elif op == 1:
                UI.cliente_register()
            else:
                UI.menu_receptionist()


    # Main
    @classmethod
    def main(cls):
        print("----------WELLCOME TO VETHELP----------\n")
        UI.login_user()

UI.main()
