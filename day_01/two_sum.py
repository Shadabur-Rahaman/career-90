n = [1,2,3,4,5]
target = 7
def two_summ(n,target):
    for i in range(len(n)):
        for j in range(i+1,len(n)):
            summ = n[i]+n[j]
            if summ == target:
                return[i,j]
    return []
r = two_summ(n,target)
print(r)

def two_summm(n,target):
    seen = {}
    for i,a in enumerate(n):
        diff = target - n[i]
        if diff in seen:
            return[seen[diff],i]
        seen[a]=i
r = two_summm(n,target)
print(r)