
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009= 91* 99.

#Find the largest palindrome made from the product of two 3-digit numbers
from math import *
palindromes= []
x=999
y=999


#loop through products and add palindromes to array
while x > 99:
    while y>99:
        test=x*y
        stringTest= str(test)


### product is number of chars
        if len(stringTest)%2==0:
            palindrome=False
            myLen=len(stringTest) - 1
            half=ceil(myLen/2)
            j=0
            while j<half:
                if stringTest[j]==stringTest[myLen]:
                    j+=1
                    myLen-=1
                    palindrome= True

                else:
                    palindrome=False
                    break
          
    
### product is odd number of chars        
        else:
            plaindrome=False
            myLen=len(stringTest) - 1
            half=floor(myLen/2)

            j=0

            while j<=half:

                if stringTest[j]==stringTest[myLen]:
                    j+=1
                    myLen-=1
                    palindrome=True
                else: 
                    palindrome=False
                    break
                    
            if palindrome==True:
                palindromes.append(stringTest)

        y-=1
        if palindrome==True:
            palindromes.append(stringTest)    
             
    x-=1
    y=999    
        
    
  

### find and print the largest number in the array

start=0

for abc in palindromes:
    myint= int(abc)
    if myint > start:
        start=myint

### Print the anser
print(str(start))        