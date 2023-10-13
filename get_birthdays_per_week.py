from datetime import datetime, timedelta
from collections import defaultdict
from utils.cli_text_format import cli_text_format


def get_birthdays_per_week(users:list, nextweek:bool=True, dict_output:bool=False) -> None or dict:
    today = datetime.now().date()
    result = defaultdict(list)

    if nextweek: # includes current weekends and Monday-Friday nextweek
        next_monday = today + timedelta(days=-today.weekday(), weeks=1)
        max_date = next_monday + timedelta(days=4) # next_friday
        min_date = next_monday - timedelta(days=2) # weekends_start
    else:  # forward 7 days
        min_date = today #today
        max_date = min_date + timedelta(days=7)
    
    for user in users:
        if not isinstance(user["birthday"],datetime):
            print(f"\n{cli_text_format.FAIL}Error >>> {cli_text_format.ENDC}Incorrect type \"birthday\" - not instance of datetime\n")
            continue 

        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=min_date.year)

        if  birthday_this_year < min_date or birthday_this_year > max_date:
            continue
        
        weekday_num = birthday_this_year.weekday()  
        if weekday_num in [5,6]:
            birthday_this_year = birthday_this_year + timedelta(days=(7 - birthday_this_year.weekday()))
            
        weekday_name = birthday_this_year.strftime('%A')
        result[weekday_name].append(f"{user['name']} - {user['birthday']}")
    
    if dict_output:
        return result
    
    if len(result):
        for key, val in result.items():
            print(f"{cli_text_format.OKCYAN}{key}{cli_text_format.ENDC}: {', '.join(val)}")
    else:
        print("Nobody has a birthday")
# end get_birthdays_per_week
