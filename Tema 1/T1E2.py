import random

def multiplication():
    a = random.uniform(0, 10000000000000)
    b = random.uniform(0, 10000000000000)
    c = random.uniform(0, 10000000000000)
    print('Generated: ' + str(a) + '   ' + str(b) + '   ' + str(c))
    while (a * b) * c == a * (b * c):
        a = random.uniform(0, 10000000000000)
        b = random.uniform(0, 10000000000000)
        c = random.uniform(0, 10000000000000)
        print('Generated: ' + str(a) + '   ' + str(b) + '   ' + str(c))
    else:
        print('\nFound unassociative multiplication:\n')
        print('a = ' + str(a) + '\nb = ' + str(b) + '\nc = ' + str(c))

multiplication()
