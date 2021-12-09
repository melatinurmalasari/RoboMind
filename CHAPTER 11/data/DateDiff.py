from datetime import datetime
from datetime import date

def diffDate(n):
    n = n.split('-')
    years  = int(n[0])
    month  = int(n[1])
    day = int(n[2])
    date1 = datetime(years, month, day)
    date2 = datetime.now()
    delta = date2 - date1
    return delta.day