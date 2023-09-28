from datetime import timedelta, datetime, date
from collections import defaultdict

def get_birthdays_per_week(users:list):
    cur_date = date.today()
    delta = timedelta(days=7)
    date_off = cur_date + delta
   
    birthdays_dict = defaultdict(list)
    
    for user in users:
        
        day_of_birthday_this_year = datetime(year=cur_date.year, month=user['birthday'].month, day=user['birthday'].day).date()
        day_of_birthday_next_year = datetime(year=cur_date.year+1, month=user['birthday'].month, day=user['birthday'].day).date()
        
        if day_of_birthday_this_year <= date_off and day_of_birthday_this_year >= cur_date \
            or day_of_birthday_next_year <= date_off and \
            day_of_birthday_next_year >= cur_date:
            
            day_of_birthday_this_year = day_of_birthday_this_year.weekday() 
            
            if day_of_birthday_this_year == 1:
                birthdays_dict['Tuesday'].append(user['name'])
            elif day_of_birthday_this_year == 2:
                birthdays_dict['Wednesday'].append(user['name'])
            elif day_of_birthday_this_year == 3:
                birthdays_dict['Thursday'].append(user['name'])
            elif day_of_birthday_this_year == 4:
                birthdays_dict['Friday'].append(user['name'])
            else:
                birthdays_dict['Monday'].append(user['name'])
    return birthdays_dict