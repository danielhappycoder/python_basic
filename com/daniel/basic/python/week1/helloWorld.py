numbercalculation_box =[] # this is to prepare a box to put numbers in it

while True:
    print('Hello guy i can calculate any 2 whole number you type, and tell you the answer')

    number1 = input('type the first number here:  ')
    number2 = input('type the second number here:  ')

    print(type(number1))
    print(type(number2))

    number1 = int(number1)
    number2 = int(number2)

    print('result of add ', number1 + number2)
    print('result of minus ', number1 - number2)
    print('result of multiplication ', number1 * number2)
    print('result of division', number1 / number2)

    numbercalculation_box.append(number1)
    numbercalculation_box.append(number2)
    print('i have done calculating this much number for you ', len(numbercalculation_box))