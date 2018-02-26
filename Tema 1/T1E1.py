def machine_precision():
    power = 0;
    startValue = 10;
    while (1 + startValue**((-1)*power)) != 1.0:
        print('Machine precision is bigger than ' + str(power) + '.')
        power = power + 1
    else:
        print('Machine precisio is ' + str(power) + '.')

machine_precision()