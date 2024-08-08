from datetime import datetime as dt
from Functions.models import Clients, Sales

class InfoClients:
    @staticmethod
    def gender_of_clients(db_file):
        clients = Clients.load_clients(db_file)
        gender_clients = {'Male': 0, 'Female': 0, 'Other': 0}

        for client in clients:
          match client.gender:
               case 'M':
                    gender_clients['Male'] += 1

               case 'F':
                    gender_clients['Female'] += 1
               
               case 'O':
                  gender_clients['Other'] += 1
     
        return gender_clients
    
    @staticmethod
    def age_of_clients(db_file):
        clients = Clients.load_clients(db_file)
        age_clients = {'15-20': 0, '21-25': 0, '26-30': 0, '31-35': 0, '36-40': 0, '41-45': 0, '46+': 0}

        for client in clients:
          match client.age:
               case age if 15 <= age <= 20:
                  age_clients['15-20'] += 1

               case age if 21 <= age <= 25:
                  age_clients['21-25'] += 1

               case age if 26 <= age <= 30:
                  age_clients['26-30'] += 1

               case age if 31 <= age <= 35:
                  age_clients['31-35'] += 1

               case age if 36 <= age <= 40:
                  age_clients['36-40'] += 1

               case age if 41 <= age <= 45:
                  age_clients['41-45'] += 1

               case age if age >= 46:
                  age_clients['46+'] += 1

        return age_clients

    @staticmethod
    def client_sale_history(db_file, id):
        total_sales = Sales.load_sales(db_file)
        client_history = []

        for sale in total_sales:
            if sale.client_id == id:
                client_history.append(sale)

        return client_history
    
    @staticmethod
    def client_total_cash(db_file, id):
        total_sales = Sales.load_sales(db_file)
        client_cash = 0

        for sale in total_sales:
            if sale.client_id == id:
               client_cash += sale.cash

        return client_cash
    
    @staticmethod
    def client_total_sales(db_file, id):
        total_sales = Sales.load_sales(db_file)
        total_client_sales = 0

        for sale in total_sales:
            if sale.client_id == id:
               total_client_sales += 1

        return total_client_sales
    
    @staticmethod
    def debt_of_the_client(db_file, id):
        total_sales = Sales.load_sales(db_file)
        debt = 0

        for sale in total_sales:
            if sale.client_id == id and sale.paid == 0:
               debt += sale.cash

        return debt
    
class InfoSales:
   @staticmethod
   def total_cash_sales(db_file):
       total_sales = Sales.load_sales(db_file)
       total_cash = 0

       for sale in total_sales:
           total_cash += sale.cash

       return total_cash
   
   @staticmethod
   def total_cash_sale_for_day(db_file, date):
       total_sales = Sales.load_sales(db_file)
       total_cash_for_day = 0
       day_str = date.strftime('%Y-%m-%d')

       for sale in total_sales:
           sale_date_str = sale.date.split(' ')[0]
           if sale_date_str == day_str:
               total_cash_for_day += sale.cash

       return total_cash_for_day
   
   @staticmethod
   def total_cash_sale_today(db_file):
       today = dt.now()
       total_cash_day = InfoSales.total_cash_sale_for_day(db_file, today)

       return total_cash_day
   
   @staticmethod
   def total_cash_sale_for_month(db_file, date):
       total_sales = Sales.load_sales(db_file)
       total_cash_for_month = 0
       date_year = date.year
       date_month = date.month

       for sale in total_sales:
           sale_date = dt.strptime(sale.date, '%Y-%m-%d %H:%M:%S')
           if sale_date.year == date_year and sale_date.month == date_month:
               total_cash_for_month += sale.cash

       return total_cash_for_month
   
   @staticmethod
   def total_cash_sale_this_month(db_file):
       today = dt.now()
       total_cash_this_month = InfoSales.total_cash_sale_for_month(db_file, today)

       return total_cash_this_month
   
   @staticmethod
   def total_cash_sale_for_year(db_file, date):
       total_sales = Sales.load_sales(db_file)
       total_cash_for_year = 0
       date_year = date.year

       for sale in total_sales:
           sale_date = dt.strptime(sale.date, '%Y-%m-%d %H:%M:%S')
           if sale_date.year == date_year:
               total_cash_for_year += sale.cash

       return total_cash_for_year
   
   @staticmethod
   def total_cash_sale_this_year(db_file):
       today = dt.now()
       total_cash_this_year = InfoSales.total_cash_sale_for_year(db_file, today)

       return total_cash_this_year
   
   @staticmethod
   def transaction_state_of_sales(db_file):
       total_sales = Sales.load_sales(db_file)
       transaction_state_of_sales = {'paid': 0, 'pending': 0}

       for sale in total_sales:
           if sale.paid == 0:
               transaction_state_of_sales['pending'] += 1
           elif sale.paid == 1:
               transaction_state_of_sales['paid'] += 1

       return transaction_state_of_sales
   
   @staticmethod
   def sales_pending_to_pay(db_file):
       total_sales = Sales.load_sales(db_file)
       pending_sales = []

       for sale in total_sales:
           if sale.paid == 0:
               pending_sales.append(sale)
          
       return pending_sales

   @staticmethod
   def service_state_of_sales(db_file):
       total_sales = Sales.load_sales(db_file)
       service_state_of_sales = {'delivered': 0, 'pending': 0}

       for sale in total_sales:
           if sale.delivered == 0:
               service_state_of_sales['pending'] += 1
           elif sale.delivered == 1:
               service_state_of_sales['delivered'] += 1

       return service_state_of_sales
   
   @staticmethod
   def sales_pending_to_deliver(db_file):
       total_sales = Sales.load_sales(db_file)
       pending_sales = []

       for sale in total_sales:
           if sale.delivered == 0:
               pending_sales.append(sale)

       return pending_sales