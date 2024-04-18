from Functions.Auxiliars.database import *

class Client:
    def __init__(self, id, name, surname, gender, age):
        self.id = id
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        
class Clients:
    list_clients = []

    with SimpleConnection(DATABASE_PATH) as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS clients" \
                    "(id VARCHAR PRIMARY KEY, name VARCHAR, surname VARCHAR, gender VARCHAR, age INTEGER)")
    
        content = cursor.execute('SELECT * FROM clients').fetchall()
        for id, name, surname, gender, age in content:
            client = Client(id, name, surname, gender, age)
            list_clients.append(client) 

    @staticmethod
    def search_client(id):
        for client in Clients.list_clients:
            if client.id == id:
                return client

    @staticmethod
    def add_client(id, name, surname, gender, age):
        with ConnectionCommit(DATABASE_PATH) as cursor: 
            client = Client(id, name, surname, gender, age)
            Clients.list_clients.append(client) 
            cursor.execute("INSERT INTO clients(id, name, surname, gender, age) VALUES(?, ?, ?, ?, ?)", (client.id, client.name, client.surname, client.gender, client.age))
           
            return client
    
    @staticmethod
    def modificate_client(id, name, surname, gender, age):
        with ConnectionCommit(DATABASE_PATH) as cursor: 
             for i, client in enumerate(Clients.list_clients):
                if client.id == id:
                    Clients.list_clients[i].name = name
                    Clients.list_clients[i].surname = surname
                    Clients.list_clients[i].gender = gender
                    Clients.list_clients[i].age = age 
                    cursor.execute("UPDATE clients SET name = ?, surname = ?, gender = ?, age = ? WHERE id = ?", (client.name, client.surname, client.gender, client.age, client.id))
                
                    return Clients.list_clients[i]
            
    @staticmethod          
    def remove_client(id):
        with ConnectionCommit(DATABASE_PATH) as cursor:
            for index, client in enumerate(Clients.list_clients):
                if client.id == id:
                    Clients.list_clients.pop(index)
                    cursor.execute("DELETE FROM clients WHERE id = ?", (id,))
                    return client

    @staticmethod
    def add_many_clients(list_new_clients):
        with ConnectionCommit(DATABASE_PATH) as cursor:
            for any in list_new_clients:
                client = Client(any[0], any[1], any[2], any[3], any[4])
                Clients.list_clients.append(client) 
                cursor.execute("INSERT INTO clients(id, name, surname, gender, age) VALUES(?, ?, ?, ?, ?)", (client.id, client.name, client.surname, client.gender, client.age))

    @staticmethod
    def remove_all_clients(): 
        with ConnectionCommit(DATABASE_PATH) as cursor:
            cursor.execute("DELETE FROM clients;")
            Clients.list_clients.clear()

class Sale:
    def __init__(self, id, client_id, date, cash, transaction_state, service_state):
        self.id = id
        self.client_id = client_id
        self.date = date
        self.cash = cash
        self.transaction_state = transaction_state
        self.service_state = service_state
    
    def __str__(self):
        return "N° {}, {} and {}".format(self.id, self.transaction_state, self.service_state)

class Sales:
    list_sales = []

    with SimpleConnection(DATABASE_PATH) as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS sales" \
                    "(id INTEGER PRIMARY KEY AUTOINCREMENT, client_id VARCHAR, date VARCHAR, cash INTEGER, transaction_state VARCHAR, service_state VARCHAR, FOREIGN KEY (client_id) REFERENCES clients(id))")

        content = cursor.execute('SELECT * FROM sales').fetchall()
        for id, client_id, date, cash, transaction_state, service_state in content:
            sale = Sale(id, client_id, date, cash, transaction_state, service_state)
            list_sales.append(sale)

    @staticmethod
    def search_sale(id):
        for sale in Sales.list_sales:
            if sale.id == id:
                return sale
            
    @staticmethod
    def add_sale(id, client_id, date, cash, transaction_state, service_state):
        with ConnectionCommit(DATABASE_PATH) as cursor: 
            sale = Sale(id, client_id, date, cash, transaction_state, service_state)
            cursor.execute("INSERT INTO sales(id, client_id, date, cash, transaction_state, service_state) VALUES(?, ?, ?, ?, ?, ?)", (sale.id, sale.client_id, sale.date, sale.cash, sale.transaction_state, sale.service_state))

            return sale

    @staticmethod
    def modificate_sale(id, transaction_state, service_state):
        with ConnectionCommit(DATABASE_PATH) as cursor:
            for i, sale in enumerate(Sales.list_sales):
                if sale.id == id:
                    Clients.list_sales[i].transaction_state = transaction_state
                    Clients.list_sales[i].service_state = service_state
                    cursor.execute("UPDATE sales SET transaction_state = ?, service_state = ? WHERE id = ?", (sale.transaction_state, sale.service_state, sale.id))
                    return sale
            
    @staticmethod
    def remove_sale(id):
        with ConnectionCommit(DATABASE_PATH) as cursor:
            for i, sale in enumerate(Sales.list_sales):
                if sale.id == id:
                    Sales.list_sales.pop(i)
                    cursor.execute("DELETE FROM sales WHERE id = ?", (id,))
                    return sale

    @staticmethod
    def add_many_sales(list_new_sales):
        with ConnectionCommit(DATABASE_PATH) as cursor:
            for any in list_new_sales:
                sale = Sale(any[0], any[1], any[2], any[3], any[4], any[5])
                Sales.list_sales.append(sale)
                cursor.execute("INSERT INTO sales(id, client_id, date, cash, transaction_state, service_state) VALUES(?, ?, ?, ?, ?, ?)", (sale.id, sale.client_id, sale.date, sale.cash, sale.transaction_state, sale.service_state))

    @staticmethod
    def remove_all_sales():
        with ConnectionCommit(DATABASE_PATH) as cursor:
            cursor.execute("DELETE FROM sales;")
            Sales.list_sales.clear()