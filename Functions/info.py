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
    def client_sales_history(db_file, id):
        total_sales = Sales.load_sales(db_file)
        client_history = []

        for sale in total_sales:
            if sale.client_id == id:
                client_history.append(sale)

        return total_sales
    
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