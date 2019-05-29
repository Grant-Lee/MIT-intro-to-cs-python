def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here
    #any zero power return 1
    if exp == 0:
        return 1

    else:
        #if exp even numbers
        if exp % 2 == 0:
            print "even", exp
            return recurPowerNew(base*base, exp/2)
        #if exp odd numbers
        else:
            print "odd", exp
            return base * recurPowerNew(base, exp - 1)

print recurPowerNew(6.69,7), 2**4