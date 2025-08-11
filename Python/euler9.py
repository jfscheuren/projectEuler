#find pythagorean triplets, check if their sums are equal to 1000, if so, find their product


for x in range (1,500):
    for y in range (1,500):
        for c in range (1,500):
            if x*x + y*y == c*c:
                if x + y + c==1000:
                    print(x*y*c) 


