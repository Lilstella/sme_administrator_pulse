import sys
import re

DATABASE_PATH = "clients.db"

if "pytest" in sys.argv[0]:
    DATABASE_PATH = "tests/clientes_test.csv"


def valid_id(id, list):
    if not re.match('[0-9]{2}[A-Z]$', id):
        return False
    for client in list:
        if client.id == id:
            return False
    return True
 