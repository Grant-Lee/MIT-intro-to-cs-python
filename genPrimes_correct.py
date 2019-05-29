def genPrimes():
    last = 1
    prime = []
    while True:
        last += 1
        for i in prime:
            if last % i == 0:
                break
        else:
            prime.append(last)
            yield last
            
x = genPrimes()