import re
        
def valid_id(id, list):
    if not re.match('[0-9]{2}[A-Z]$', id):
        return False
    for client in list:
        if client.id == id:
            return False
    return True
 

