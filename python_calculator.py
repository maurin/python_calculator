# This file has multiple functions! Lets code them indepenently
# This is a basic calculator with many functions

def add_num(a,b):
    c =  a+b
    print_num(a, '+', b, c)

def sub_num(a,b):
    c =  a-b
    print_num(a, '-', b, c)
    

def multiply_num(a,b):
    pass

def divide_num(a,b):
    pass

def print_num(a, symbol, b, c):
    pass

# This while loop will run until the exit selection is made
while(True):
    print('\nWelcome to my calculator')
    print('1: Add\n2: Subtract\n3: Multipy\n4: Divide\n5: Exit')

    selection = int(input('Input your selection:'))

    if (selection == 5):
        print ('Thank you come again!')
        break

    num_a = int(input('Input your first number: '))
    num_b = int(input('Input your second number: '))

    if (selection == 1):
        add_num(num_a, num_b)
    elif (selection == 2):
        sub_num(num_a, num_b)
    elif (selection == 3):
        multiply_num(num_a, num_b)
    elif (selection == 4):
        divide_num(num_a, num_b)
    else:
        print('Please enter a number 1-5!')
