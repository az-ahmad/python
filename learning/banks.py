_users = {}

class Bank:
    def __init__(self,bankname):
        print(f'Bank: {bankname} created')
        self.bankname = bankname
    def __str__(self):
        print(f'You are at at {self.bankname} bank')

    def getUsers(self):
        for a,b in _users.items():
            if b[0] == self.bankname:
                print(f'User : {a}, Branch: {b[1]}')


class Branch(Bank):
    def __init__(self,bankname,branchname):
        print(f'{branchname} branch created')
        Bank.__init__(self,bankname)
        self.branchname = branchname
    
    def __str__(self):
        print(f'You are at at {self.branchname} bank')
    
    def getUsers(self):
        for a,b in _users.items():
            if b[0] == self.bankname and b[1]== self.branchname:
                print(a)

class Person(Branch,Bank):
    global users
    def __init__(self,name='John Smith',money=100,bankname='Halifax',branchname='Kensington'):
        Branch.__init__(self,bankname,branchname)
        self.name = name
        self.money = money
        _users[self.name] = [self.bankname,self.branchname]

    def __str__(self):
        return(f'Your name is {self.name}, you have £{self.money} at the {self.branchname} {self.bankname}')

    def deposit(self,amount):
        self.money += amount
    
    def withdraw(self,amount):
        if amount<=self.money:
            self.money -= amount
        else:
            print('Insufficient funds')

    def getUsers(self):
        print('Does nothing')

person1 = Person('Mr Red',300,'Barclays','Mayfair')
person2 = Person('Mr Blue',600,'Barclays','Mayfair')
person3 = Person('Mr Green',115,'Halifax','Bricky')
person4 = Person('Mr Purple',60,'Halifax','Mayfair')
person5 = Person('Mr Gold',10,'Metro','Egham')

print(person1.name)
print(person1.money)
person1.deposit(25)
print(person1.money)
person1.withdraw(600)

print(person1)

bank1 = Bank('Barclays')
bank1.getUsers()