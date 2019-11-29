#create a class

class User:
    #constructer
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f"Hello, my name is {self.name} and I am {self.age}."

#extend class (like inheritence)
class Customer(User):
    def __init__(self,name,email,age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    
    def set_balance(self, balance):
        self.balance=balance

furkan = User("Furkan","frkn@gmail.com",20)
hakan = Customer("Hakan","hkn@gmail.com",17)
hakan.set_balance(5000)
print(hakan.greeting() + " My balance is " + str(hakan.balance)+".")