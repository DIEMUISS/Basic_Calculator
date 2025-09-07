Valid_op = ('+','-','*','/')
#a while loop to run calculator repeatly till terminated
while True:
    #user input
        try:
            num1 = float(input('What is your first number: '))
            num2 = float(input('What is your second  number: '))
            operator = str(input('Using what operator: '))
        #just in case they dont put in the right data type
        except ValueError:
            print('invalid values entered')
            continue
        #cheack is positive number
        if num1 < 0 and num2 < 0:
            print('invalid number')
            continue
        #if it not one of the provided operators
        if operator not in Valid_op:
            print('invalid operator')
            continue
            #begin calculation if stapents
        else:
            if operator == '+':#addition
                print(num1 + num2)
            elif  operator == '-':#substraction
                print(num1 - num2)
            elif  operator == '*':#multiplication
                print(num1 * num2)
            else:#division
                if num2 == 0:#cheack if it is invalid division
                    print('invalid division')
                else:print(num1/num2)
            again = input('try again(y/n)').lower()
            #option to try again
            if again == 'n':#stop if no
                break


