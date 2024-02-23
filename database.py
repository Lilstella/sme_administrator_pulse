import sqlite3 as sql
import config

class Client:
    def __init__(self, id, name, last_name, gender, age):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.gender = gender
        self.age = age

class Clients:
    #Generate/connect database
    connector = sql.connect(config.DATABASE_PATH)
    cursor = connector.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS clients" \
                   "(id VARCHAR PRIMARY KEY, name VARCHAR, last_name VARCHAR, gender VARCHAR, age INTEGER)")
    
    #List of clients/objects
    list_clients = []

    #Add all clients in the list
    content = cursor.execute('SELECT * FROM clients').fetchall()
    for id, name, last_name, gender, age in content:
        client = Client(id, name, last_name, gender, age)
        list_clients.append(client) 

    connector.close()

    @staticmethod
    def add(id, name, last_name, gender, age):
        connector = sql.connect(config.DATABASE_PATH)
        cursor = connector.cursor() 

        client = Client(id, name, last_name, gender, age)
        Clients.list_clients.append(client) 
        cursor.execute("INSERT INTO clients(id, name, last_name, gender, age) VALUES(?, ?, ?, ?, ?)", (client.id, client.name, client.last_name, client.gender, client.age))
           
        connector.commit()
        connector.close()
    
    @staticmethod
    def modificate(id, name, last_name, gender, age):
        connector = sql.connect(config.DATABASE_PATH)
        cursor = connector.cursor() 

        for i, client in enumerate(Clients.list_clients):
            if client.id == id:
                Clients.list_clients[i].name = name
                Clients.list_clients[i].last_name = last_name
                Clients.list_clients[i].gender = gender
                Clients.list_clients[i].age = age 
                cursor.execute("UPDATE clients SET name = ?, last_name = ?, gender = ?, age = ? WHERE id = ?", (client.name, client.last_name, client.id, client.gender, client.age))

        connector.commit()
        connector.close()
            
    @staticmethod          
    def remove(id):
        connector = sql.connect(config.DATABASE_PATH)
        cursor = connector.cursor()

        for index, client in enumerate(Clients.list_clients):
            if client.id == id:
                Clients.list_clients.pop(index)
                cursor.execute("DELETE FROM clients WHERE id = ?", (id,))

        connector.commit()
        connector.close()

    @staticmethod
    def add_many(clients):
        connector = sql.connect(config.DATABASE_PATH)
        cursor = connector.cursor()

        for any in clients:
            client = Client(any[0], any[1], any[2], any[3], any[4])
            Clients.list_clients.append(client) 
            cursor.execute("INSERT INTO clients(id, name, last_name, gender, age) VALUES(?, ?, ?, ?, ?)", (client.id, client.name, client.last_name, client.gender, client.age))

        connector.commit()
        connector.close()

    @staticmethod
    def remove_all(): 
        connector = sql.connect(config.DATABASE_PATH)
        cursor = connector.cursor() 

        cursor.execute("DELETE FROM clients;")

        connector.commit()
        connector.close()
