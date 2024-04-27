from copy import copy
import unittest
from Functions.models import Client, Clients
from Functions.Auxiliars import valid_id as vid, date as dt
from Functions.Auxiliars.database import DatabaseFunctions

class TestDatabase(unittest.TestCase):
    def setUp(self):
        DatabaseFunctions.create_tables('1')
        Clients.add_client('ABC-1', 'John', 'Doe', 'M', 30)
        Clients.add_client('XYZ-2', 'Alice', 'Smith', 'F', 25)
        Clients.add_client('123-3', 'Michael', 'Johnson', 'M', 40)

    def test_search_client(self):
        true_client = Clients.search_client('ABC-1')
        false_client = Clients.search_client('000-0')
        self.assertIsNotNone(true_client)
        self.assertIsNone(false_client)

    def test_add_client(self):
        previous_list_client = Clients.load_clients().copy()
        new_client = Clients.add_client('PLG-H', 'Marie', 'Curie', 'F', 40)
        new_list_clients = Clients.load_clients()
        diferrence_totals = len(new_list_clients) - len(previous_list_client)
        self.assertEqual(diferrence_totals, 1)
        self.assertEqual(new_client.id, 'PLG-H')
        self.assertEqual(new_client.name, 'Marie')
        self.assertEqual(new_client.surname, 'Curie')
        self.assertEqual(new_client.gender, 'F')
        self.assertEqual(new_client.age, 40)

    def test_modificate_client(self):
        client_to_modificate = copy(Clients.search_client('XYZ-2'))
        modificated_client = Clients.modificate_client('XYZ-2', 'Charlotte', 'Smith', 'F', 25)
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
        list_of_new_clients = [Client('DEF-4', 'Emily', 'Brown', 'F', 35),
                               Client('456-A', 'James', 'Williams', 'M', 28)]
        Clients.add_many_clients(list_of_new_clients)
        difference_totals = len(Clients.load_clients()) - len(previous_list_clients)
        self.assertEqual(difference_totals, 2)

    def test_valid_id(self):
        list_clients = Clients.load_clients()
        self.assertTrue(vid.valid_id('34W-W', list_clients))
        self.assertFalse(vid.valid_id('75480', list_clients))
        self.assertFalse(vid.valid_id('04G-a', list_clients))
        self.assertFalse(vid.valid_id('5t6-y', list_clients))
        self.assertFalse(vid.valid_id('ABC-1', list_clients))

    def test_remove_all_clients(self):
        Clients.remove_all_clients()
        new_register = Clients.load_clients()
        empty_list = len(new_register)
        self.assertEqual(empty_list, 0)

    def test_date(self):
        #test done in 27/04/2024
        today = dt.date()
        self.assertEqual(today, '27/04/2024')