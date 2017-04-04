def sum_of_primes(n):
    sum1 = 0
    for i in range(0,len(n)):
        num = n[i]
        if num > 1:
            prime=True
            for j in range(2, int(num**0.5)+1):
                if num%j == 0:
                    prime=False
                    break
                    
            if prime:
              sum1=sum1+num
        else:
            sum1 = 0
    return sum1

"""class reminder:
    def __init__(self,remind,reminder):
        self.remind=remind
        self.reminder=reminder
       
    def what(self):
        whater=self.remind
        print(whater)"""