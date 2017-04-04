def CalculateRepayment(principal,time,rate):
    #calculate interest
    Interest = principal * rate/100 * time/12
    amount = Interest + principal
    return amount

print(CalculateRepayment(100000,12,12))