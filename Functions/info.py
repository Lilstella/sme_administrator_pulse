from datetime import datetime as dt
from Functions.models import Clients, Sales, Workers, Expenses

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
    def client_summary(id, db_file):
        all_sales = Sales.load_sales(db_file)
        client_history = []
        client_cash = 0
        total_client_sales = 0
        debt = 0
        sales_pending_to_paid = []
        sales_pending_to_deliver = []

        for sale in all_sales:
            if sale.client_id == id:
                client_history.append(sale)
                client_cash += sale.cash
                total_client_sales += 1
                if sale.paid == 0:
                    sales_pending_to_paid.append(sale)
                    debt += sale.cash
                if sale.delivered == 0:
                    sales_pending_to_deliver.append(sale)

        return {'history': client_history, 
                'cash': client_cash, 
                'amount': total_client_sales, 
                'debt': debt, 
                'pending_pay': sales_pending_to_paid, 
                'pending_deliver': sales_pending_to_deliver}    
     
class InfoSales:
   @staticmethod
   def total_summary(db_file):
       all_sales = Sales.load_sales(db_file)
       total_cash = 0
       transaction_state_of_sales = {'paid': 0, 'pending': 0}
       pending_sales_to_pay = []
       service_state_of_sales = {'delivered': 0, 'pending': 0}
       pending_sales_to_deliver = []

       for sale in all_sales:
           total_cash += sale.cash

           if sale.paid == 0:
               transaction_state_of_sales['pending'] += 1
               pending_sales_to_pay.append(sale)
           elif sale.paid == 1:
               transaction_state_of_sales['paid'] += 1

           if sale.delivered == 0:
               service_state_of_sales['pending'] += 1
               pending_sales_to_deliver.append(sale)
           elif sale.delivered == 1:
               service_state_of_sales['delivered'] += 1

       return {'cash': total_cash, 
               'transaction_states': transaction_state_of_sales, 
               'pending_transactions': pending_sales_to_pay,
               'service_states': service_state_of_sales,
               'pending_services': pending_sales_to_deliver,
               'all_sales': all_sales,
               'total_sales': len(all_sales)}
   
   @staticmethod
   def dialy_summary(date, db_file):
       all_sales = Sales.load_sales(db_file)
       total_cash_this_day = 0
       transaction_state_of_sales_this_day = {'paid': 0, 'pending': 0}
       pending_sales_to_pay_this_day = []
       service_state_of_sales_this_day = {'delivered': 0, 'pending': 0}
       pending_sales_to_deliver_this_day = []
       all_sales_this_day = []
       day_str = date.strftime('%Y-%m-%d')

       for sale in all_sales:
           sale_date_str = sale.date.split(' ')[0]
           if sale_date_str == day_str:
               total_cash_this_day += sale.cash
               all_sales_this_day.append(sale)

               if sale.paid == 0:
                transaction_state_of_sales_this_day['pending'] += 1
                pending_sales_to_pay_this_day.append(sale)
               elif sale.paid == 1:
                transaction_state_of_sales_this_day['paid'] += 1

               if sale.delivered == 0:
                service_state_of_sales_this_day['pending'] += 1
                pending_sales_to_deliver_this_day.append(sale)
               elif sale.delivered == 1:
                service_state_of_sales_this_day['delivered'] += 1

       return {'cash': total_cash_this_day,
               'transaction_states': transaction_state_of_sales_this_day, 
               'pending_transactions': pending_sales_to_pay_this_day,
               'service_states': service_state_of_sales_this_day,
               'pending_services': pending_sales_to_deliver_this_day,
               'all_sales': all_sales_this_day,
               'total_sales': len(all_sales_this_day)}
   
   @staticmethod
   def monthly_summary(date, db_file):
       all_sales = Sales.load_sales(db_file)
       total_cash_this_month = 0
       transaction_state_of_sales_this_month = {'paid': 0, 'pending': 0}
       pending_sales_to_pay_this_month = []
       service_state_of_sales_this_month = {'delivered': 0, 'pending': 0}
       pending_sales_to_deliver_this_month = []
       all_sales_this_month = []
       date_year = date.year
       date_month = date.month

       for sale in all_sales:
           sale_date = dt.strptime(sale.date, '%Y-%m-%d %H:%M:%S')
           if sale_date.year == date_year and sale_date.month == date_month:
               total_cash_this_month += sale.cash
               all_sales_this_month.append(sale)

               if sale.paid == 0:
                transaction_state_of_sales_this_month['pending'] += 1
                pending_sales_to_pay_this_month.append(sale)
               elif sale.paid == 1:
                transaction_state_of_sales_this_month['paid'] += 1

               if sale.delivered == 0:
                service_state_of_sales_this_month['pending'] += 1
                pending_sales_to_deliver_this_month.append(sale)
               elif sale.delivered == 1:
                service_state_of_sales_this_month['delivered'] += 1

       return {'cash': total_cash_this_month,
               'transaction_states': transaction_state_of_sales_this_month, 
               'pending_transactions': pending_sales_to_pay_this_month,
               'service_states': service_state_of_sales_this_month,
               'pending_services': pending_sales_to_deliver_this_month,
               'all_sales': all_sales_this_month,
               'total_sales': len(all_sales_this_month)}
   
   @staticmethod
   def annual_summary(date, db_file):
      all_sales = Sales.load_sales(db_file)
      total_cash_this_year = 0
      transaction_state_of_sales_this_year = {'paid': 0, 'pending': 0}
      pending_sales_to_pay_this_year = []
      service_state_of_sales_this_year = {'delivered': 0, 'pending': 0}
      pending_sales_to_deliver_this_year = []
      all_sales_this_year = []
      date_year = date.year

      for sale in all_sales:
          sale_date = dt.strptime(sale.date, '%Y-%m-%d %H:%M:%S')
          if sale_date.year == date_year:
             total_cash_this_year += sale.cash
             all_sales_this_year.append(sale)

             if sale.paid == 0:
                transaction_state_of_sales_this_year['pending'] += 1
                pending_sales_to_pay_this_year.append(sale)
             elif sale.paid == 1:
                transaction_state_of_sales_this_year['paid'] += 1

             if sale.delivered == 0:
                service_state_of_sales_this_year['pending'] += 1
                pending_sales_to_deliver_this_year.append(sale)
             elif sale.delivered == 1:
                service_state_of_sales_this_year['delivered'] += 1

      return {'cash': total_cash_this_year,
               'transaction_states': transaction_state_of_sales_this_year, 
               'pending_transactions': pending_sales_to_pay_this_year,
               'service_states': service_state_of_sales_this_year,
               'pending_services': pending_sales_to_deliver_this_year,
               'all_sales': all_sales_this_year,
               'total_sales': len(all_sales_this_year)}