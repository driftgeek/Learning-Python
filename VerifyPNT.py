def VerifyPNT(N):

   if (N < 2): #The number 2 is considered as the first prime number. So 0 and 1 have to excluded from the range.
        return False
   if (N == 2) or (N == 3): #N has to be prime numbers. 2 and 3 are prime numbers.
       return True
   if (N == 5) or (N == 7): # 5 and 7 are prime numbers.
       return True
   if (N % 2)  == 0 or (N % 3) == 0: #N cannot be multiples of 2 and 3. If it does, it will be considered as a composite number.
       return False
   if (N% 5) == 0 or (N % 7) == 0:#N cannot be multiples or 5 or 7 in order for this to work. The output will be considered False.
       return False

   for i in range (2, int(N**(0.5))+1):
        if (N%i) == 0: #N cannot be divisible by i.
            return False

   return True





piN = 0 #This is my pi(N)

N1= 10
N2= 100
N3= 1000
N4= 10000
N5= 100000

for i in range (1,N1):
        if VerifyPNT(i) == True:
##          print(i), ##I wanted to verify the prime numbers in the range from 1-10.
          piN += 1
tempN1 = piN/(math.log(N1))

print [N1, piN, tempN1]

for i in range (11,N2): # I excluded the previous range 1-10 from finding out the range from (1,100). Previously, I noticed I was getting an added number of prime numbers. It is suppose to be 25 but I was getting 29 instead. 
        if VerifyPNT(i) == True:
##            print (i),# I wanted to verify the prime numbers in the range from 1-100.
            piN += 1
tempN2 = piN/(math.log(N2))

print [N2, piN, tempN2]

for i in range (101,N3):
        if VerifyPNT(i) == True:
####            print(i), # Just verifying the prime numbers in the range.
            piN += 1
tempN3 = piN/(math.log(N3))

print [N3, piN, tempN3]

for i in range (1001, N4):
        if VerifyPNT(i) == True:
##            print(i), # Just verifying the prime numbers in the range.
            piN += 1
tempN4 = piN/(math.log(N4))

print [N4, piN, tempN4]

for i in range (10001, N5):
        if VerifyPNT(i) == True:
##            print(i), # Just verifying the prime numbers in the range.
            piN += 1

tempN5 = piN/(math.log(N5))            
print  [N5, piN, tempN5]

