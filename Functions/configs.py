import sys
import re
from datetime import datetime

DATABASE_PATH = "data.db"

if "pytest" in sys.argv[0]:
    DATABASE_PATH = "Test/data_test.db"


def valid_id(id, list):
    if not re.match('[A-Z0-9]{3}-[A-Z0-9]$', id):
        return False
    for client in list:
        if client.id == id:
            return False
    return True

def date():
    date = datetime.now()
    moment = datetime.strftime(date, "%d/%m/%Y")

    return moment