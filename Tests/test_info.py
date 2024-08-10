import unittest
import os
from tempfile import NamedTemporaryFile
from datetime import datetime
from Functions.models import Clients, Sales
from Functions.info import InfoClients, InfoSales

class TestInfoClients(unittest.TestCase):
    def setUp(self):
        self.test_db_file = NamedTemporaryFile(delete=False)
        self.db_file_name = self.test_db_file.name
        self.test_db_file.close()
        Clients.create_table_client(self.db_file_name)
        Sales.create_table_sale(self.db_file_name)
        Clients.add_client('ABCDE-1', 'John', 'Doe', 'M', 30, 'tr@gmail.com', self.db_file_name)
        Clients.add_client('XYZ00-2', 'Alice', 'Smith', 'F', 25, 'y@gmail.com', self.db_file_name)
        Clients.add_client('12345-3', 'Michael', 'Johnson', 'M', 40, 'urs@gmail.com', self.db_file_name)
        Sales.add_sale('KKKEDNFW3', 'ABCDE-1', '2024-05-10 21:30:00', 150, 1, 1, 'X5 Pasta Bolognese Combo', self.db_file_name)
        Sales.add_sale('KVVNFNNV5', '12345-3', '2024-02-01 12:00:00', 50, 0, 1, 'X1 Large Neapolitan Pizza & X1 Large Jam Pizza', self.db_file_name)
        Sales.add_sale('GYYYOOPO7', '12345-3', '2024-02-04 12:30:00', 10, 0, 0, 'X1 Caprese Salad', self.db_file_name)
        Sales.add_sale('HHJJGUHJ9', 'ABCDE-1', '2024-03-15 18:45:00', 200, 1, 1, 'X2 BBQ Chicken Wings Combo', self.db_file_name)
        Sales.add_sale('LLEWQZLL8', '12345-3', '2024-03-20 19:15:00', 75, 0, 1, 'X1 Veggie Delight Pizza', self.db_file_name)
        Sales.add_sale('MOMMAZZZ0', 'ABCDE-1', '2024-04-22 13:50:00', 120, 1, 0, 'X3 Spaghetti Carbonara', self.db_file_name)
        Sales.add_sale('NEEFEDCQ1', '12345-3', '2024-04-11 20:10:00', 60, 0, 1, 'X1 Margherita Pizza', self.db_file_name)
        Sales.add_sale('PPPPEJLJ6', 'ABCDE-1', '2024-05-05 14:25:00', 90, 1, 1, 'X2 Caesar Salad & X2 Garlic Bread', self.db_file_name)
        Sales.add_sale('XYZLXXAZ7', '12345-3', '2024-02-15 14:30:00', 80, 1, 1, 'X2 Pepperoni Pizza', self.db_file_name)
        Sales.add_sale('YTTBJUYY5', '12345-3', '2024-03-09 18:45:00', 50, 1, 1, 'X1 Hawaiian Pizza', self.db_file_name)
        Sales.add_sale('ZXZXZCVA4', '12345-3', '2024-04-23 12:00:00', 70, 1, 1, 'X3 Veggie Pizza', self.db_file_name)
        Sales.add_sale('WTGTHTGW3', '12345-3', '2024-03-14 19:20:00', 90, 1, 1, 'X2 Meat Lovers Pizza', self.db_file_name)
        Sales.add_sale('VVEEVVOK1', '12345-3', '2024-02-28 16:35:00', 65, 0, 1, 'X1 BBQ Chicken Pizza', self.db_file_name)

    def tearDown(self):
        try:
            os.remove(self.db_file_name)
        except PermissionError:
            pass

    def test_gender_of_clients(self):
        gender_of_clients = InfoClients.gender_of_clients(self.db_file_name)
        expected = {'Male': 2, 'Female': 1, 'Other': 0}

        self.assertEqual(gender_of_clients, expected)

    def test_age_of_clients(self):
        age_of_clients = InfoClients.age_of_clients(self.db_file_name)
        expected = {'15-20': 0, '21-25': 1, '26-30': 1, '31-35': 0, '36-40': 1, '41-45': 0, '46+': 0}

        self.assertEqual(age_of_clients, expected)

    def test_client_summary(self):
        client_summary_1 = InfoClients.client_summary('ABCDE-1', self.db_file_name)
        client_summary_2 = InfoClients.client_summary('XYZ00-2', self.db_file_name)
        client_summary_3 = InfoClients.client_summary('12345-3', self.db_file_name)

        id_of_history_1 = set([sale.id for sale in client_summary_1['history']])
        expected_history_ids_1 = {'KKKEDNFW3', 'HHJJGUHJ9', 'MOMMAZZZ0', 'PPPPEJLJ6'}
        id_of_history_2 = set([sale.id for sale in client_summary_2['history']])
        expected_history_ids_2 = set()
        id_of_history_3 = set([sale.id for sale in client_summary_3['history']])
        expected_history_ids_3 = {'KVVNFNNV5', 'GYYYOOPO7', 'LLEWQZLL8', 'NEEFEDCQ1', 'XYZLXXAZ7', 'YTTBJUYY5', 'ZXZXZCVA4', 'WTGTHTGW3', 'VVEEVVOK1'}

        ids_of_pending_pay_1 = set([sale.id for sale in client_summary_1['pending_pay']])
        expected_pending_pay_ids_1 = set()
        ids_of_pending_pay_2 = set([sale.id for sale in client_summary_2['pending_pay']])
        expected_pending_pay_ids_2 = set()
        ids_of_pending_pay_3 = set([sale.id for sale in client_summary_3['pending_pay']])
        expected_pending_pay_ids_3 = {'KVVNFNNV5', 'GYYYOOPO7', 'LLEWQZLL8', 'NEEFEDCQ1', 'VVEEVVOK1'}

        ids_of_pending_deliver_1 = set([sale.id for sale in client_summary_1['pending_deliver']])
        expected_pending_deliver_ids_1 = {'MOMMAZZZ0'}
        ids_of_pending_deliver_2 = set([sale.id for sale in client_summary_2['pending_deliver']])
        expected_pending_deliver_ids_2 = set()
        ids_of_pending_deliver_3 = set([sale.id for sale in client_summary_3['pending_deliver']])
        expected_pending_deliver_ids_3 = {'GYYYOOPO7'}

        self.assertEqual(id_of_history_1, expected_history_ids_1)
        self.assertEqual(id_of_history_2, expected_history_ids_2)
        self.assertEqual(id_of_history_3, expected_history_ids_3)
        self.assertEqual(client_summary_1['cash'], 560)
        self.assertEqual(client_summary_2['cash'], 0)
        self.assertEqual(client_summary_3['cash'], 550)
        self.assertEqual(client_summary_1['amount'], 4)
        self.assertEqual(client_summary_2['amount'], 0)
        self.assertEqual(client_summary_3['amount'], 9)
        self.assertEqual(client_summary_1['debt'], 0)
        self.assertEqual(client_summary_2['debt'], 0)
        self.assertEqual(client_summary_3['debt'], 260)
        self.assertEqual(ids_of_pending_pay_1, expected_pending_pay_ids_1)
        self.assertEqual(ids_of_pending_pay_2, expected_pending_pay_ids_2)
        self.assertEqual(ids_of_pending_pay_3, expected_pending_pay_ids_3)
        self.assertEqual(ids_of_pending_deliver_1, expected_pending_deliver_ids_1)
        self.assertEqual(ids_of_pending_deliver_2, expected_pending_deliver_ids_2)
        self.assertEqual(ids_of_pending_deliver_3, expected_pending_deliver_ids_3)

    def test_monthly_client_summary(self):
        month_1 = datetime(2024, 2, 1)
        client_summary_1 = InfoClients.monthly_client_summary('12345-3', month_1, self.db_file_name)
        month_2 = datetime(2024, 3, 1)
        client_summary_2 = InfoClients.monthly_client_summary('12345-3', month_2, self.db_file_name)
        month_3 = datetime(2024, 4, 1)
        client_summary_3 = InfoClients.monthly_client_summary('12345-3', month_3, self.db_file_name)

        id_of_history_1 = set([sale.id for sale in client_summary_1['history']])
        expected_history_ids_1 = {'KVVNFNNV5', 'GYYYOOPO7', 'XYZLXXAZ7', 'VVEEVVOK1'}
        id_of_history_2 = set([sale.id for sale in client_summary_2['history']])
        expected_history_ids_2 = {'LLEWQZLL8', 'YTTBJUYY5', 'WTGTHTGW3'}
        id_of_history_3 = set([sale.id for sale in client_summary_3['history']])
        expected_history_ids_3 = {'NEEFEDCQ1', 'ZXZXZCVA4'}

        ids_of_pending_pay_1 = set([sale.id for sale in client_summary_1['pending_pay']])
        expected_pending_pay_ids_1 = {'KVVNFNNV5', 'GYYYOOPO7', 'VVEEVVOK1'}
        ids_of_pending_pay_2 = set([sale.id for sale in client_summary_2['pending_pay']])
        expected_pending_pay_ids_2 = {'LLEWQZLL8'}
        ids_of_pending_pay_3 = set([sale.id for sale in client_summary_3['pending_pay']])
        expected_pending_pay_ids_3 = {'NEEFEDCQ1'}

        ids_of_pending_deliver_1 = set([sale.id for sale in client_summary_1['pending_deliver']])
        expected_pending_deliver_ids_1 = {'GYYYOOPO7'}
        ids_of_pending_deliver_2 = set([sale.id for sale in client_summary_2['pending_deliver']])
        expected_pending_deliver_ids_2 = set()
        ids_of_pending_deliver_3 = set([sale.id for sale in client_summary_3['pending_deliver']])
        expected_pending_deliver_ids_3 = set()

        self.assertEqual(id_of_history_1, expected_history_ids_1)
        self.assertEqual(id_of_history_2, expected_history_ids_2)
        self.assertEqual(id_of_history_3, expected_history_ids_3)
        self.assertEqual(client_summary_1['cash'], 205)
        self.assertEqual(client_summary_2['cash'], 215)
        self.assertEqual(client_summary_3['cash'], 130)
        self.assertEqual(client_summary_1['amount'], 4)
        self.assertEqual(client_summary_2['amount'], 3)
        self.assertEqual(client_summary_3['amount'], 2)
        self.assertEqual(client_summary_1['debt'], 125)
        self.assertEqual(client_summary_2['debt'], 75)
        self.assertEqual(client_summary_3['debt'], 60)
        self.assertEqual(ids_of_pending_pay_1, expected_pending_pay_ids_1)
        self.assertEqual(ids_of_pending_pay_2, expected_pending_pay_ids_2)
        self.assertEqual(ids_of_pending_pay_3, expected_pending_pay_ids_3)
        self.assertEqual(ids_of_pending_deliver_1, expected_pending_deliver_ids_1)
        self.assertEqual(ids_of_pending_deliver_2, expected_pending_deliver_ids_2)
        self.assertEqual(ids_of_pending_deliver_3, expected_pending_deliver_ids_3)

class TestInfoSales(unittest.TestCase):
    def setUp(self):
        self.test_db_file = NamedTemporaryFile(delete=False)
        self.db_file_name = self.test_db_file.name
        self.test_db_file.close()
        Clients.create_table_client(self.db_file_name)
        Sales.create_table_sale(self.db_file_name)
        Sales.add_sale('KKKEDNFW3', None, '2024-05-10 21:30:00', 150, 1, 1, 'X5 Pasta Bolognese Combo', self.db_file_name)
        Sales.add_sale('KVVNFNNV5', None, '2024-01-01 12:00:00', 50, 0, 1, 'X1 Large Neapolitan Pizza & X1 Large Jam Pizza', self.db_file_name)
        Sales.add_sale('GYYYOOPO7', None, '2024-02-04 12:30:00', 10, 0, 0, 'X1 Caprese Salad', self.db_file_name)
        Sales.add_sale('HALOFFGA8', None, '2024-03-01 14:15:00', 15, 0, 0, 'X2 Margherita Pizza', self.db_file_name)
        Sales.add_sale('ABAJEABE4', None, '2024-03-15 16:45:00', 20, 0, 0, 'X3 Spaghetti Bolognese', self.db_file_name)
        Sales.add_sale('KEYYYNAD5', None, '2024-04-25 11:00:00', 8, 0, 0, 'X4 Caesar Salad', self.db_file_name)
        Sales.add_sale('LEYYYMNL9', None, '2024-04-25 13:30:00', 12, 0, 0, 'X5 Pepperoni Pizza', self.db_file_name)
        Sales.add_sale('MTMMTMJM2', None, '2024-05-05 15:20:00', 18, 0, 0, 'X6 Lasagna', self.db_file_name)
        Sales.add_sale('LMNNHTNH5', None, '2024-05-10 14:30:00', 22, 1, 0, 'X3 Tiramisu', self.db_file_name)
        Sales.add_sale('HGHTGHTY0', None, '2024-06-15 18:00:00', 35, 0, 1, 'X4 Chicken Alfredo', self.db_file_name)
        Sales.add_sale('KKLPPMPY0', None, '2024-06-20 12:45:00', 50, 1, 1, 'X2 Seafood Risotto', self.db_file_name)
        Sales.add_sale('NIGFFFIG6', None, '2024-05-25 19:10:00', 27, 0, 0, 'X2 Cannoli', self.db_file_name)
        Sales.add_sale('PEPOJILO3', None, '2024-07-05 16:40:00', 45, 1, 1, 'X5 Four Cheese Pizza', self.db_file_name)
        Sales.add_sale('ARAEARRA8', None, '2023-02-14 18:30:00', 35, 0, 1, 'X1 Medium Pepperoni Pizza & X1 Medium Cheese Pizza', self.db_file_name)
        Sales.add_sale('BBBNMBBB1', None, '2023-05-21 20:00:00', 42, 1, 1, 'X1 Large Veggie Pizza & X1 Large BBQ Chicken Pizza', self.db_file_name)
        Sales.add_sale('CKJCLKCK5', None, '2023-08-03 12:45:00', 60, 0, 0, 'X2 Large Hawaiian Pizza', self.db_file_name)
        Sales.add_sale('DEEDDONN6', None, '2023-10-10 19:15:00', 28, 1, 1, 'X1 Medium Margherita Pizza & X1 Medium Meat Lovers Pizza', self.db_file_name)
        Sales.add_sale('EREEJJKK0', None, '2023-12-25 17:00:00', 50, 1, 0, 'X1 Large Supreme Pizza & X1 Large Garlic Bread', self.db_file_name)

    def tearDown(self):
        try:
            os.remove(self.db_file_name)
        except PermissionError:
            pass

    def test_total_summary(self):
        summary = InfoSales.total_summary(self.db_file_name)

        ids_of_pending_transactions = set([sale.id for sale in summary['pending_transactions']])
        ids_of_pending_services = set([sale.id for sale in summary['pending_services']])
        ids_of_all_sales = set([sale.id for sale in summary['all_sales']])

        expected_transaction_states_ids = {'CKJCLKCK5', 'ARAEARRA8', 'KVVNFNNV5', 'GYYYOOPO7', 'HALOFFGA8', 'ABAJEABE4', 'KEYYYNAD5', 'LEYYYMNL9', 'MTMMTMJM2', 'HGHTGHTY0', 'NIGFFFIG6'}
        expected_transaction_states = {'paid': 7, 'pending': 11}
        expected_service_states = {'delivered': 8, 'pending': 10}
        expected_services_states_ids = {'EREEJJKK0', 'CKJCLKCK5', 'GYYYOOPO7', 'HALOFFGA8', 'ABAJEABE4', 'KEYYYNAD5', 'LEYYYMNL9', 'MTMMTMJM2', 'LMNNHTNH5', 'NIGFFFIG6'}
        expected_all_ids = {'EREEJJKK0', 'DEEDDONN6', 'CKJCLKCK5', 'BBBNMBBB1', 'ARAEARRA8', 'KKKEDNFW3', 'KVVNFNNV5', 'GYYYOOPO7', 'HALOFFGA8', 'ABAJEABE4', 'KEYYYNAD5', 'LEYYYMNL9', 'MTMMTMJM2', 'HGHTGHTY0', 'NIGFFFIG6', 'LMNNHTNH5', 'KKLPPMPY0', 'PEPOJILO3'}

        self.assertEqual(summary['cash'], 677)
        self.assertEqual(summary['transaction_states'], expected_transaction_states)
        self.assertEqual(ids_of_pending_transactions, expected_transaction_states_ids)
        self.assertEqual(summary['service_states'], expected_service_states)
        self.assertEqual(ids_of_pending_services, expected_services_states_ids)
        self.assertEqual(ids_of_all_sales, expected_all_ids)
        self.assertEqual(summary['total_sales'], 18)

    def test_daily_summary(self):
        day_1 = datetime(2024, 7, 5)
        summary_1 = InfoSales.dialy_summary(day_1, self.db_file_name)
        day_2 = datetime(2024, 4, 25)
        summary_2 = InfoSales.dialy_summary(day_2, self.db_file_name)
        day_3 = datetime(2023, 2, 1)
        summary_3 = InfoSales.dialy_summary(day_3, self.db_file_name)

        ids_pending_transaction_states_1 = set([sale.id for sale in summary_1['pending_transactions']])
        ids_pending_transaction_states_2 = set([sale.id for sale in summary_2['pending_transactions']])
        ids_pending_transaction_states_3 = set([sale.id for sale in summary_3['pending_transactions']])
        ids_pending_service_states_1 = set([sale.id for sale in summary_1['pending_services']])
        ids_pending_service_states_2 = set([sale.id for sale in summary_2['pending_services']])
        ids_pending_service_states_3 = set([sale.id for sale in summary_3['pending_services']])
        ids_of_all_sales_1 = set([sale.id for sale in summary_1['all_sales']])
        ids_of_all_sales_2 = set([sale.id for sale in summary_2['all_sales']])
        ids_of_all_sales_3 = set([sale.id for sale in summary_3['all_sales']])

        expected_transaction_states_1 = {'paid': 1, 'pending': 0}
        expected_transaction_states_2 = {'paid': 0, 'pending': 2}
        expected_transaction_states_3 = {'paid': 0, 'pending': 0}
        expected_pending_transaction_ids_1 = set()
        expected_pending_transaction_ids_2 = {'KEYYYNAD5', 'LEYYYMNL9'}
        expected_pending_transaction_ids_3 = set()
        expected_service_states_1 = {'delivered': 1, 'pending': 0}
        expected_service_states_2 = {'delivered': 0, 'pending': 2}
        expected_service_states_3 = {'delivered': 0, 'pending': 0}
        expected_pending_services_ids_1 = set()
        expected_pending_services_ids_2 = {'KEYYYNAD5', 'LEYYYMNL9'}
        expected_pending_services_ids_3 = set()
        expected_all_sales_id_1 = {'PEPOJILO3'}
        expected_all_sales_id_2 = {'KEYYYNAD5', 'LEYYYMNL9'}
        expected_all_sales_id_3 = set()

        self.assertEqual(summary_1['cash'], 45)
        self.assertEqual(summary_2['cash'], 20)
        self.assertEqual(summary_3['cash'], 0)
        self.assertEqual(summary_1['transaction_states'], expected_transaction_states_1)
        self.assertEqual(summary_2['transaction_states'], expected_transaction_states_2)
        self.assertEqual(summary_3['transaction_states'], expected_transaction_states_3)
        self.assertEqual(ids_pending_transaction_states_1, expected_pending_transaction_ids_1)
        self.assertEqual(ids_pending_transaction_states_2, expected_pending_transaction_ids_2)
        self.assertEqual(ids_pending_transaction_states_3, expected_pending_transaction_ids_3)
        self.assertEqual(summary_1['service_states'], expected_service_states_1)
        self.assertEqual(summary_2['service_states'], expected_service_states_2)
        self.assertEqual(summary_3['service_states'], expected_service_states_3)
        self.assertEqual(ids_pending_service_states_1, expected_pending_services_ids_1)
        self.assertEqual(ids_pending_service_states_2, expected_pending_services_ids_2)
        self.assertEqual(ids_pending_service_states_3, expected_pending_services_ids_3)
        self.assertEqual(ids_of_all_sales_1, expected_all_sales_id_1)
        self.assertEqual(ids_of_all_sales_2, expected_all_sales_id_2)
        self.assertEqual(ids_of_all_sales_3, expected_all_sales_id_3)
        self.assertEqual(summary_1['total_sales'], 1)
        self.assertEqual(summary_2['total_sales'], 2)
        self.assertEqual(summary_3['total_sales'], 0)

    def test_monthly_summary(self):
        month_1 = datetime(2024, 7, 1)
        summary_1 = InfoSales.monthly_summary(month_1, self.db_file_name)
        month_2 = datetime(2024, 6, 1)
        summary_2 = InfoSales.monthly_summary(month_2, self.db_file_name)
        month_3 = datetime(2024, 5, 1)
        summary_3 = InfoSales.monthly_summary(month_3, self.db_file_name)
        month_4 = datetime(2024, 4, 1)
        summary_4 = InfoSales.monthly_summary(month_4, self.db_file_name)

        ids_pending_transaction_states_1 = set([sale.id for sale in summary_1['pending_transactions']])
        ids_pending_transaction_states_2 = set([sale.id for sale in summary_2['pending_transactions']])
        ids_pending_transaction_states_3 = set([sale.id for sale in summary_3['pending_transactions']])
        ids_pending_transaction_states_4 = set([sale.id for sale in summary_4['pending_transactions']])
        ids_pending_service_states_1 = set([sale.id for sale in summary_1['pending_services']])
        ids_pending_service_states_2 = set([sale.id for sale in summary_2['pending_services']])
        ids_pending_service_states_3 = set([sale.id for sale in summary_3['pending_services']])
        ids_pending_service_states_4 = set([sale.id for sale in summary_4['pending_services']])
        ids_of_all_sales_1 = set([sale.id for sale in summary_1['all_sales']])
        ids_of_all_sales_2 = set([sale.id for sale in summary_2['all_sales']])
        ids_of_all_sales_3 = set([sale.id for sale in summary_3['all_sales']])
        ids_of_all_sales_4 = set([sale.id for sale in summary_4['all_sales']])

        expected_transaction_states_1 = {'paid': 1, 'pending': 0}
        expected_transaction_states_2 = {'paid': 1, 'pending': 1}
        expected_transaction_states_3 = {'paid': 2, 'pending': 2}
        expected_transaction_states_4 = {'paid': 0, 'pending': 2}
        expected_pending_transaction_ids_1 = set()
        expected_pending_transaction_ids_2 = {'HGHTGHTY0'}
        expected_pending_transaction_ids_3 = {'MTMMTMJM2', 'NIGFFFIG6'}
        expected_pending_transaction_ids_4 = {'KEYYYNAD5', 'LEYYYMNL9'}
        expected_service_states_1 = {'delivered': 1, 'pending': 0}
        expected_service_states_2 = {'delivered': 2, 'pending': 0}
        expected_service_states_3 = {'delivered': 1, 'pending': 3}
        expected_service_states_4 = {'delivered': 0, 'pending': 2}
        expected_pending_services_ids_1 = set()
        expected_pending_services_ids_2 = set()
        expected_pending_services_ids_3 = {'MTMMTMJM2', 'LMNNHTNH5', 'NIGFFFIG6'}
        expected_pending_services_ids_4 = {'KEYYYNAD5', 'LEYYYMNL9'}
        expected_all_sales_id_1 = {'PEPOJILO3'}
        expected_all_sales_id_2 = {'HGHTGHTY0', 'KKLPPMPY0'}
        expected_all_sales_id_3 = {'KKKEDNFW3', 'MTMMTMJM2', 'LMNNHTNH5', 'NIGFFFIG6'}
        expected_all_sales_id_4 = {'KEYYYNAD5', 'LEYYYMNL9'}

        self.assertEqual(summary_1['cash'], 45)
        self.assertEqual(summary_2['cash'], 85)
        self.assertEqual(summary_3['cash'], 217)
        self.assertEqual(summary_4['cash'], 20)
        self.assertEqual(summary_1['transaction_states'], expected_transaction_states_1)
        self.assertEqual(summary_2['transaction_states'], expected_transaction_states_2)
        self.assertEqual(summary_3['transaction_states'], expected_transaction_states_3)
        self.assertEqual(summary_4['transaction_states'], expected_transaction_states_4)
        self.assertEqual(ids_pending_transaction_states_1, expected_pending_transaction_ids_1)
        self.assertEqual(ids_pending_transaction_states_2, expected_pending_transaction_ids_2)
        self.assertEqual(ids_pending_transaction_states_3, expected_pending_transaction_ids_3)
        self.assertEqual(ids_pending_transaction_states_4, expected_pending_transaction_ids_4)
        self.assertEqual(summary_1['service_states'], expected_service_states_1)
        self.assertEqual(summary_2['service_states'], expected_service_states_2)
        self.assertEqual(summary_3['service_states'], expected_service_states_3)
        self.assertEqual(summary_4['service_states'], expected_service_states_4)
        self.assertEqual(ids_pending_service_states_1, expected_pending_services_ids_1)
        self.assertEqual(ids_pending_service_states_2, expected_pending_services_ids_2)
        self.assertEqual(ids_pending_service_states_3, expected_pending_services_ids_3)
        self.assertEqual(ids_pending_service_states_4, expected_pending_services_ids_4)
        self.assertEqual(ids_of_all_sales_1, expected_all_sales_id_1)
        self.assertEqual(ids_of_all_sales_2, expected_all_sales_id_2)
        self.assertEqual(ids_of_all_sales_3, expected_all_sales_id_3)
        self.assertEqual(ids_of_all_sales_4, expected_all_sales_id_4)
        self.assertEqual(summary_1['total_sales'], 1)
        self.assertEqual(summary_2['total_sales'], 2)
        self.assertEqual(summary_3['total_sales'], 4)
        self.assertEqual(summary_4['total_sales'], 2)

    def test_annual_summary(self):
        year_1 = datetime(2024, 1, 1)
        summary_1 = InfoSales.annual_summary(year_1, self.db_file_name)
        year_2 = datetime(2023, 1, 1)
        summary_2 = InfoSales.annual_summary(year_2, self.db_file_name)
        year_3 = datetime(2022, 1, 1)
        summary_3 = InfoSales.annual_summary(year_3, self.db_file_name)

        ids_pending_transaction_states_1 = set([sale.id for sale in summary_1['pending_transactions']])
        ids_pending_transaction_states_2 = set([sale.id for sale in summary_2['pending_transactions']])
        ids_pending_transaction_states_3 = set([sale.id for sale in summary_3['pending_transactions']])
        ids_pending_service_states_1 = set([sale.id for sale in summary_1['pending_services']])
        ids_pending_service_states_2 = set([sale.id for sale in summary_2['pending_services']])
        ids_pending_service_states_3 = set([sale.id for sale in summary_3['pending_services']])
        ids_of_all_sales_1 = set([sale.id for sale in summary_1['all_sales']])
        ids_of_all_sales_2 = set([sale.id for sale in summary_2['all_sales']])
        ids_of_all_sales_3 = set([sale.id for sale in summary_3['all_sales']])

        expected_transaction_states_1 = {'paid': 4, 'pending': 9}
        expected_transaction_states_2 = {'paid': 3, 'pending': 2}
        expected_transaction_states_3 = {'paid': 0, 'pending': 0}
        expected_pending_transaction_ids_1 = {'KVVNFNNV5', 'GYYYOOPO7', 'HALOFFGA8', 'ABAJEABE4', 'KEYYYNAD5', 'LEYYYMNL9', 'MTMMTMJM2', 'HGHTGHTY0', 'NIGFFFIG6'}
        expected_pending_transaction_ids_2 = {'ARAEARRA8', 'CKJCLKCK5'}
        expected_pending_transaction_ids_3 = set()
        expected_service_states_1 = {'delivered': 5, 'pending': 8}
        expected_service_states_2 = {'delivered': 3, 'pending': 2}
        expected_service_states_3 = {'delivered': 0, 'pending': 0}
        expected_pending_services_ids_1 = {'GYYYOOPO7', 'HALOFFGA8', 'ABAJEABE4', 'KEYYYNAD5', 'LEYYYMNL9', 'MTMMTMJM2', 'LMNNHTNH5', 'NIGFFFIG6'}
        expected_pending_services_ids_2 = {'CKJCLKCK5', 'EREEJJKK0'}
        expected_pending_services_ids_3 = set()
        expected_all_sales_id_1 = {'KKKEDNFW3', 'KVVNFNNV5', 'GYYYOOPO7', 'HALOFFGA8', 'ABAJEABE4', 'KEYYYNAD5', 'LEYYYMNL9', 'MTMMTMJM2', 'LMNNHTNH5', 'HGHTGHTY0', 'KKLPPMPY0', 'NIGFFFIG6', 'PEPOJILO3'}
        expected_all_sales_id_2 = {'ARAEARRA8', 'BBBNMBBB1', 'CKJCLKCK5', 'DEEDDONN6', 'EREEJJKK0'}
        expected_all_sales_id_3 = set()

        self.assertEqual(summary_1['cash'], 462)
        self.assertEqual(summary_2['cash'], 215)
        self.assertEqual(summary_3['cash'], 0)
        self.assertEqual(summary_1['transaction_states'], expected_transaction_states_1)
        self.assertEqual(summary_2['transaction_states'], expected_transaction_states_2)
        self.assertEqual(summary_3['transaction_states'], expected_transaction_states_3)
        self.assertEqual(ids_pending_transaction_states_1, expected_pending_transaction_ids_1)
        self.assertEqual(ids_pending_transaction_states_2, expected_pending_transaction_ids_2)
        self.assertEqual(ids_pending_transaction_states_3, expected_pending_transaction_ids_3)
        self.assertEqual(summary_1['service_states'], expected_service_states_1)
        self.assertEqual(summary_2['service_states'], expected_service_states_2)
        self.assertEqual(summary_3['service_states'], expected_service_states_3)
        self.assertEqual(ids_pending_service_states_1, expected_pending_services_ids_1)
        self.assertEqual(ids_pending_service_states_2, expected_pending_services_ids_2)
        self.assertEqual(ids_pending_service_states_3, expected_pending_services_ids_3)
        self.assertEqual(ids_of_all_sales_1, expected_all_sales_id_1)
        self.assertEqual(ids_of_all_sales_2, expected_all_sales_id_2)
        self.assertEqual(ids_of_all_sales_3, expected_all_sales_id_3)
        self.assertEqual(summary_1['total_sales'], 13)
        self.assertEqual(summary_2['total_sales'], 5)
        self.assertEqual(summary_3['total_sales'], 0)