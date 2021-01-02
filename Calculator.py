while True:
    numer_1 = int(input('Please put your first number :'))
    numer_2 = int(input('Please put your second number :'))
    action = input('''
        For sum type '+', 
        for substract type '-', 
        for product type 'x', 
        for division type '/' 
        to exit type 'q' ''')
    ######################CALCULATOR#####################
    if action == '+':
        print('The result is', float(numer_1 + numer_2))
    elif action == '-':
        print('The result is', float(numer_1 - numer_2))
    elif action == 'x':
        print('The result is', float(numer_1 * numer_2))
    elif action == '/':
        print('The result is', float(numer_1 / numer_2))
    elif action == 'q':
        break
    print('Try again')

print('Calculator has ended')
