import pandas as pd
from Functions.models import Clients, Client, Sales, Sale, Workers, Worker, Expenses, Expense

class SaveAllInExcel:
    @staticmethod
    def save_all_clients_in_excel(excel_file, db_file):
        clients = Clients.load_clients(db_file)
        clients_data = [{'id': client.id, 'name': client.name, 'surname': client.surname, 'gender': client.gender, 'age': client.age, 'mail': client.mail} for client in clients]
        clients_columns = ['id', 'name', 'surname', 'gender', 'age', 'mail']

        df = pd.DataFrame(clients_data, columns=clients_columns)
        df.to_excel(excel_file, sheet_name='Clients', index=False, engine='openpyxl')

    @staticmethod
    def save_all_sales_in_excel(excel_file, db_file):
        sales = Sales.load_sales(db_file)
        sales_data = [{'id': sale.id, 'client_id': sale.client_id, 'date': sale.date, 'cash': sale.cash, 'transaction_state': sale.transaction_state, 'service_state': sale.service_state, 'description': sale.description} for sale in sales]
        sales_columns = ['id', 'client_id', 'date', 'cash', 'transaction_state', 'service_state', 'description']

        df = pd.DataFrame(sales_data, columns=sales_columns)
        df.to_excel(excel_file, sheet_name='Sales', index=False, engine='openpyxl')

    @staticmethod
    def save_all_workers_in_excel(excel_file, db_file):
        workers = Workers.load_workers(db_file)
        workers_data = [{'id': worker.id, 'name': worker.name, 'surname': worker.surname, 'position': worker.position, 'salary': worker.salary, 'mail': worker.mail} for worker in workers]
        workers_columns = ['id', 'name', 'surname', 'position', 'salary', 'mail']

        df = pd.DataFrame(workers_data, columns=workers_columns)
        df.to_excel(excel_file, sheet_name='Workers', index=False, engine='openpyxl')

    @staticmethod
    def save_all_expenses_in_excel(excel_file, db_file):
        expenses = Expenses.load_expenses(db_file)
        expenses_data = [{'id': expense.id, 'worker_id': expense.worker_id, 'date': expense.date, 'cash': expense.cash, 'transaction_state': expense.transaction_state, 'description': expense.description} for expense in expenses]
        expenses_columns = ['id', 'worker_id', 'date', 'cash', 'transaction_state', 'description']

        df = pd.DataFrame(expenses_data, columns=expenses_columns)
        df.to_excel(excel_file, sheet_name='Expenses', index=False, engine='openpyxl')

    @staticmethod
    def save_all_elements_in_excel(excel_file, db_file):
        with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
            SaveAllInExcel.save_all_clients_in_excel(writer, db_file)
            SaveAllInExcel.save_all_sales_in_excel(writer, db_file)
            SaveAllInExcel.save_all_workers_in_excel(writer, db_file)
            SaveAllInExcel.save_all_expenses_in_excel(writer, db_file)

class LoadAllFromTable:
    @staticmethod
    def load_clients_from_excel(excel_file):
        df = pd.read_excel(excel_file, sheet_name='Clients', engine='openpyxl')
        df = df.map(lambda value: None if pd.isna(value) else value)
        clients = [Client(row.id, row.name, row.surname, row.gender, row.age, row.mail) for row in df.itertuples(index=False)]

        return clients

    @staticmethod
    def load_sales_from_excel(excel_file):
        df = pd.read_excel(excel_file, sheet_name='Sales', engine='openpyxl')
        df = df.map(lambda value: None if pd.isna(value) else value)
        sales = [Sale(row.id, row.client_id, row.date, row.cash, row.transaction_state, row.service_state, row.description) for row in df.itertuples(index=False)]

        return sales

    @staticmethod
    def load_workers_from_excel(excel_file):
        df = pd.read_excel(excel_file, sheet_name='Workers', engine='openpyxl')
        df = df.map(lambda value: None if pd.isna(value) else value)
        workers = [Worker(row.id, row.name, row.surname, row.position, row.salary, row.mail) for row in df.itertuples(index=False)]

        return workers

    @staticmethod
    def load_expenses_from_excel(excel_file):
        df = pd.read_excel(excel_file, sheet_name='Expenses', engine='openpyxl')
        df = df.map(lambda value: None if pd.isna(value) else value)
        expenses = [Expense(row.id, row.worker_id, row.date, row.cash, row.transaction_state, row.description) for row in df.itertuples(index=False)]

        return expenses

    @staticmethod
    def load_all_from_excel(excel_file):
        clients = LoadAllFromTable.load_clients_from_excel(excel_file)
        sales = LoadAllFromTable.load_sales_from_excel(excel_file)
        workers = LoadAllFromTable.load_workers_from_excel(excel_file)
        expenses = LoadAllFromTable.load_expenses_from_excel(excel_file)

        return clients, sales, workers, expenses

class SaveOneInExcel:
    @staticmethod
    def save_client_in_excel(excel_file, client):
        total_clients_in_excel = LoadAllFromTable.load_clients_from_excel(excel_file)
        data_client = {'id': client.id, 'name': client.name, 'surname': client.surname, 'gender': client.gender, 'age': client.age, 'mail': client.mail}
        total_clients_in_excel.append(data_client)
        clients_columns = ['id', 'name', 'surname', 'gender', 'age', 'mail']

        total_clients_for_data = pd.DataFrame(total_clients_in_excel, columns=clients_columns)
        total_clients_for_data.to_excel(excel_file, sheet_name='Clients', index=False, engine='openpyxl')

    @staticmethod
    def save_sale_in_excel(excel_file, sale):
        total_sales_in_excel = LoadAllFromTable.load_sales_from_excel(excel_file)
        data_sale = {'id': sale.id, 'client_id': sale.client_id, 'date': sale.date, 'cash': sale.cash, 'transaction_state': sale.transaction_state, 'service_state': sale.service_state, 'description': sale.description}
        total_sales_in_excel.append(data_sale)
        sales_columns = ['id', 'client_id', 'date', 'cash', 'transaction_state', 'service_state', 'description']

        total_sales_for_data = pd.DataFrame(total_sales_in_excel, columns=sales_columns)
        total_sales_for_data.to_excel(excel_file, sheet_name='Sales', index=False, engine='openpyxl')

    @staticmethod
    def save_worker_in_excel(excel_file, worker):
        total_workers_in_excel = LoadAllFromTable.load_workers_from_excel(excel_file)
        data_worker = {'id': worker.id, 'name': worker.name, 'surname': worker.surname, 'position': worker.position, 'salary': worker.salary, 'mail': worker.mail}
        total_workers_in_excel.append(data_worker)
        workers_columns = ['id', 'name', 'surname', 'position', 'salary', 'mail']

        total_workers_for_data = pd.DataFrame(total_workers_in_excel, columns=workers_columns)
        total_workers_for_data.to_excel(excel_file, sheet_name='Workers', index=False, engine='openpyxl')

    @staticmethod
    def save_expense_in_excel(excel_file, expense):
        total_expenses_in_excel = LoadAllFromTable.load_expenses_from_excel(excel_file)
        data_expense = {'id': expense.id, 'worker_id': expense.worker_id, 'date': expense.date, 'cash': expense.cash, 'transaction_state': expense.transaction_state, 'description': expense.description}
        total_expenses_in_excel.append(data_expense)
        expenses_columns = ['id', 'worker_id', 'date', 'cash', 'transaction_state', 'description']

        total_expenses_for_data = pd.DataFrame(total_expenses_in_excel, columns=expenses_columns)
        total_expenses_for_data.to_excel(excel_file, sheet_name='Expenses', index=False, engine='openpyxl')