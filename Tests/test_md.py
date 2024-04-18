from copy import copy
import unittest
from Functions import models as md
from Functions.Auxiliars import valid_id as vid
from Functions.Auxiliars import date as dt

class TestDatabase(unittest.TestCase):
    def setUp(self):
        md.Clients.list_clients = [
            md.Client('ABC-1', 'John', 'Doe', 'M', 30),
            md.Client('XYZ-2', 'Alice', 'Smith', 'F', 25),
            md.Client('123-3', 'Michael', 'Johnson', 'M', 40),
        ]

    def test_search_client(self):
        true_client = md.Clients.search_client('ABC-1')
        false_client = md.Clients.search_client('000-0')
        self.assertIsNotNone(true_client)
        self.assertIsNone(false_client)

    def test_add_client(self):
        previous_list_client = copy(md.Clients.list_clients)
        new_client = md.Clients.add_client('PLG-H', 'Marie', 'Curie', 'F', 40)
        diferrence_totals = len(md.Clients.list_clients) - len(previous_list_client)
        self.assertEqual(diferrence_totals, 1)
        self.assertEqual(new_client.id, 'PLG-H')
        self.assertEqual(new_client.name, 'Marie')
        self.assertEqual(new_client.surname, 'Curie')
        self.assertEqual(new_client.gender, 'F')
        self.assertEqual(new_client.age, 40)

    def test_modificate_client(self):
        client_to_modificate = copy(md.Clients.search_client('XYZ-2'))
        modificated_client = md.Clients.modificate_client('XYZ-2', 'Charlotte', 'Smith', 'F', 25)
        self.assertEqual(client_to_modificate.name, 'Alice')
        self.assertEqual(modificated_client.name, 'Charlotte')

    def test_remove_client(self):
        previous_list_clients = copy(md.Clients.list_clients)
        removed_client = md.Clients.remove_client('123-3')
        search_removed_client = md.Clients.search_client('123-3')
        difference_totals = len(previous_list_clients) - len(md.Clients.list_clients)
        self.assertEqual(removed_client.id, '123-3')
        self.assertIsNone(search_removed_client)
        self.assertEqual(difference_totals, 1)

    def test_add_many_clients(self):
        previous_list_clients = copy(md.Clients.list_clients)
        list_of_new_clients = [("DEF-4", "Emily", "Brown", "Female", 35),
                               ("456-A", "James", "Williams", "Male", 28)]
        md.Clients.add_many_clients(list_of_new_clients)
        difference_totals = len(md.Clients.list_clients) - len(previous_list_clients)
        self.assertEqual(difference_totals, 2)

    def test_valid_id(self):
        self.assertTrue(vid.valid_id('34W-W', md.Clients.list_clients))
        self.assertFalse(vid.valid_id('75480', md.Clients.list_clients))
        self.assertFalse(vid.valid_id('04G-a', md.Clients.list_clients))
        self.assertFalse(vid.valid_id('5t6-y', md.Clients.list_clients))
        self.assertFalse(vid.valid_id('ABC-1', md.Clients.list_clients))

    def test_remove_all_clients(self):
        md.Clients.remove_all_clients()
        empty_list = len(md.Clients.list_clients)
        self.assertEqual(empty_list, 0)

    def test_date(self):
        #test done in 17/04/2024
        today = dt.date()
        self.assertEqual(today, '17/04/2024')