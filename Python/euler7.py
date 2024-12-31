limit = 100

nums = [True for i in range(limit+1)] 

for p in range(2, limit+1):
    if nums[p]:
        print(p)
        for j in range(p*p, limit+1, p): 
            nums[j] = False
