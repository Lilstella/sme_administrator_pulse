import unittest
import os
from tempfile import NamedTemporaryFile
from Functions.models import Clients, Sales, Workers, Expenses
from Functions.Auxiliars.valid_id import valid_id

class TestAuxiliars(unittest.TestCase):
    def setUp(self):
        self.test_db_file = NamedTemporaryFile(delete=False)
        self.db_file_name = self.test_db_file.name
        self.test_db_file.close()

        Clients.create_table_client(self.db_file_name)
        Clients.add_client('AB7DE-1', 'John', 'Doe', 'M', 30, 'tr@gmail.com', self.db_file_name)

        Sales.create_table_sale(self.db_file_name)
        Sales.add_sale('00000876L', None, '2024-06-20 21:15:00', 80, 1, 1, 'X5 Pasta Bolognese Combo', self.db_file_name)

        Workers.create_table_worker(self.db_file_name)
        Workers.add_worker('OPL67-5', 'Carlos', 'Quintero', 'Cashier', 550, 'plm@gmail.com', self.db_file_name)

        Expenses.create_table_expense(self.db_file_name)
        Expenses.add_expense('98052000B', None, '2008-02-03 20:21:00', 30, 0, 'Recompose a client', self.db_file_name)

    def tearDown(self):
        try:
            os.remove(self.db_file_name)
        except PermissionError:
            pass

    def test_valid_id(self):
        list_clients = Clients.load_clients(self.db_file_name)
        list_sales = Sales.load_sales(self.db_file_name)
        list_workers = Workers.load_workers(self.db_file_name)
        list_expenses = Expenses.load_expenses(self.db_file_name)

        self.assertTrue(valid_id('3456W-W', list_clients, 'client_id_pattern'))
        self.assertFalse(valid_id('75480', list_clients, 'client_id_pattern'))
        self.assertFalse(valid_id('04G5s-a', list_clients, 'client_id_pattern'))
        self.assertFalse(valid_id('AB7DE-1', list_clients, 'client_id_pattern'))

        self.assertTrue(valid_id('00000719J', list_sales, 'sale_id_pattern'))
        self.assertFalse(valid_id('6676U650K', list_sales, 'sale_id_pattern'))
        self.assertFalse(valid_id('3180M', list_sales, 'sale_id_pattern'))
        self.assertFalse(valid_id('00000876L', list_sales, 'sale_id_pattern'))

        self.assertTrue(valid_id('00004-Y', list_workers, 'worker_id_pattern'))
        self.assertFalse(valid_id('870000', list_workers, 'worker_id_pattern'))
        self.assertFalse(valid_id('a0Fj5-0', list_workers, 'worker_id_pattern'))
        self.assertFalse(valid_id('OPL67-5', list_workers, 'worker_id_pattern'))

        self.assertTrue(valid_id('88911000F', list_expenses, 'expense_id_pattern'))
        self.assertFalse(valid_id('992YT890L', list_expenses, 'expense_id_pattern'))
        self.assertFalse(valid_id('8600H', list_expenses, 'expense_id_pattern'))
        self.assertFalse(valid_id('98052000B', list_expenses, 'expense_id_pattern'))