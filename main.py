from datetime import datetime, timedelta
from user_generator import get_friends
from PRRGENERATED import PEOPLE_2000


def get_birthdays_per_week(users: list) -> None:
    current_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    # current_date = datetime(year=2023, month=3, day=20)
    birthdays_this_week = dict()
    weekend = ('Saturday', 'Sunday')
    for i in range(0, 7):
        birthdays_this_week[(current_date + timedelta(days=i % 7)).strftime('%A')] = []
    for person in users:
        try:
            birthday = person['birthday'].replace(year=current_date.year)
        except ValueError:
            birthday = person['birthday'].replace(year=current_date.year)  # Leap Year error
        weekday = birthday.strftime('%A')
        weekday_index = (birthday - current_date).days  # =0 for current day
        weekday_now = current_date.weekday()
        if weekday_index in range(0, 7) and weekday not in weekend:
            # print(person['name'], person['birthday'].date(), weekday, weekday_index)
            birthdays_this_week[weekday].append(person['name'])
        elif weekday_index in range(-2 + weekday_now % 2, 5 + weekday_now % 2) and weekday in weekend:
            # print(person['name'], person['birthday'].date(), weekday, weekday_index)
            birthdays_this_week['Monday'].append(person['name'])
    for day in birthdays_this_week:
        print(f'{day}: {", ".join(birthdays_this_week[day])}')


# people = get_friends(2000)
get_birthdays_per_week(PEOPLE_2000)
