'''

 Simple Calculator v1
    This calculator provides the most basic mathematical functions. Thank you for listening to my TED talk.
    Built using Anaconda distribution and PyCharm CE

'''

def greeting():
    print('This is SimpleCalc v0.0.0.0.1.')
    # print('Input your option: ')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    choice()

def choice():
    while True:
        userChoice = int(input('Enter your choice: '))
        if userChoice == 1:
            addition()
            break
        elif userChoice == 2:
            subtraction()
            break
        elif userChoice == 3:
            multiply()
            break
        elif userChoice == 4:
            division()
            break
        else:
            continue

def addition():
    i=0
    print('Addition chosen')
    numbers = input('Enter the numbers you wish to add together, seperated by commas: ')
    values = [value for value in numbers]
    for items in values:
        i+=items
    print(i)
    reset()

def subtraction():
    print('Subtraction chosen')
    numbers = input('Enter the numbers you wish to subtract from each other, seperated by commas: ')
    values = [value for value in numbers]
    i=values[0]
    for items in values[1:]:
        i-=items
    print(i)
    reset()

def multiply():
    print('Multiplication chosen')
    numbers = input('Enter the numbers you wish to multiply, seperated by commas: ')
    values = [value for value in numbers]
    i=1
    for items in values:
        i*=items
    print(i)
    reset()

def division():
    print('Division chosen')
    numbers = input('Enter the numbers you wish to divide, seperated by commas: ')
    values = [value for value in numbers]
    i=values[0]
    for items in values[1:]:
        i/=items
    print(i)
    reset()

def reset():
    answer = input('Would you like to perform another calculation?: Y/N ')
    if answer == 'y':
        print('\n')
        greeting()
    else:
        print('Thank you for using SimpleCalc')

if __name__ == "__main__":
    greeting()