#parent class user 

class User: #class A
    name = "Mark"
    email = "mark@gmail.com"
    password = "123abcd"
    
    def getLoginInfo(self): #as instance
        entry_name = input("Enter Your name: ")
        entry_email = input("Enter your email")
        entry_password = input("Enter your password")
        if(entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect")
            
#child class employee
class Employee(User):
    base_pay = 11.00
    department = "General"
    pin_num = 3980
    
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter Your Pin: ")
        if (entry_email == self.email ):
            print("welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect")
            
customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()


        

            
                


    
