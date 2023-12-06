import csv

# open Titanic.csv file with csv.DictReader and read its content into a list of dictionary, titanic_data
titanic_data = []
with open('Titanic.csv') as f:
    rows = csv.DictReader(f)
    for r in rows:
        titanic_data.append(r)


def number_single_embarked_survived(place_embarked, age_threshold, titanic_data):
    """Returns the number of survived single women over age_threshold embarked at place_embarked
    (Single women are denoted by "Miss")

    >>> number_single_embarked_survived("Southampton", 40, titanic_data)
    4
    >>> number_single_embarked_survived("Cherbourg", 50, titanic_data)
    2
    >>> number_single_embarked_survived("Queenstown", 20, titanic_data)
    3
    """
    survived = 0
    for _dict in titanic_data:
        if _dict['gender'] == 'F' and _dict['embarked'] == place_embarked:
            if _dict['survived'] == 'yes' and _dict['age'] != '':
                if (float(_dict['age'])) > age_threshold:
                    if 'Miss' in _dict['first']:
                        survived += 1

    return survived


def class_survival_rate(passenger_class, titanic_data):
    """Returns the survival rate of a given passenger_class

    >>> survival_rate = class_survival_rate("1", titanic_data)
    >>> f"{survival_rate:.2f}"
    '0.63'
    >>> survival_rate = class_survival_rate("2", titanic_data)
    >>> f"{survival_rate:.2f}"
    '0.47'
    >>> survival_rate = class_survival_rate("3", titanic_data)
    >>> f"{survival_rate:.2f}"
    '0.24'
    """
    survive = 0
    total = 0
    for _dict in titanic_data:
        if _dict['class'] == passenger_class:
            total += 1
            if _dict['survived'] == 'yes':
                survive += 1

    return survive/total


def average_class_fare(passenger_class, titanic_data):
    """Returns the average fare for a given class, 1, 2 or 3

    >>> average = average_class_fare("1", titanic_data)
    >>> f"{average:.2f}"
    '84.15'
    >>> average = average_class_fare("2", titanic_data)
    >>> f"{average:.2f}"
    '20.66'
    >>> average = average_class_fare("3", titanic_data)
    >>> f"{average:.2f}"
    '13.68'
    """
    fare = [float(_dict['fare']) for _dict in titanic_data if _dict['class'] == passenger_class]
    return sum(fare)/len(fare)


def gender_survival_number(passenger_gender, titanic_data):
    """Returns the number of survivors for a given gender, M (male) or F (female)

    >>> gender_survival_number('M', titanic_data)
    109
    >>> gender_survival_number('F', titanic_data)
    233
    """
    survive = 0
    for _dict in titanic_data:
        if _dict['gender'] == passenger_gender:
            if _dict['survived'] == 'yes':
                survive += 1

    return survive


def common_last_name(titanic_data):
    """Returns most common last name

    >>> common_last_name(titanic_data)
    'Andersson'
    """
    name = {}
    for _dict in titanic_data:
        if _dict['last'] not in name:
            name[_dict['last']] = 1
        elif _dict['last'] in name:
            name[_dict['last']] += 1

    normal = 0
    most_name = ''
    for name, count in name.items():
        if count > normal:
            normal = count
            most_name = name

    return most_name


if __name__ == "__main__":
    import doctest
    doctest.testmod()