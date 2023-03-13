import names
from datetime import datetime
from random import randint


def get_friends(quantity: int) -> list:
    friends = []
    while len(friends) != quantity:
        try:
            friends.append({'name': names.get_first_name(),
                            'birthday': datetime(year=randint(1950, 2015),
                                                 month=randint(1, 12),
                                                 day=randint(1, 31))})
        except ValueError:
            pass
    return friends
