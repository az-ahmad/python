class Bank:
    def __init__(self,bankname):
        self.bankname = bankname

    def __str__(self):
        print(f'You are at at {self.bankname} bank')
        print('To list the users and their respective branches, call getUsers() on this object')

    def getUsers(self):
        with open('bankdata.txt', 'r') as file:
            for line in file:
                if line.split(',')[2] == self.bankname:
                    print('Name:', line.split(',')[0], ', Money:', line.split(',')[1], ', Branch:', line.rstrip().split(',')[3])
        file.close()
        branchQuery = input('\nIf you would like to query a specific branch, please enter the branch\'s name: ')
        branch = Branch(self.bankname,branchQuery)
        branch.getUsers()


class Branch(Bank):
    def __init__(self,bankname,branchname):
        Bank.__init__(self,bankname)
        self.branchname = branchname
    
    def __str__(self):
        print(f'You are at at {self.branchname} bank')
        print('To list the users of this branch, call getUsers() on this object')
    
    def getUsers(self):
        with open('bankdata.txt', 'r') as file:
            for line in file:
                if line.rstrip().split(',')[3] == self.branchname and line.split(',')[2] == self.bankname:
                    print('Name:', line.split(',')[0], ', Money:', line.split(',')[1])


class Person(Branch,Bank):    
    def __init__(self,name='John Smith',money=100,bankname='Halifax',branchname='Kensington'):
        Branch.__init__(self,bankname,branchname)
        self.name = name
        self.money = money
        with open('bankdata.txt', 'a+') as file:
            file.write(f'{self.name},{self.money},{self.bankname},{self.branchname}\n')
            file.close()
        
    def __str__(self):
        return(f'Your name is {self.name}, you have £{self.money} at the {self.branchname} {self.bankname}')

    def deposit(self,amount):
        self.money += amount
    
    def withdraw(self,amount):
        try:
            if amount<=self.money:
                self.money -= amount
            else:
                print('Insufficient funds')
        except:
            print('Something went wrong!')

    def getUsers(self):
        raise NotImplementedError("Function can only be called on Bank or Branch instances")


def main():
    try:
        print('\nHello and welcome to Online Banking\n')
        print('Please type \'0\' to check your account')
        print('Please type \'1\' to create a new account')
        print('Please type \'2\' to query a bank\'s data')
        bankingScreen = int(input('Enter your selection: '))
        if bankingScreen == 1:
            newCustomer()
        elif bankingScreen == 2:
            bankQuery = input('\nWhich bank would you like to query? ')
            bank = Bank(bankQuery)
            bank.getUsers()
        elif bankingScreen ==0:
            withdrawNameQuery = input('\nPlease enter your name as it appears in your bank account: ')
            with open('bankdata.txt', 'r') as file:
                for line in file:
                    if line.split(',')[0] == withdrawNameQuery:
                        print('Name:', line.split(',')[0], ', Money:', line.split(',')[1], ' Bank:', line.rstrip().split(',')[2] ,', Branch:', line.rstrip().split(',')[3])
            print('\nPlease type \'1\' to withdraw money')
            print('Please type \'2\' to deposit money\n')
            screenSelection = int(input('Enter your selection: '))
            if screenSelection==1:
                withdrawMoney(withdrawNameQuery)
            elif screenSelection == 2:
                depositMoney(withdrawNameQuery)
    except ValueError:
        raise ValueError


def withdrawMoney(name):
    withdrawAmount = int(input('\nHow much would you like to withdraw? '))
    with open('bankdata.txt', 'r') as file :
        filedata = file.read().splitlines()
        file.close()
    for line in filedata:
        if line.split(',')[0] == name and int(line.split(',')[1])>=withdrawAmount:
            newAmount = int(line.split(',')[1]) - withdrawAmount
            newdata = line.replace(line.split(',')[1], str(newAmount))
            print(f'{name}, you now have £{newAmount} in your bank account.')
            with open('bankdata.txt', 'w') as file :
                for items in filedata:
                    if items.split(',')[0] != name:
                        file.write(f'{items}\n')
                file.write(f'{newdata}\n')
                file.close()
        elif line.split(',')[0] == name and int(line.split(',')[1])<withdrawAmount:
            print('Insufficient funds!')


def depositMoney(name):
    depositAmount = int(input('How much would you like to deposit? '))
    with open('bankdata.txt', 'r') as file :
        filedata = file.read().splitlines()
        file.close()
    for line in filedata:
        if line.split(',')[0] == name:
            newAmount = int(line.split(',')[1]) + depositAmount
            newdata = line.replace(line.split(',')[1], str(newAmount))
            print(f'{name}, you now have £{newAmount} in your bank account.')
            with open('bankdata.txt', 'w') as file :
                for items in filedata:
                    if items.split(',')[0] != name:
                        file.write(f'{items}\n')
                file.write(f'{newdata}\n')
                file.close()


def newCustomer():
    try:
        print('\nPlease enter the following details to create your brand new Online Banking account')
        newName = input('Please enter your full name: ')
        newMoney = int(input('How much money will you put in your bank account? '))
        newBank = input('What company is your bank? ')
        newBranch = input('Where is your local bank branch located? ')
    except ValueError:
        raise ValueError
    person1 = Person(newName,newMoney,newBank,newBranch)


if __name__=='__main__':
    main()


