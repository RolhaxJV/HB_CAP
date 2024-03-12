from datetime import datetime,date
import pandas as pd
from app.models import F_Dose

def find_date(S_year):
    """
    Find the date in the past based on the input year.

    Args:
        S_year (int): The year to find the date in the past from.

    Returns:
        date: The calculated date in the past.
    """
    date_now = datetime.now()
    sem_now = date_now.isocalendar()[1]
    
    
    sub = date_now.year - S_year
    if sub < 0:
        return None
    date_past = date(date_now.year - sub, date_now.month, date_now.day )
    sem_past = date_past.isocalendar()[1]
    
    diff_sem = sem_now - sem_past
    if diff_sem >= 1:
        date_past = date(2021,date_past.month,date_past.day + 7 * diff_sem)
        sem_past = date_past.isocalendar()[1]
        
    weekday = date_past.isocalendar().weekday
    diff = 0
    if weekday != 7:
        diff = 7 - weekday
    return date(date_past.year,date_past.month,date_past.day + diff)

def find_data(S_year,depart_id):
    """
    This function takes two parameters, S_year and depart_id, and returns the sum of nb_dose values from the F_Dose objects filtered by Date_id and Depart_id. If the last_day is not found, it prints "date in the future" and returns None.
    """
    last_day = find_date(S_year)

    if(last_day == None):
        print("date in the future")
        return
    df = pd.DataFrame(list(F_Dose.objects.values('nb_dose').filter(Date_id=last_day, Depart_id=depart_id)))
    return df.sum()
