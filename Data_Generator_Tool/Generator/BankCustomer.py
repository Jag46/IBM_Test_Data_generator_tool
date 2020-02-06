from faker import Faker
global obj
obj = Faker()

def get_customerNumber():
    return obj.random_int(10**9, ((10**10)-1))


def get_IbanNumber():
    return obj.iban()


def get_accountNumber():
    num =  obj.random_int(10**7,((10**8)-1))
    num = str(num)
    return"07-04-36 "+num  

