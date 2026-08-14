# Count word frequency in a sentence (dict + loops)

s = 'python is is easy'
wd = s.split()
f = {}
for w in wd:
    if w in f:
        f[w] += 1
    else:
        f[w] = 1
print(f)

# Remove duplicates from a list keeping order (list + loops)

list = [1,1,3,4]
for i in set(list):
    print(i)

# Simple calculator using dict of operators (dict + function)

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

op = {
    '+':add,
    '-':sub,
    '*':mul,
    '/':div
}

a = float(input('enter first number '))
operator = input('enter operator: ')
b = float(input('enter seconf number '))

if operator in op:
    res = op[operator](a,b)
    print("Result: ",res)
else:
    print('invalid operator')
 
    
# FizzBuzz 1 to 100 (control flow)
for i in range(1,101):
    if i%3 == 0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)
        
# Separate numbers into even/odd dicts (dict + loops)

nums = [1,2,3,4,5,6]
res = {
    'even':[],
    'odd':[]
}
for n in nums:
    if n%2 == 0:
        res['even'].append(n)
    else:
        res['odd'].append(n)
print(res)