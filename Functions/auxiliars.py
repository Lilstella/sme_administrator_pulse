import re
from datetime import datetime

def valid_id(id, list):
    if not re.match('[A-Z0-9]{3}-[A-Z0-9]$', id):
        return False
    for any in list:
        if any.id == id:
            return False
    return True

def date():
    date = datetime.now()
    moment = datetime.strftime(date, "%d/%m/%Y")
    return moment