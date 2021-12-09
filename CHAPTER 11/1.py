from datetime import datetime
from datetime import date

def diffDate(dateSatu, dateDua):
    return abs(dateDua-dateSatu).days

def delta():
    Date1 = date(2021,11,13)
    Date2 = date(2021,11,27)

    #Tanggal yang akan dihitung
    result = diffDate(Date2, Date1)
    print('Jumlah selisih hari adalah sebanyak', result)

delta()