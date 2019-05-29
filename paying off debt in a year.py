balance = 3926
annualInterestRate = 0.2
lowest_payment = 0
month = 1
reset_balance = balance
while True:
    balance = reset_balance
    while month <= 12:        
        balance = balance - lowest_payment
        balance = balance + balance * annualInterestRate/12.0
        #print "month: %i %.2f" %(month, balance) 
        month = month + 1   
    if balance < 0:
        break
    month = 1    
    lowest_payment = lowest_payment + 10
print "Lowest Payment: %i" %lowest_payment