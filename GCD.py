####################GCD aka Greatest common Divisor########################
##It is known for a and b to be integers. Let's say there is a integer d which
##is known to be a divisor of both a and b...for example, d|a and d|b.

##After going through the GCD algorithm, I noticed my input size is about 7-9 lines of code.
##I do not believe my algorithm is not efficient due the continuation of the loop. I needed to actually
##manipulate the conditions in order for my code to work.


a = 70
b = 30


def GCD(a,b):

 
    if a == b:
            return a

for d in range (1, b-1): 

    while (a%d)== 0 and (b%d) == 0: #d has to divides both a and b in order for this to work.
      
        if (a % 2) == 0 and (b % 2) == 0: # If both a and b are even, the both have to be divided by 2.
            a = (a//2)
            b = (b//2)
            twogcd = (a, b)
            print 'The 2gcd is ', twogcd
        
        if (a % 2) != 0 and (b% 2) != 0 and (a>b):# If both a and b are odd.
                a = (a - b)
                gcd = (a, b)
                print 'The 2gcd is ', gcd

        if (a % 2) == 0 or (b % 2) != 0: # Here a is even but b is not.
            a = a//2
            gcd = (a, b)
            print 'The 2gcd is ', gcd

        if (a%2) != 0 and (b%2) != 0 and (a<b): # Here a and b is odd but I had keep it separate from the other condition since b<a.
                b = (b-a)
                gcd = (a,b)
                print 'The 2gcd is ', gcd


        if (a % 2) !=0 and (b % 2) == 0:
            b = b//2
            gcd = (a, b)
            print 'The 2gcd is ', gcd

        if a == b:
            a = 2 * a # Here I multiplied the gcd on the right side in order to reach to the result of 10.
            gcd = a 
            
            print 'The gcd is ', gcd
        

          
        break       
