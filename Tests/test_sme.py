from copy import copy
import unittest
from Functions.models import *
from Functions.Auxiliars import valid_id as vid, date as dt
from Functions.Auxiliars.database import DatabaseFunctions

class TestModels:
    class TestModelClient(unittest.TestCase):
        def setUp(self):
            DatabaseFunctions.create_tables('1')
            Clients.add_client('ABC-1', 'John', 'Doe', 'Male', 30, 'tr@gmail.com')
            Clients.add_client('XYZ-2', 'Alice', 'Smith', 'Female', 25, 'y@gmail.com')
            Clients.add_client('123-3', 'Michael', 'Johnson', 'Male', 40, 'urs@gmail.com')

        def test_search_client(self):
            true_client = Clients.search_client('ABC-1')
            false_client = Clients.search_client('000-0')
            self.assertIsNotNone(true_client)
            self.assertIsNone(false_client)

        def test_add_client(self):
            previous_list_client = copy(Clients.load_clients())
            new_client = Clients.add_client('PLG-H', 'Marie', 'Curie', 'Female', 40, 'l@gmail.com')
            new_list_clients = Clients.load_clients()
            new_client_in_db = Clients.search_client('PLG-H')
            diferrence_totals = len(new_list_clients) - len(previous_list_client)
            self.assertEqual(diferrence_totals, 1)
            self.assertEqual(new_client.id, 'PLG-H')
            self.assertEqual(new_client.name, 'Marie')
            self.assertEqual(new_client.surname, 'Curie')
            self.assertEqual(new_client.gender, 'Female')
            self.assertEqual(new_client.age, 40)
            self.assertEqual(new_client.name, new_client_in_db.name)

        def test_modificate_client(self):
            client_to_modificate = copy(Clients.search_client('XYZ-2'))
            modificated_client = Clients.modificate_client('XYZ-2', 'Charlotte', 'Smith', 'Female', 25, 'sa@gmail.com')
            new_client = Clients.search_client('XYZ-2')
            self.assertEqual(client_to_modificate.name, 'Alice')
            self.assertEqual(modificated_client.name, 'Charlotte')
            self.assertEqual(new_client.name, 'Charlotte')

        def test_remove_client(self):
            previous_list_clients = copy(Clients.load_clients())
            removed_client = Clients.remove_client('123-3')
            search_removed_client = Clients.search_client('123-3')
            difference_totals = len(previous_list_clients) - len(Clients.load_clients())
            self.assertEqual(removed_client.id, '123-3')
            self.assertIsNone(search_removed_client)
            self.assertEqual(difference_totals, 1)

        def test_add_many_clients(self):
            previous_list_clients = copy(Clients.load_clients())
            list_of_new_clients = [Client('DEF-4', 'Emily', 'Brown', 'Female', 35, 'cde@gmail.com'),
                                Client('456-A', 'James', 'Williams', 'Male', 28, 'efvg@gmail.com')]
            Clients.add_many_clients(list_of_new_clients)
            difference_totals = len(Clients.load_clients()) - len(previous_list_clients)
            self.assertEqual(difference_totals, 2)

        def test_remove_all_clients(self):
            Clients.remove_all_clients()
            new_register = Clients.load_clients()
            empty_list = len(new_register)
            self.assertEqual(empty_list, 0)

    class TestModelSale(unittest.TestCase):
        def setUp(self):
            DatabaseFunctions.create_tables('2')
            Clients.add_client('NJ8-9', 'John', 'Doe', 'Male', 30, 'as@gmail.com')
            Sales.add_sale('000-1', 'NJ8-9', '2024-05-10 21:30:00', 500, 'completed', 'active')
            Sales.add_sale('7U0-7', 'NJ8-9', '2024-01-01 12:00:00', 50, 'pending', 'active')
            Sales.add_sale('M09-6', 'NJ8-9', '2024-02-04 12:30:00', 1205, 'pending', 'inactive')

        def test_search_sale(self):
            true_sale = Sales.search_sale('M09-6')
            false_sale = Sales.search_sale('333-J')
            self.assertIsNotNone(true_sale)
            self.assertIsNone(false_sale)

        def test_add_sale(self):
            previous_list_sale = copy(Sales.load_sales())
            new_sale = Sales.add_sale('B70-2', 'NJ8-9', '27/01/2024', 400, 'pending', 'inactive')
            new_sale_in_db = Sales.search_sale('B70-2')
            new_list_sale = Sales.load_sales()
            difference_totals = len(new_list_sale) - len(previous_list_sale)
            self.assertEqual(difference_totals, 1)
            self.assertEqual(new_sale.id, 'B70-2')
            self.assertEqual(new_sale.client_id, 'NJ8-9')
            self.assertEqual(new_sale.date, '27/01/2024')
            self.assertEqual(new_sale.cash, 400)
            self.assertEqual(new_sale.transaction_state, 'pending')
            self.assertEqual(new_sale.service_state, 'inactive')
            self.assertEqual(new_sale.cash, new_sale_in_db.cash)

        def test_modificate_sale(self):
            sale_to_modificate = copy(Sales.search_sale('7U0-7'))
            modificated_sale = Sales.modificate_sale('7U0-7', 32, 'completed', 'inactive')
            new_sale = Sales.search_sale('7U0-7')
            self.assertEqual(sale_to_modificate.cash, 50)
            self.assertEqual(modificated_sale.cash, 32)
            self.assertEqual(new_sale.cash, 32)

        def test_remove_sale(self):
            previous_list_sales = copy(Sales.load_sales())
            removed_sale = Sales.remove_sale('000-1')
            search_removed_sale = Sales.search_sale('000-1')
            difference_totals = len(previous_list_sales) - len(Sales.load_sales())
            self.assertEqual(removed_sale.id, '000-1')
            self.assertIsNone(search_removed_sale)
            self.assertEqual(difference_totals, 1)

        def test_many_sales(self):
            previous_list_sales = copy(Sales.load_sales())
            list_of_new_sales = [Sale('65H-Q', 'NJ8-9', '12/07/2023', 90, 'completed', 'active'),
                                Sale('01G-N', 'NJ8-9', '12/07/2023', 23, 'pending', 'inactive')]
            Sales.add_many_sales(list_of_new_sales)
            difference_totals = len(Sales.load_sales()) - len(previous_list_sales)
            self.assertEqual(difference_totals, 2)

        def test_remove_all_sales(self):
            Sales.remove_all_sales()
            new_register = Sales.load_sales()
            empty_list = len(new_register)
            self.assertEqual(empty_list, 0)

    class TestModelWoker(unittest.TestCase):
        def setUp(self):
            DatabaseFunctions.create_tables('3')
            Workers.add_worker('OPL-5', 'Carlos', 'Quintero', 'Cashier', 550, 'plm@gmail.com')
            Workers.add_worker('301-J', 'Nerea', 'Linares', 'Waitress', 750, 'yt@gmail.com')

        def test_search_worker(self):
            true_worker = Workers.search_worker('OPL-5')
            false_worker = Workers.search_worker('000-0')
            self.assertIsNotNone(true_worker)
            self.assertIsNone(false_worker)

        def test_add_worker(self):
            previous_list_worker = copy(Workers.load_workers())
            new_worker = Workers.add_worker('C40-0', 'Crystal', 'Moreno', 'Manager', 1500, 'oe@gmail.com')
            new_list_workers = Workers.load_workers()
            new_worker_in_db = Workers.search_worker('C40-0')
            difference_totals = len(new_list_workers) - len(previous_list_worker)
            self.assertEqual(difference_totals, 1)
            self.assertEqual(new_worker.id, 'C40-0')
            self.assertEqual(new_worker.name, 'Crystal')
            self.assertEqual(new_worker.surname, 'Moreno')
            self.assertEqual(new_worker.position, 'Manager')
            self.assertEqual(new_worker.salary, 1500)
            self.assertEqual(new_worker.name, new_worker_in_db.name)

        def test_modificate_worker(self):
            worker_to_modificate = copy(Workers.search_worker('301-J'))
            modificated_client = Workers.modificate_worker('301-J', 'Maria', 'Linares', 'Waitress', 750, 'res@gmail.com')
            new_worker = Workers.search_worker('301-J')
            self.assertEqual(worker_to_modificate.name, 'Nerea')
            self.assertEqual(modificated_client.name, 'Maria')
            self.assertEqual(new_worker.name, 'Maria')

        def test_remove_worker(self):
            previous_list_workers = copy(Workers.load_workers())
            removed_worker = Workers.remove_worker('301-J')
            search_removed_worked = Workers.search_worker('301-J')
            difference_totals = len(previous_list_workers) - len(Workers.load_workers())
            self.assertEqual(removed_worker.id, '301-J')
            self.assertIsNone(search_removed_worked)
            self.assertEqual(difference_totals, 1)

        def test_add_many_workers(self):
            previous_list_workers = copy(Workers.load_workers())
            list_of_new_workers = [Worker('WAR-0', 'Tyron', 'Valenzuela', 'Chef', 1500, 'pyg@gmail.com'), 
                                   Worker('PAZ-0', 'Jenny', 'Rauch', 'Kitchen assistant', 200, 'ytd@gmail.com')]
            Workers.add_many_workers(list_of_new_workers)
            difference_totals = len(Workers.load_workers()) - len(previous_list_workers)
            self.assertEqual(difference_totals, 2)
            
        def test_remove_all_workers(self):
            Workers.remove_all_workers()
            new_register = Workers.load_workers()
            empty_list = len(new_register)
            self.assertEqual(empty_list, 0)

    class TestModelExpense(unittest.TestCase):
        def setUp(self):
            DatabaseFunctions.create_tables('4')
            Workers.add_worker('KEY-0', 'Marco', 'Polo', 'Waiter', 21, 'jdsjdjs@gmail.com')
            Expenses.add_expense('UIO-2', 'KEY-0', '2021-10-12 08:21:00', 500, 'active', 'Salary of Marco')
            Expenses.add_expense('320-0', None, '2008-02-03 20:21:00', 30, 'inactive', 'Recompose a client')

        def test_search_expense(self):
            true_expense = Expenses.search_expense('UIO-2')
            false_expense = Expenses.search_expense('010-0')
            self.assertIsNotNone(true_expense)
            self.assertIsNone(false_expense)

        def test_add_expense(self):
            previous_list_expense = copy(Expenses.load_expenses())
            new_expense = Expenses.add_expense('T32-0', None, '2023-12-01 10:30:00', 5000, 'active', 'Pay bills')
            new_expense_in_db = Expenses.search_expense('T32-0')
            new_list_expense = Expenses.load_expenses()
            difference_totals = len(new_list_expense) - len(previous_list_expense)
            self.assertEqual(difference_totals, 1)
            self.assertEqual(new_expense.id, 'T32-0')
            self.assertEqual(new_expense.worker_id, None)
            self.assertEqual(new_expense.date, '2023-12-01 10:30:00')
            self.assertEqual(new_expense.cash, 5000)
            self.assertEqual(new_expense.transaction_state, 'active')
            self.assertEqual(new_expense.cash, new_expense_in_db.cash)

        def test_modificate_expense(self):
            expense_to_modificate = copy(Expenses.search_expense('UIO-2'))
            modificated_expense = Expenses.modificate_expense('UIO-2', '2021-10-12 08:21:00', 600, 'active', 'Salary of Marco')
            new_expense = Expenses.search_expense('UIO-2')
            self.assertEqual(expense_to_modificate.cash, 500)
            self.assertEqual(modificated_expense.cash, 600)
            self.assertEqual(new_expense.cash, 600)

        def test_remove_expense(self):
            previous_list_expense = copy(Expenses.load_expenses())
            removed_expense = Expenses.remove_expense('320-0')
            searc_removed_expense = Expenses.search_expense('320-0')
            difference_totals = len(previous_list_expense) - len(Expenses.load_expenses())
            self.assertEqual(removed_expense.id, '320-0')
            self.assertIsNone(searc_removed_expense)
            self.assertEqual(difference_totals, 1)

        def test_many_expenses(self):
            previous_list_expenses = copy(Expenses.load_expenses())
            list_of_new_expenses = [Expense('P20-0', None, '2019-09-23 10:05:00', 81, 'inactive', 'Replenish ingredients'),
                                    Expense('P50-0', None, '2019-10-23 10:05:00', 100, 'inactive', 'Buy utensils')]
            Expenses.add_many_expenses(list_of_new_expenses)
            difference_totals = len(Expenses.load_expenses()) - len(previous_list_expenses)
            self.assertEqual(difference_totals, 2)

        def test_remove_all_expenses(self):
            Expenses.remove_all_expenses()
            new_register = Expenses.load_expenses()
            empty_list = len(new_register)
            self.assertEqual(empty_list, 0)

class TestAuxiliars(unittest.TestCase):
        def test_valid_id(self):
            list_clients = Clients.load_clients()
            self.assertTrue(vid.valid_id('34W-W', list_clients))
            self.assertFalse(vid.valid_id('75480', list_clients))
            self.assertFalse(vid.valid_id('04G-a', list_clients))
            self.assertFalse(vid.valid_id('5t6-y', list_clients))
            self.assertFalse(vid.valid_id('ABC-1', list_clients))

        def test_date(self):
            #test done in 12/05/2024
            today = dt.date()
            self.assertEqual(today, '2024-05-12')