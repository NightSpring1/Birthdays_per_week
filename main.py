from faker import Faker
from datetime import date
from calendar import day_name


def get_fake_users(quantity: int, seed=None) -> list:
    fake = Faker()
    Faker.seed(seed)
    users = []
    for _ in range(quantity + 1):
        users.append({'name': fake.first_name(),
                      'birthday': fake.date_of_birth()})
    return users


def get_birthdays_per_week(users: list) -> None:
    today = date.today()
    # today = date(year=2023, month=3, day=20)
    birthdays_this_week = {}

    # fill the dictionary with weekdays starting from current day
    for i in range(0, 7):
        birthdays_this_week[(today.weekday() + i) % 7] = []

    for user in users:
        # Getting this year birthday date
        try:
            birthday = user['birthday'].replace(year=today.year)
        except ValueError:
            birthday = user['birthday'].replace(year=today.year, day=28)  # Leap Year error

        # index from which birthdays will be looking around, always 0 for current day
        day_index = (birthday - today).days

        # looking for dates that are between -2 and + 6 days from current date
        if -2 <= day_index <= 6:

            # all birthdays which are on working day
            if birthday.weekday() < 5 and day_index in range(0, 7):
                birthdays_this_week[birthday.weekday()].append(user['name'])

            # all birthdays which are on weekend and check if the weekend of current week or previous
            elif birthday.weekday() >= 5 and day_index in range(-2 + today.weekday() % 2, 5 + today.weekday() % 2):
                birthdays_this_week[0].append(user['name'])

    # Print birthdays in function according to the home-task
    for day, name in birthdays_this_week.items():
        print(f'{day_name[day]}: {", ".join(name)}')


if __name__ == "__main__":
    get_birthdays_per_week(get_fake_users(1000))

# print(user['name'], birthday, birthday.strftime('%A'), day_index)
