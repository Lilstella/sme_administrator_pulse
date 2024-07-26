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
    @staticmethod
    def create_table_client(db_file):
        DatabaseFunctions.create_tables('1', db_file)

    @staticmethod
    def load_clients(db_file):
        return DatabaseFunctions.load_from_table('clients', Client, db_file)

    @staticmethod
    def search_client(id, db_file):
        clients = Clients.load_clients(db_file)
        for client in clients:
            if client.id == id:
                return client

    @staticmethod
    def add_client(id, name, surname, gender, age, mail, db_file):
        client = Client(id, name, surname, gender, age, mail)
        DatabaseFunctions.insert_register('clients', ['id', 'name', 'surname', 'gender', 'age', 'mail'], [id, name, surname, gender, age, mail], db_file)
        return client

    @staticmethod
    def modificate_client(id, name, surname, gender, age, mail, db_file):
        DatabaseFunctions.update_register('clients', ['name', 'surname', 'gender', 'age', 'mail'], [name, surname, gender, age, mail, id], db_file)
        return Clients.search_client(id, db_file)
            
    @staticmethod          
    def remove_client(id, db_file):
        client = Clients.search_client(id, db_file)
        DatabaseFunctions.delete_register('clients', id, db_file)
        return client

    @staticmethod
    def add_many_clients(list_new_clients, db_file):
        for client in list_new_clients:
            DatabaseFunctions.insert_register('clients', ['id', 'name', 'surname', 'gender', 'age', 'mail'], [client.id, client.name, client.surname, client.gender, client.age, client.mail], db_file)

    @staticmethod
    def remove_all_clients(db_file): 
        DatabaseFunctions.remove_all_registers('clients', db_file)

class Sale:
    def __init__(self, id, client_id, date, cash, paid, delivered, description):
        self.id = id
        self.client_id = client_id
        self.date = date
        self.cash = cash
        self.paid = paid
        self.delivered = delivered
        self.description = description
    
class Sales:
    @staticmethod
    def create_table_sale(db_file):
        DatabaseFunctions.create_tables('2', db_file)

    @staticmethod
    def load_sales(db_file):
        return DatabaseFunctions.load_from_table('sales', Sale, db_file)
    
    @staticmethod
    def search_sale(id, db_file):
        sales = Sales.load_sales(db_file)
        for sale in sales:
            if sale.id == id:
                return sale
            
    @staticmethod
    def add_sale(id, client_id, date, cash, paid, delivered, description, db_file):
        sale = Sale(id, client_id, date, cash, paid, delivered, description)
        DatabaseFunctions.insert_register('sales', ['id', 'client_id', 'date', 'cash', 'paid', 'delivered', 'description'], [id, client_id, date, cash, paid, delivered, description], db_file)
        return sale

    @staticmethod
    def modificate_sale(id, cash, paid, delivered, description, db_file):
        DatabaseFunctions.update_register('sales', ['cash', 'paid', 'delivered', 'description'], [cash, paid, delivered, description, id], db_file)
        return Sales.search_sale(id, db_file)
            
    @staticmethod
    def remove_sale(id, db_file):
        sale = Sales.search_sale(id, db_file)
        DatabaseFunctions.delete_register('sales', id, db_file)
        return sale

    @staticmethod
    def add_many_sales(list_new_sales, db_file):
        for sale in list_new_sales:
            DatabaseFunctions.insert_register('sales', ['id', 'client_id', 'date', 'cash', 'paid', 'delivered', 'description'], [sale.id, sale.client_id, sale.date, sale.cash, sale.paid, sale.delivered, sale.description], db_file)

    @staticmethod
    def remove_all_sales(db_file):
        DatabaseFunctions.remove_all_registers('sales', db_file)

class Worker:
    def __init__(self, id, name, surname, position, salary, mail):
        self.id = id
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary
        self.mail = mail

class Workers:
    @staticmethod
    def create_table_worker(db_file):
        DatabaseFunctions.create_tables('3', db_file)

    @staticmethod
    def load_workers(db_file):
        return DatabaseFunctions.load_from_table('workers', Worker, db_file)
    
    @staticmethod
    def search_worker(id, db_file):
        workers = Workers.load_workers(db_file)
        for worker in workers:
            if worker.id == id:
                return worker
            
    @staticmethod
    def add_worker(id, name, surname, position, salary, mail, db_file):
        worker = Worker(id, name, surname, position, salary, mail)
        DatabaseFunctions.insert_register('workers', ['id', 'name', 'surname', 'position', 'salary', 'mail'], [id, name, surname, position, salary, mail], db_file)
        return worker
        
    @staticmethod
    def modificate_worker(id, name, surname, position, salary, mail, db_file):
        DatabaseFunctions.update_register('workers', ['name', 'surname', 'position', 'salary', 'mail'], [name, surname, position, salary, mail, id], db_file)
        return Workers.search_worker(id, db_file)
                
    @staticmethod
    def remove_worker(id, db_file):
        worker = Workers.search_worker(id, db_file)
        DatabaseFunctions.delete_register('workers', id, db_file)
        return worker
                
    @staticmethod
    def add_many_workers(list_new_workers, db_file):
        for worker in list_new_workers:
            DatabaseFunctions.insert_register('workers', ['id', 'name', 'surname', 'position', 'salary', 'mail'], [worker.id, worker.name, worker.surname, worker.position, worker.salary, worker.mail], db_file)

    @staticmethod
    def remove_all_workers(db_file):
        DatabaseFunctions.remove_all_registers('workers', db_file)

class Expense:
    def __init__(self, id, worker_id, date, cash, paid, description):
        self.id = id
        self.worker_id = worker_id
        self.date = date
        self.cash = cash
        self.paid = paid
        self.description = description

class Expenses:
    @staticmethod
    def create_table_expense(db_file):
        DatabaseFunctions.create_tables('4', db_file)

    @staticmethod
    def load_expenses(db_file):
        return DatabaseFunctions.load_from_table('expenses', Expense, db_file)
    
    @staticmethod
    def search_expense(id, db_file):
        expenses = Expenses.load_expenses(db_file)
        for expense in expenses:
            if expense.id == id:
                return expense
            
    @staticmethod
    def add_expense(id, worker_id, date, cash, paid, description, db_file):
        expense = Expense(id, worker_id, date, cash, paid, description)
        DatabaseFunctions.insert_register('expenses', ['id', 'worker_id', 'date', 'cash', 'paid', 'description'], [id, worker_id, date, cash, paid, description], db_file)
        return expense
    
    @staticmethod
    def modificate_expense(id, date, cash, paid, description, db_file):
        DatabaseFunctions.update_register('expenses', ['date', 'cash', 'paid', 'description'], [date, cash, paid, description, id], db_file)
        return Expenses.search_expense(id, db_file)
    
    @staticmethod
    def remove_expense(id, db_file):
        expense = Expenses.search_expense(id, db_file)
        DatabaseFunctions.delete_register('expenses', id, db_file)
        return expense

    @staticmethod
    def add_many_expenses(list_new_expenses, db_file):
        for expense in list_new_expenses:
            DatabaseFunctions.insert_register('expenses', ['id', 'worker_id', 'date', 'cash', 'paid', 'description'], [expense.id, expense.worker_id, expense.date, expense.cash, expense.paid, expense.description], db_file)

    @staticmethod
    def remove_all_expenses(db_file):
        DatabaseFunctions.remove_all_registers('expenses', db_file)

class Task:
    def __init__(self, id, worker_id, title, content, done):
        self.id = id
        self.worker_id = worker_id
        self.title = title
        self.content = content
        self.done = done

class Tasks:
    @staticmethod
    def create_table_task(db_file):
        DatabaseFunctions.create_tables('5', db_file)

    @staticmethod
    def load_tasks(db_file):
        return DatabaseFunctions.load_from_table('tasks', Task, db_file)
    
    @staticmethod
    def search_task(id, db_file):
        tasks = Tasks.load_tasks(db_file)
        for task in tasks:
            if task.id == id:
                return task
            
    @staticmethod
    def add_task(id, worker_id, title, content, done, db_file):
        task = Task(id, worker_id, title, content, done)
        DatabaseFunctions.insert_register('tasks', ['id', 'worker_id', 'title', 'content', 'done'], [id, worker_id, title, content, done], db_file)
        return task

    @staticmethod 
    def modificate_task(id, worker_id, title, content, done, db_file):
        DatabaseFunctions.update_register('tasks', ['worker_id','title', 'content', 'done'], [worker_id, title, content, done, id], db_file)
        return Tasks.search_task(id, db_file)

    @staticmethod
    def remove_task(id, db_file):
        task = Tasks.search_task(id, db_file)
        DatabaseFunctions.delete_register('tasks', id, db_file)
        return task

    @staticmethod
    def remove_all_task(db_file):
        DatabaseFunctions.remove_all_registers('tasks', db_file)