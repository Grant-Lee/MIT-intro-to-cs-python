def paying_min(balance, annualInterestRate, monthlyPaymentRate):
    year = 12
    month = 0
    total_paid = 0
    annualInterestRate = annualInterestRate/12.0
    min_pay = balance * monthlyPaymentRate
    while month < year:
        min_pay = balance * monthlyPaymentRate
        balance = balance - min_pay
        balance = balance + balance * annualInterestRate
        month = month + 1
        total_paid = total_paid + min_pay
        print "Month: %i" %month
        print "Minimum monthly payment: %.2f" %min_pay
        print "Remaining balance: %.2f" %balance
    return "Total paid: %.2f\nRemaining balance: %.2f" %(total_paid, balance)
print paying_min(4213, 0.2, 0.04)
    