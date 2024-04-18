from datetime import datetime

def date():
    date = datetime.now()
    moment = datetime.strftime(date, "%d/%m/%Y")
    return moment