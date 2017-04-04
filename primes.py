import math
#imported math,although it can be imported without having to specify so

def main():
    count = 2#innitialise counter to 2, first prime number
    
    while True:
        isprime = True#set while iterator to boolean true for the start of the counter
        
        for x in range(2, int(math.sqrt(count) + 1)):#implementing finding prime numbers
            if count % x == 0: 
                isprime = False
                break
        
        if isprime:
            print (count)
        
        count += 1

main()#call and execute function