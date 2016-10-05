import math     


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
