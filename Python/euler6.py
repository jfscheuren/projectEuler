#The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 ... =385

#The square of the sum of the first ten natural numbers is, (1+2+..+10)^2 = 3025


#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385=2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


#sum of first 100 numbers:
sum=0
for x in range (1,101):
	sum +=x
#square the sum
sumsquared=sum*sum
print(sumsquared)

#square each of the first 100 numbers and sum together
sum2=0
for y in range (1,101):
	square=y*y
	sum2+=square

print(sum2)

answer=sumsquared-sum2
print(answer)
# 25164150
