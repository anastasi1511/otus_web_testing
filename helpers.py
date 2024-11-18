import random
import string
from faker import Faker


def random_string(lenght=10):
    return "".join([random.choice(string.ascii_letters) for _ in range(lenght)])


def random_phone():
    return "".join([random.choice(string.digits) for _ in range(10)])


def random_email():
    return random_string() + "@" + random_string(5) + "." + random.choice(["com", "ua", "org", "ru"])


def create_random_user():
    faker = Faker()
    fake_user = dict()
    fake_user["name"] = faker.first_name()
    fake_user["address"] = faker.address()
    fake_user["phone"] = faker.phone_number()
    fake_user["last_name"] = faker.last_name()
    return fake_user


def create_random_name_of_good():
    return random.choice(["AndroidPhone12", "Apple watch ultra", "Bluetooth earbudsPro"])


def create_random_model():
    return random.choice(["15", "12", "11"])
