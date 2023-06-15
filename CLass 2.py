class User:
    name = 'no name provided'
    email = ' '
    password = '1234abcd'
    account_number = 0
    
class Employee(User):
    Base_pay = 11.00
    deparment = 'general'
    
class Customer(User):
    mailing_adress = ''
    mailing_list = True
    

    