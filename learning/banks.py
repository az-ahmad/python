
class Bank:
    def __init__(self,bankname):
        print(f'Bank: {bankname} created')
        self.bankname = bankname
    def __str__(self):
        print(f'You are at at {self.bankname} bank')

class Branch(Bank):
    def __init__(self,bankname,branchname):
        print(f'{branchname} branch created')
        Bank.__init__(self,bankname)
        self.branchname = branchname
    
    def __str__(self):
        print(f'You are at at {self.branchname} bank')

class Person(Branch,Bank):
    def __init__(self,name='John Smith',money=100,bankname='Halifax',branchname='Hounslow'):
        Branch.__init__(self,bankname,branchname)
        self.name = name
        self.money = money
    
    def __str__(self):
        return(f'Your name is {self.name}, you have £{self.money} at the {self.branchname} {self.bankname}')

    def deposit(self,amount):
        self.money += amount
    
    def withdraw(self,amount):
        if amount<=self.money:
            self.money -= amount
        else:
            print('Insufficient funds')

person1 = Person('Aziz',300,'Barclays','Feltham')

print(person1.name)
print(person1.money)
person1.deposit(25)
print(person1.money)
person1.withdraw(600)
print(person1.branchname)
print(person1.bankname)
print(person1)
