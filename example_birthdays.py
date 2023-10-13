from get_birthdays_per_week import get_birthdays_per_week
from utils.fakedata import dbList,fakerList

users_list = dbList()
print(("* "*5)+"dbList"+(" *"*5))
print(("* "*5)+"forward 7 days"+(" *"*5))
get_birthdays_per_week(users_list)
print(("* "*5)+"next week"+(" *"*5))
get_birthdays_per_week(users_list, nextweek=True)

print(("* "*5)+"fakerList"+(" *"*5))
print(("* "*5)+"forward 7 days"+(" *"*5))
users_list = fakerList(50)
get_birthdays_per_week(users_list)
print(("* "*5)+"next week"+(" *"*5))
get_birthdays_per_week(users_list, nextweek=True)
