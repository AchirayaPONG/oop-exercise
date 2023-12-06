import csv

# open Cities.csv file with csv.DictReader and read its content into a list of dictionary, cities_data
cities_data = []
with open('Cities.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities_data.append(r)
print(cities_data)

# open Countries.csv file with csv.DictReader and read its content into a list of dictionary, countries_data
countries_data = []
with open('Countries.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries_data.append(r)


def min_max_temp(cities_data):
    """Returns a list whose first and second elements are the min and the max
    temperatures of all the cities in cities_data.
    """
    temps = []
    for r in cities_data:
        temps.append(float(r['temperature']))
    return [min(temps), max(temps)]


def country_list(cities_data):
    """Returns a list of all the countries represented in cities_data.
    """
    countries = []
    for r in cities_data:
        if r['country'] not in countries:
            countries.append(r['country'])
    return countries


def average_country_temp(cities_data):
    """
    Return a dictionary whose key:value pair is country name:its average temp.
    The size of the returned dictionary must equal the number of countries
    represented.

    Notes: the test results below are printed out with two decimal places to
    get around floating-point errors.

    >>> temp_dict = average_country_temp(cities_data)
    >>> for key in sorted(temp_dict):
    ...    print(f"{key} {temp_dict[key]:.2f}")
    Albania 15.18
    Andorra 9.60
    Austria 6.14
    Belarus 5.95
    Belgium 9.65
    Bosnia and Herzegovina 9.60
    Bulgaria 10.44
    Croatia 10.87
    Czech Republic 7.86
    Denmark 7.62
    Estonia 4.59
    Finland 3.49
    France 10.15
    Germany 7.87
    Greece 16.90
    Hungary 9.60
    Ireland 9.30
    Italy 13.47
    Latvia 5.27
    Lithuania 6.14
    Macedonia 9.36
    Moldova 8.41
    Montenegro 9.99
    Netherlands 8.76
    Norway 3.73
    Poland 7.25
    Portugal 14.47
    Romania 9.22
    Serbia 9.85
    Slovakia 8.48
    Slovenia 9.27
    Spain 14.24
    Sweden 3.59
    Switzerland 7.25
    Turkey 11.73
    Ukraine 7.42
    United Kingdom 8.65
    """
    country_dict = {}
    for _dict in cities_data:
        temp_list = []
        if _dict['country'] not in country_dict:
            temp_list.append(float(_dict['temperature']))
            country_dict[_dict['country']] = temp_list
        else:
            country_dict[_dict['country']].append(float(_dict['temperature']))

    for country, temp in country_dict.items():
        country_dict[country] = sum(temp)/len(temp)

    return country_dict


def country_max_diff_temperature(cities_data):
    """Returns a tuple with information about a country whose minimum and
    maximum city temperatures differ the most in the following format: (the
    country whose minimum and maximum city temperatures differ the most, min
    temperature, max temperature, max temperature - min temperature)

    Notes: the test results below are printed out with two decimal places to
    get around floating-point errors.

    >>> result = country_max_diff_temperature(cities_data)
    >>> type(result)
    <class 'tuple'>
    >>> country, temp_min, temp_max, temp_diff = result
    >>> f"{country} {temp_min:.2f} {temp_max:.2f} {temp_diff:.2f}"
    'Turkey 5.17 18.67 13.50'
    """
    diff = 0
    country_dict = {}
    for _dict in cities_data:
        temp_list = []
        if _dict['country'] not in country_dict:
            temp_list.append(float(_dict['temperature']))
            country_dict[_dict['country']] = temp_list
        else:
            country_dict[_dict['country']].append(float(_dict['temperature']))

    country_name = ''
    min_temp = 0
    max_temp = 0
    for country, temp in country_dict.items():
        diff_temp = max(temp) - min(temp)
        if diff_temp > diff:
            diff = diff_temp
            country_name = country
            min_temp = min(temp)
            max_temp = max(temp)

    return country_name, min_temp, max_temp, diff


def western_eastern_most_cities(cities_data):
    """Returns a list of tuples with information about the westernmost and
    easternmost cities together with their associated countries in the
    following format:

    [(westernmost city, its country, its longitude), (easternmost city, its country, its longitude)]

    Notes: the test results below are printed out with two decimal places to
    get around floating-point errors.

    >>> results = western_eastern_most_cities(cities_data)
    >>> for city, country, lon in results:
    ...     print(f"{city} {country} {lon:.2f}")
    Lisbon Portugal -9.14
    Siirt Turkey 41.93
    """
    min_long = 0
    max_long = 0
    min_country = ''
    max_country = ''
    min_city = ''
    max_city = ''
    for _dict in cities_data:
        longtitude = float(_dict['longitude'])
        if longtitude < min_long:
            min_long = longtitude
            min_city = _dict['city']
            min_country = _dict['country']
        elif longtitude > max_long:
            max_long = longtitude
            max_city = _dict['city']
            max_country = _dict['country']

    return [(min_city, min_country, min_long), (max_city, max_country, max_long)]


def average_EU_city_temperature(cities_data, countries_data):
    """Returns a tuple with two elements: (the average temperature of all the
    cities in EU countries, the average temperature of all the cities not in
    EU countries)

    Notes: the test results below are printed out with two decimal places to
    get around floating-point errors.

    >>> result = average_EU_city_temperature(cities_data, countries_data)
    >>> type(result)
    <class 'tuple'>
    >>> eu, non_eu = result
    >>> f"{eu:.2f} {non_eu:.2f}"
    '9.69 9.03'
    """
    eu_temp = 0
    non_temp = 0
    eu_count = 0
    non_count = 0
    for country_dict in countries_data:
        if country_dict['EU'] == 'yes':
            for city_dict in cities_data:
                if city_dict['country'] == country_dict['country']:
                    eu_temp += float(city_dict['temperature'])
                    eu_count += 1
        elif country_dict['EU'] == 'no':
            for city_dict in cities_data:
                if city_dict['country'] == country_dict['country']:
                    non_temp += float(city_dict['temperature'])
                    non_count += 1

    return eu_temp/eu_count, non_temp/non_count


if __name__ == "__main__":
    import doctest
    doctest.testmod()
