from Functions.Auxiliars.database import *

class Client:
    def __init__(self, id, name, surname, gender, age):
        self.id = id
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        
class Clients:
    DatabaseFunctions.create_tables('1')

    @staticmethod
    def load_clients():
        return DatabaseFunctions.load_from_table('clients', Client)

    @staticmethod
    def search_client(id):
        clients = Clients.load_clients()
        for client in clients:
            if client.id == id:
                return client

    @staticmethod
    def add_client(id, name, surname, gender, age):
        client = Client(id, name, surname, gender, age)
        DatabaseFunctions.insert_register('clients', ['id', 'name', 'surname', 'gender', 'age'], [id, name, surname, gender, age])
        return client

    @staticmethod
    def modificate_client(id, name, surname, gender, age):
        DatabaseFunctions.update_register('clients', ['name', 'surname', 'gender', 'age'], [name, surname, gender, age, id])
        return Clients.search_client(id)
            
    @staticmethod          
    def remove_client(id):
        client = Clients.search_client(id)
        DatabaseFunctions.delete_register('clients', id)
        return client

    @staticmethod
    def add_many_clients(list_new_clients):
        for client in list_new_clients:
            DatabaseFunctions.insert_register('clients', ['id', 'name', 'surname', 'gender', 'age'], [client.id, client.name, client.surname, client.gender, client.age])

    @staticmethod
    def remove_all_clients(): 
        DatabaseFunctions.remove_all_registers('clients')

class Sale:
    def __init__(self, id, client_id, date, cash, transaction_state, service_state):
        self.id = id
        self.client_id = client_id
        self.date = date
        self.cash = cash
        self.transaction_state = transaction_state
        self.service_state = service_state
    
class Sales:
    @staticmethod
    def load_sales():
        return DatabaseFunctions.load_from_table('clients', Sales)
    
    @staticmethod
    def search_sale(id):
        sales = Sales.load_sales()
        for sale in sales:
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

class Worker:
    def __init__(self, id, name, surname, position, salary):
        self.id = id
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary

class Workers:
    list_workers = []

    with SimpleConnection(DATABASE_PATH) as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS workers" \
                    "(id VARCHAR PRIMARY KEY, name VARCHAR, surname VARCHAR, position VARCHAR, salary INTEGER)")
        
        content = cursor.execute('SELECT * FROM workers').fetchall()
        for id, name, surname, position, salary in content:
            worker = Worker(id, name, surname, position, salary)
            list_workers.append(worker)

    @staticmethod
    def search_worker(id):
        for worker in Workers.list_workers:
            if worker.id == id:
                return worker
            
    @staticmethod
    def add_worker(id, name, surname, position, salary):
        with ConnectionCommit(DATABASE_PATH) as cursor:
            worker = Worker(id, name, surname, position, salary)
            Workers.list_workers.append(worker)
            cursor.execute('INSERT INTO workers(id, name, surname, position, salary) VALUES(?, ?, ?, ?, ?)', (worker.id, worker.name, worker.surname, worker.position, worker.salary))
            return worker
        
    @staticmethod
    def modificate_worker(id, name, surname, position, salary):
        with ConnectionCommit(DATABASE_PATH) as cursor:
            for i, worker in enumerate(Workers.list_workers):
                if worker.id == id:
                    Workers.list_workers[i].name = name
                    Workers.list_workers[i].surname = surname
                    Workers.list_workers[i].position = position
                    Workers.list_workers[i].salary = salary
                    cursor.execute('UPDATE workers SET name = ?, surname = ?, position = ?, salary = ? WHERE id = ?', (worker.name, worker.surname, worker.position, worker.salary, worker.id))
                    return Workers.list_workers[i]
                
    @staticmethod
    def remove_worker(id):
        with ConnectionCommit(DATABASE_PATH) as cursor:
            for i, worker in enumerate(Workers.list_workers):
                if worker.id == id:
                    Workers.list_workers.pop(i)
                    cursor.execute('DELETE FROM works WHERE id = ?', (id))
                    return worker
                
    @staticmethod
    def add_many_workers(list_new_workers):
        with ConnectionCommit(DATABASE_PATH) as cursor:
            for any in list_new_workers:
                worker = Worker(any[0], any[1], any[2], any[3], any[4])
                Workers.list_workers.append(worker)
                cursor.execute('INSERT INTO workers(id, name, surname, position, salary) VALUES (?, ?, ?, ?, ?)', (worker.id, worker.name, worker.surname, worker.position, worker.salary))

    @staticmethod
    def remove_all_workers():
        with ConnectionCommit(DATABASE_PATH) as cursor:
            cursor.execute('DELETE FROM workers;')