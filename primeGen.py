def genPrimes():
    x = 4
    p = [2,3]
    isPrime = None
    while x < 10000:
        isPrime = True
        for i in p:
            if (x % i) == 0:
                x += 1
                isPrime = False
                break
        if isPrime:
            p.append(x)
            x += 1
    for j in p:
        yield j
x = genPrime()

                
            