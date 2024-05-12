from datetime import datetime

def date():
    date = datetime.now()
    moment = datetime.strftime(date, "%Y-%m-%d")
    return moment