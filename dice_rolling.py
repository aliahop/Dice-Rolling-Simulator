import random
while True:
    name = input("Hi! Whats your name: ")

    print('{}, do you want to roll dice?'.format(name))
            
    answer = input('')

    if answer.lower() == 'yes':
        number = range(1,7)
        number = random.choice(number)
        print('You have {}'.format(number))
    elif answer.lower() == 'no':
        print ('Thank you for game')
    else:
        print('Yes or No?')






