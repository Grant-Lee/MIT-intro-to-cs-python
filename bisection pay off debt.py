balance = 3962
annualInterestRate = 0.2
lower_bound = balance/12
upper_bound = (balance*(1+(annualInterestRate)/12)**12/12)
def bisection(x,y):
    i = (x+y)/2
    return i
lowest_payment = bisection(lower_bound, upper_bound)
month = 1
reset_balance = balance

while True:
    #print lowest_payment
    balance = reset_balance
    while month <= 12:        
        balance = balance - lowest_payment
        balance = balance + balance * annualInterestRate/12.0
        #print "month: %i %.2f" %(month, balance) 
        month = month + 1 
    if balance > 0 and balance < 1:
        break  
    if balance > 0:
        lower_bound = lowest_payment
        lowest_payment = bisection(lowest_payment, upper_bound)
    if balance < 0:
        upper_bound = lowest_payment
        lowest_payment = bisection(lower_bound, lowest_payment)
        
    month = 1
    
print "Lowest Payment: %.2f" %lowest_payment
#print lower_bound, bisection(lower_bound, upper_bound), upper_bound
#print bisection(lower_bound, lowest_payment)