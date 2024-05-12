from Functions.Auxiliars.database import *

class Client:
    def __init__(self, id, name, surname, gender, age, mail):
        self.id = id
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.mail = mail
        
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
    def add_client(id, name, surname, gender, age, mail):
        client = Client(id, name, surname, gender, age, mail)
        DatabaseFunctions.insert_register('clients', ['id', 'name', 'surname', 'gender', 'age', 'mail'], [id, name, surname, gender, age, mail])
        return client

    @staticmethod
    def modificate_client(id, name, surname, gender, age, mail):
        DatabaseFunctions.update_register('clients', ['name', 'surname', 'gender', 'age', 'mail'], [name, surname, gender, age, mail, id])
        return Clients.search_client(id)
            
    @staticmethod          
    def remove_client(id):
        client = Clients.search_client(id)
        DatabaseFunctions.delete_register('clients', id)
        return client

    @staticmethod
    def add_many_clients(list_new_clients):
        for client in list_new_clients:
            DatabaseFunctions.insert_register('clients', ['id', 'name', 'surname', 'gender', 'age', 'mail'], [client.id, client.name, client.surname, client.gender, client.age, client.mail])

    @staticmethod
    def remove_all_clients(): 
        DatabaseFunctions.remove_all_registers('clients')

class Sale:
    def __init__(self, id, client_id, date, cash, transaction_state, service_state, description):
        self.id = id
        self.client_id = client_id
        self.date = date
        self.cash = cash
        self.transaction_state = transaction_state
        self.service_state = service_state
        self.description = description
    
class Sales:
    DatabaseFunctions.create_tables('2')

    @staticmethod
    def load_sales():
        return DatabaseFunctions.load_from_table('sales', Sale)
    
    @staticmethod
    def search_sale(id):
        sales = Sales.load_sales()
        for sale in sales:
            if sale.id == id:
                return sale
            
    @staticmethod
    def add_sale(id, client_id, date, cash, transaction_state, service_state, description):
        sale = Sale(id, client_id, date, cash, transaction_state, service_state, description)
        DatabaseFunctions.insert_register('sales', ['id', 'client_id', 'date', 'cash', 'transaction_state', 'service_state', 'description'], [id, client_id, date, cash, transaction_state, service_state, description])
        return sale

    @staticmethod
    def modificate_sale(id, cash, transaction_state, service_state, description):
        DatabaseFunctions.update_register('sales', ['cash', 'transaction_state', 'service_state', 'description'], [cash, transaction_state, service_state, description, id])
        return Sales.search_sale(id)
            
    @staticmethod
    def remove_sale(id):
        sale = Sales.search_sale(id)
        DatabaseFunctions.delete_register('sales', id)
        return sale

    @staticmethod
    def add_many_sales(list_new_sales):
        for sale in list_new_sales:
            DatabaseFunctions.insert_register('sales', ['id', 'client_id', 'date', 'cash', 'transaction_state', 'service_state', 'description'], [sale.id, sale.client_id, sale.date, sale.cash, sale.transaction_state, sale.service_state, sale.description])

    @staticmethod
    def remove_all_sales():
        DatabaseFunctions.remove_all_registers('sales')

class Worker:
    def __init__(self, id, name, surname, position, salary, mail):
        self.id = id
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary
        self.mail = mail

class Workers:
    DatabaseFunctions.create_tables('3')

    @staticmethod
    def load_workers():
        return DatabaseFunctions.load_from_table('workers', Worker)
    
    @staticmethod
    def search_worker(id):
        workers = Workers.load_workers()
        for worker in workers:
            if worker.id == id:
                return worker
            
    @staticmethod
    def add_worker(id, name, surname, position, salary, mail):
        worker = Worker(id, name, surname, position, salary, mail)
        DatabaseFunctions.insert_register('workers', ['id', 'name', 'surname', 'position', 'salary', 'mail'], [id, name, surname, position, salary, mail])
        return worker
        
    @staticmethod
    def modificate_worker(id, name, surname, position, salary, mail):
        DatabaseFunctions.update_register('workers', ['name', 'surname', 'position', 'salary', 'mail'], [name, surname, position, salary, mail, id])
        return Workers.search_worker(id)
                
    @staticmethod
    def remove_worker(id):
        worker = Workers.search_worker(id)
        DatabaseFunctions.delete_register('workers', id)
        return worker
                
    @staticmethod
    def add_many_workers(list_new_workers):
        for worker in list_new_workers:
            DatabaseFunctions.insert_register('workers', ['id', 'name', 'surname', 'position', 'salary', 'mail'], [worker.id, worker.name, worker.surname, worker.position, worker.salary, worker.mail])

    @staticmethod
    def remove_all_workers():
        DatabaseFunctions.remove_all_registers('workers')

class Expense:
    def __init__(self, id, worker_id, date, cash, transaction_state, description):
        self.id = id
        self.worker_id = worker_id
        self.date = date
        self.cash = cash
        self.transaction_state = transaction_state
        self.description = description

class Expenses:
    DatabaseFunctions.create_tables('4')

    @staticmethod
    def load_expenses():
        return DatabaseFunctions.load_from_table('expenses', Expense)
    
    @staticmethod
    def search_expense(id):
        expenses = Expenses.load_expenses()
        for expense in expenses:
            if expense.id == id:
                return expense
            
    @staticmethod
    def add_expense(id, worker_id, date, cash, transaction_state, description):
        expense = Expense(id, worker_id, date, cash, transaction_state, description)
        DatabaseFunctions.insert_register('expenses', ['id', 'worker_id', 'date', 'cash', 'transaction_state', 'description'], [id, worker_id, date, cash, transaction_state, description])
        return expense
    
    @staticmethod
    def modificate_expense(id, date, cash, transaction_state, description):
        DatabaseFunctions.update_register('expenses', ['date', 'cash', 'transaction_state', 'description'], [date, cash, transaction_state, description, id])
        return Expenses.search_expense(id)
    
    @staticmethod
    def remove_expense(id):
        expense = Expenses.search_expense(id)
        DatabaseFunctions.delete_register('expenses', id)
        return expense

    @staticmethod
    def add_many_expenses(list_new_expenses):
        for expense in list_new_expenses:
            DatabaseFunctions.insert_register('expenses', ['id', 'worker_id', 'date', 'cash', 'transaction_state', 'description'], [expense.id, expense.worker_id, expense.date, expense.cash, expense.transaction_state, expense.description])

    @staticmethod
    def remove_all_expenses():
        DatabaseFunctions.remove_all_registers('expenses')