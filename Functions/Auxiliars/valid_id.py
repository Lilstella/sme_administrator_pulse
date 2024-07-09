import re

person_id_pattern = '[A-Z0-9]{5}-[A-Z0-9]$'
transfer_id_pattern = '[0-9]{8}[A-Z]$'

id_patterns = {
    'client_id_pattern': person_id_pattern,
    'worker_id_pattern': person_id_pattern,
    'sale_id_pattern': transfer_id_pattern,
    'expense_id_pattern': transfer_id_pattern,
    'task_id_pattern': '[A-Z]{8}[0-9]'
}

def valid_id(id, list, pattern_key):
    pattern = id_patterns.get(pattern_key)
    if not re.match(pattern, id):
        return False
    for any in list:
        if any.id == id:
            return False
    return True