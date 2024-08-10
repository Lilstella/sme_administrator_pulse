import unittest
import os
from copy import copy
from tempfile import NamedTemporaryFile
from Functions.models import Clients, Client, Sales, Sale, Workers, Worker, Expenses, Expense, Tasks

class TestModelClient(unittest.TestCase):
    def setUp(self):
        self.test_db_file = NamedTemporaryFile(delete=False)
        self.db_file_name = self.test_db_file.name
        self.test_db_file.close()
        Clients.create_table_client(self.db_file_name)
        Clients.add_client('ABCDE-1', 'John', 'Doe', 'M', 30, 'tr@gmail.com', self.db_file_name)
        Clients.add_client('XYZ00-2', 'Alice', 'Smith', 'F', 25, 'y@gmail.com', self.db_file_name)
        Clients.add_client('12345-3', 'Michael', 'Johnson', 'M', 40, 'urs@gmail.com', self.db_file_name)

    def tearDown(self):
        try:
            os.remove(self.db_file_name)
        except PermissionError:
            pass

    def test_search_client(self):
        true_client = Clients.search_client('ABCDE-1', self.db_file_name)
        false_client = Clients.search_client('00000-0', self.db_file_name)
        self.assertIsNotNone(true_client)
        self.assertIsNone(false_client)

    def test_add_client(self):
        previous_list_client = copy(Clients.load_clients(self.db_file_name))
        new_client = Clients.add_client('PLG00-H', 'Marie', 'Curie', 'F', 40, 'l@gmail.com', self.db_file_name)
        new_list_clients = Clients.load_clients(self.db_file_name)
        new_client_in_db = Clients.search_client('PLG00-H', self.db_file_name)
        diferrence_totals = len(new_list_clients) - len(previous_list_client)
        self.assertEqual(diferrence_totals, 1)
        self.assertEqual(new_client.id, 'PLG00-H')
        self.assertEqual(new_client.name, 'Marie')
        self.assertEqual(new_client.surname, 'Curie')
        self.assertEqual(new_client.gender, 'F')
        self.assertEqual(new_client.age, 40)
        self.assertEqual(new_client.name, new_client_in_db.name)

    def test_modificate_client(self):
        client_to_modificate = copy(Clients.search_client('XYZ00-2', self.db_file_name))
        modificated_client = Clients.modificate_client('XYZ00-2', 'Charlotte', 'Smith', 'F', 25, 'sa@gmail.com', self.db_file_name)
        new_client = Clients.search_client('XYZ00-2', self.db_file_name)
        self.assertEqual(client_to_modificate.name, 'Alice')
        self.assertEqual(modificated_client.name, 'Charlotte')
        self.assertEqual(new_client.name, 'Charlotte')

    def test_remove_client(self):
        previous_list_clients = copy(Clients.load_clients(self.db_file_name))
        removed_client = Clients.remove_client('12345-3', self.db_file_name)
        search_removed_client = Clients.search_client('12345-3', self.db_file_name)
        difference_totals = len(previous_list_clients) - len(Clients.load_clients(self.db_file_name))
        self.assertEqual(removed_client.id, '12345-3')
        self.assertIsNone(search_removed_client)
        self.assertEqual(difference_totals, 1)

    def test_add_many_clients(self):
        previous_list_clients = copy(Clients.load_clients(self.db_file_name))
        list_of_new_clients = [Client('DEFGH-4', 'Emily', 'Brown', 'F', 35, 'cde@gmail.com'),
                            Client('45678-A', 'James', 'Williams', 'M', 28, 'efvg@gmail.com')]
        Clients.add_many_clients(list_of_new_clients, self.db_file_name)
        difference_totals = len(Clients.load_clients(self.db_file_name)) - len(previous_list_clients)
        self.assertEqual(difference_totals, 2)

    def test_remove_all_clients(self):
        Clients.remove_all_clients(self.db_file_name)
        new_register = Clients.load_clients(self.db_file_name)
        empty_list = len(new_register)
        self.assertEqual(empty_list, 0)

class TestModelSale(unittest.TestCase):
    def setUp(self):
        self.test_db_file = NamedTemporaryFile(delete=False)
        self.db_file_name = self.test_db_file.name
        self.test_db_file.close()
        Sales.create_table_sale(self.db_file_name)
        Clients.create_table_client(self.db_file_name)
        Clients.add_client('NJ876-9', 'John', 'Doe', 'M', 30, 'as@gmail.com', self.db_file_name)
        Sales.add_sale('KJHKKHJL7', 'NJ876-9', '2024-05-10 21:30:00', 150, 1, 1, 'X5 Pasta Bolognese Combo', self.db_file_name)
        Sales.add_sale('KLLLQJJJ1', 'NJ876-9', '2024-01-01 12:00:00', 50, 0, 1, 'X1 Large Neapolitan Pizza & X1 Large Jam Pizza', self.db_file_name)
        Sales.add_sale('GFGTTTGL7', 'NJ876-9', '2024-02-04 12:30:00', 10, 0, 0, 'X1 Caprese Salad', self.db_file_name)

    def tearDown(self):
        try:
            os.remove(self.db_file_name)
        except PermissionError:
            pass

    def test_search_sale(self):
        true_sale = Sales.search_sale('KJHKKHJL7', self.db_file_name)
        false_sale = Sales.search_sale('JGJJQJJQ0', self.db_file_name)
        self.assertIsNotNone(true_sale)
        self.assertIsNone(false_sale)

    def test_add_sale(self):
        previous_list_sale = copy(Sales.load_sales(self.db_file_name))
        new_sale = Sales.add_sale('DFFJDDDJ8', 'NJ876-9', '27/01/2024', 400, 0, 0, 'X3 Large Sicilian Pizza & X1 Tignanello Bottle', self.db_file_name)
        new_sale_in_db = Sales.search_sale('DFFJDDDJ8', self.db_file_name)
        new_list_sale = Sales.load_sales(self.db_file_name)
        difference_totals = len(new_list_sale) - len(previous_list_sale)
        self.assertEqual(difference_totals, 1)
        self.assertEqual(new_sale.id, 'DFFJDDDJ8')
        self.assertEqual(new_sale.client_id, 'NJ876-9')
        self.assertEqual(new_sale.date, '27/01/2024')
        self.assertEqual(new_sale.cash, 400)
        self.assertEqual(new_sale.paid, 0)
        self.assertEqual(new_sale.delivered, 0)
        self.assertEqual(new_sale.cash, new_sale_in_db.cash)

    def test_modificate_sale(self):
        sale_to_modificate = copy(Sales.search_sale('KLLLQJJJ1', self.db_file_name))
        modificated_sale = Sales.modificate_sale('KLLLQJJJ1', 25, 1, 0, 'X1 Large Jam Pizza', self.db_file_name)
        new_sale = Sales.search_sale('KLLLQJJJ1', self.db_file_name)
        self.assertEqual(sale_to_modificate.cash, 50)
        self.assertEqual(modificated_sale.cash, 25)
        self.assertEqual(new_sale.cash, 25)

    def test_remove_sale(self):
        previous_list_sales = copy(Sales.load_sales(self.db_file_name))
        removed_sale = Sales.remove_sale('GFGTTTGL7', self.db_file_name)
        search_removed_sale = Sales.search_sale('GFGTTTGL7', self.db_file_name)
        difference_totals = len(previous_list_sales) - len(Sales.load_sales(self.db_file_name))
        self.assertEqual(removed_sale.id, 'GFGTTTGL7')
        self.assertIsNone(search_removed_sale)
        self.assertEqual(difference_totals, 1)

    def test_add_many_sales(self):
        previous_list_sales = copy(Sales.load_sales(self.db_file_name))
        list_of_new_sales = [Sale('QEYQQJQQ5', 'NJ876-9', '12/07/2023', 90, 1, 1, 'X1 Gnocchi Arrabbiata & X1 Ossobuco'),
                            Sale('NJJLJNJL7', 'NJ876-9', '12/07/2023', 23, 0, 0, 'X1 Castagnaccio & X1 Ristretto')]
        Sales.add_many_sales(list_of_new_sales, self.db_file_name)
        difference_totals = len(Sales.load_sales(self.db_file_name)) - len(previous_list_sales)
        self.assertEqual(difference_totals, 2)

    def test_remove_all_sales(self):
        Sales.remove_all_sales(self.db_file_name)
        new_register = Sales.load_sales(self.db_file_name)
        empty_list = len(new_register)
        self.assertEqual(empty_list, 0)

class TestModelWoker(unittest.TestCase):
    def setUp(self):
        self.test_db_file = NamedTemporaryFile(delete=False)
        self.db_file_name = self.test_db_file.name
        self.test_db_file.close()
        Workers.create_table_worker(self.db_file_name)
        Workers.add_worker('OPL55-5', 'Carlos', 'Quintero', 'Cashier', 550, 'plm@gmail.com', self.db_file_name)
        Workers.add_worker('30111-J', 'Nerea', 'Linares', 'Waitress', 750, 'yt@gmail.com', self.db_file_name)

    def tearDown(self):
        try:
            os.remove(self.db_file_name)
        except PermissionError:
            pass

    def test_search_worker(self):
        true_worker = Workers.search_worker('OPL55-5', self.db_file_name)
        false_worker = Workers.search_worker('00000-0', self.db_file_name)
        self.assertIsNotNone(true_worker)
        self.assertIsNone(false_worker)

    def test_add_worker(self):
        previous_list_worker = copy(Workers.load_workers(self.db_file_name))
        new_worker = Workers.add_worker('C4004-0', 'Crystal', 'Moreno', 'Manager', 1500, 'oe@gmail.com', self.db_file_name)
        new_list_workers = Workers.load_workers(self.db_file_name)
        new_worker_in_db = Workers.search_worker('C4004-0', self.db_file_name)
        difference_totals = len(new_list_workers) - len(previous_list_worker)
        self.assertEqual(difference_totals, 1)
        self.assertEqual(new_worker.id, 'C4004-0')
        self.assertEqual(new_worker.name, 'Crystal')
        self.assertEqual(new_worker.surname, 'Moreno')
        self.assertEqual(new_worker.position, 'Manager')
        self.assertEqual(new_worker.salary, 1500)
        self.assertEqual(new_worker.name, new_worker_in_db.name)

    def test_modificate_worker(self):
        worker_to_modificate = copy(Workers.search_worker('30111-J', self.db_file_name))
        modificated_client = Workers.modificate_worker('30111-J', 'Maria', 'Linares', 'Waitress', 750, 'res@gmail.com', self.db_file_name)
        new_worker = Workers.search_worker('30111-J', self.db_file_name)
        self.assertEqual(worker_to_modificate.name, 'Nerea')
        self.assertEqual(modificated_client.name, 'Maria')
        self.assertEqual(new_worker.name, 'Maria')

    def test_remove_worker(self):
        previous_list_workers = copy(Workers.load_workers(self.db_file_name))
        removed_worker = Workers.remove_worker('30111-J', self.db_file_name)
        search_removed_worked = Workers.search_worker('30111-J', self.db_file_name)
        difference_totals = len(previous_list_workers) - len(Workers.load_workers(self.db_file_name))
        self.assertEqual(removed_worker.id, '30111-J', self.db_file_name)
        self.assertIsNone(search_removed_worked)
        self.assertEqual(difference_totals, 1)

    def test_add_many_workers(self):
        previous_list_workers = copy(Workers.load_workers(self.db_file_name))
        list_of_new_workers = [Worker('WARRR-0', 'Tyron', 'Valenzuela', 'Chef', 1500, 'pyg@gmail.com'), 
                            Worker('PAZZZ-0', 'Jenny', 'Rauch', 'Kitchen assistant', 200, 'ytd@gmail.com')]
        Workers.add_many_workers(list_of_new_workers, self.db_file_name)
        difference_totals = len(Workers.load_workers(self.db_file_name)) - len(previous_list_workers)
        self.assertEqual(difference_totals, 2)
        
    def test_remove_all_workers(self):
        Workers.remove_all_workers(self.db_file_name)
        new_register = Workers.load_workers(self.db_file_name)
        empty_list = len(new_register)
        self.assertEqual(empty_list, 0)

class TestModelExpense(unittest.TestCase):
    def setUp(self):
        self.test_db_file = NamedTemporaryFile(delete=False)
        self.db_file_name = self.test_db_file.name
        self.test_db_file.close()
        Expenses.create_table_expense(self.db_file_name)
        Workers.create_table_worker(self.db_file_name)
        Workers.add_worker('IUI00-0', 'Marco', 'Polo', 'Waiter', 21, 'jdsjdjs@gmail.com', self.db_file_name)
        Expenses.add_expense('QUJJQLJU4', 'IUI00-0', '2021-10-12 08:21:00', 500, 1, 'Salary of Marco', self.db_file_name)
        Expenses.add_expense('TLJTTJTT6', None, '2008-02-03 20:21:00', 30, 0, 'Recompose a client', self.db_file_name)

    def tearDown(self):
        try:
            os.remove(self.db_file_name)
        except PermissionError:
            pass

    def test_search_expense(self):
        true_expense = Expenses.search_expense('QUJJQLJU4', self.db_file_name)
        false_expense = Expenses.search_expense('AJAJAJAJA1', self.db_file_name)
        self.assertIsNotNone(true_expense)
        self.assertIsNone(false_expense)

    def test_add_expense(self):
        previous_list_expense = copy(Expenses.load_expenses(self.db_file_name))
        new_expense = Expenses.add_expense('RJIJIJIR9', None, '2023-12-01 10:30:00', 5000, 1, 'Pay bills', self.db_file_name)
        new_expense_in_db = Expenses.search_expense('RJIJIJIR9', self.db_file_name)
        new_list_expense = Expenses.load_expenses(self.db_file_name)
        difference_totals = len(new_list_expense) - len(previous_list_expense)
        self.assertEqual(difference_totals, 1)
        self.assertEqual(new_expense.id, 'RJIJIJIR9')
        self.assertEqual(new_expense.worker_id, None)
        self.assertEqual(new_expense.date, '2023-12-01 10:30:00')
        self.assertEqual(new_expense.cash, 5000)
        self.assertEqual(new_expense.paid, 1)
        self.assertEqual(new_expense.cash, new_expense_in_db.cash)

    def test_modificate_expense(self):
        expense_to_modificate = copy(Expenses.search_expense('TLJTTJTT6', self.db_file_name))
        modificated_expense = Expenses.modificate_expense('TLJTTJTT6', '2021-10-12 08:21:00', 600, 1, 'Salary of Marco', self.db_file_name)
        new_expense = Expenses.search_expense('TLJTTJTT6', self.db_file_name)
        self.assertEqual(expense_to_modificate.cash, 30)
        self.assertEqual(modificated_expense.cash, 600)
        self.assertEqual(new_expense.cash, 600)

    def test_remove_expense(self):
        previous_list_expense = copy(Expenses.load_expenses(self.db_file_name))
        removed_expense = Expenses.remove_expense('TLJTTJTT6', self.db_file_name)
        searc_removed_expense = Expenses.search_expense('TLJTTJTT6', self.db_file_name)
        difference_totals = len(previous_list_expense) - len(Expenses.load_expenses(self.db_file_name))
        self.assertEqual(removed_expense.id, 'TLJTTJTT6')
        self.assertIsNone(searc_removed_expense)
        self.assertEqual(difference_totals, 1)

    def test_add_many_expenses(self):
        previous_list_expenses = copy(Expenses.load_expenses(self.db_file_name))
        list_of_new_expenses = [Expense('EJJELJEJ2', None, '2019-09-23 10:05:00', 81, 0, 'Replenish ingredients'),
                                Expense('GNGGVGTG1', None, '2019-10-23 10:05:00', 100, 0, 'Buy utensils')]
        Expenses.add_many_expenses(list_of_new_expenses, self.db_file_name)
        difference_totals = len(Expenses.load_expenses(self.db_file_name)) - len(previous_list_expenses)
        self.assertEqual(difference_totals, 2)

    def test_remove_all_expenses(self):
        Expenses.remove_all_expenses(self.db_file_name)
        new_register = Expenses.load_expenses(self.db_file_name)
        empty_list = len(new_register)
        self.assertEqual(empty_list, 0)

class TestModelTask(unittest.TestCase):
    def setUp(self):
        self.test_db_file = NamedTemporaryFile(delete=False)
        self.db_file_name = self.test_db_file.name
        self.test_db_file.close()
        Tasks.create_table_task(self.db_file_name)
        Workers.create_table_worker(self.db_file_name)
        Workers.add_worker('IUI00-0', 'Marco', 'Polo', 'Waiter', 21, 'jdsjdjs@gmail.com', self.db_file_name)
        Tasks.add_task('66666661D', 'IUI00-0', 'clean dishes', 'blablabla', 0, self.db_file_name)

    def tearDown(self):
        try:
            os.remove(self.db_file_name)
        except PermissionError:
            pass

    def test_search_task(self):
        true_task = Tasks.search_task('66666661D', self.db_file_name)
        false_task = Tasks.search_task('71717071H', self.db_file_name)

        self.assertEqual(true_task.id, '66666661D')
        self.assertEqual(true_task.worker_id, 'IUI00-0')
        self.assertEqual(true_task.title, 'clean dishes')
        self.assertEqual(true_task.content, 'blablabla')
        self.assertEqual(true_task.done, 0)
        self.assertIsNone(false_task)

    def test_add_task(self):
        previous_list_task = copy(Tasks.load_tasks(self.db_file_name))
        new_task = Tasks.add_task('51056551P', None, 'Cook', 'blabla', 1, self.db_file_name)
        new_task_in_db = Tasks.search_task('51056551P', self.db_file_name)
        new_list_task = Tasks.load_tasks(self.db_file_name)
        difference_totals = len(new_list_task) - len(previous_list_task)
        self.assertEqual(difference_totals, 1)
        self.assertEqual(new_task.id, '51056551P')
        self.assertEqual(new_task.worker_id, None)
        self.assertEqual(new_task.title, 'Cook')
        self.assertEqual(new_task.content, 'blabla')
        self.assertEqual(new_task.done, 1)
        self.assertEqual(new_task.title, new_task_in_db.title)

    def test_modificate_task(self):
        task_to_modificate = copy(Tasks.search_task('66666661D', self.db_file_name))
        modificated_task = Tasks.modificate_task('66666661D', None, 'Cook', 'blabla', 1, self.db_file_name)
        new_task = Tasks.search_task('66666661D', self.db_file_name)
        self.assertEqual(task_to_modificate.content, 'blablabla')
        self.assertEqual(modificated_task.content, 'blabla')
        self.assertEqual(new_task.content, 'blabla')

    def test_remove_task(self):
        previous_list_task = copy(Tasks.load_tasks(self.db_file_name))
        removed_task = Tasks.remove_task('66666661D', self.db_file_name)
        search_removed_task = Tasks.search_task('66666661D', self.db_file_name)
        difference_totals = len(previous_list_task) - len(Tasks.load_tasks(self.db_file_name))
        self.assertEqual(removed_task.id, '66666661D')
        self.assertIsNone(search_removed_task)
        self.assertEqual(difference_totals, 1)

    def test_remove_all_tasks(self):
        Tasks.remove_all_task(self.db_file_name)
        new_register = Tasks.load_tasks(self.db_file_name)
        empty_list = len(new_register)
        self.assertEqual(empty_list, 0)