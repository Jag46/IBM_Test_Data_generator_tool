from faker import Faker
from barnum import gen_data

global obj
obj = Faker()

def get_dateofbirth():
    return gen_data.create_birthday(min_age=18, max_age=75)

def get_building_number():
    return obj.building_number()

def get_city():
    return obj.city()

def get_state():
    return obj.state()

def get_country():
    return obj.country()

def get_country_code():
    return obj.country_code(representation="alpha-2")

def get_city_prefix():
    return obj.city_prefix()

def get_city_suffix():
    return obj.city_suffix()

def get_postalcode():
    return obj.postalcode()

def get_secondary_address():
    return obj.secondary_address()

def get_street_address():
    return obj.street_address()

def get_street_name():
    return obj.street_name()

def get_zipcode():
    return obj.zipcode()


