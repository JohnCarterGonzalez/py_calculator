print('Welcome to the calculator!')
# Define the actions for the calculator 
def calculator():
    try:
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the second number: '))
        operator = input('Enter the operator (Think + - * /): ')
        if operator == '+':
            print('Your numbers added are ', num1+num2)
        elif operator == '-':
            print('Your numbers subtracted are ', num1-num2)
        elif operator == '*':
            print('Your numbers mutiplied are ', num1*num2)
        elif operator == '/':
            print('Your numbers divided are ', num1/num2)
        else:
            print('I did not understand that, please try again')
    except ValueError:
        print('You have a ValueError.')

while True:
   cont = input('Would you like to run a number? (y/n) ')

   if cont == 'y':
        calculator()
   elif cont == 'n':
        print('Goodbye.')
        break
   else:
        print('I did not understand that please try again')

