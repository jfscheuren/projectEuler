

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

from math import *

x=2
number=600851475143  

### you only need to check up to the floor of the sqrt of the number
testnum= floor(sqrt(number))
print(testnum)
factors= []
listofPrimes=[]

#get all the factors
while x<=testnum:
        if number%x==0:
            print(str(x)+ "is a factor")
            factors.append(x)
        x+=1
 
## print the factors
print("All the factors " + str(factors))

prime=True

i=2

### check list of factors for prime numbers
for j in factors:
    print(str(j))
    i=2
    while i<j:
# check for factors
        if (j % i) == 0:
            print(j,"is not a prime number")
            prime=False
            break
        else:
            i+=1
    if (prime):
        listofPrimes.append(j)




print("List of prime factors " + str(listofPrimes))

print("Largest prime factor: "  + str(listofPrimes.pop()))


