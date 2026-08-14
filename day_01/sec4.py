# If/elif/else based on a number

num = int(input('Enter num '))
if num<=59 and num>=18:
    print('Eligible to vote')
elif num>=60:
    print('Eligible to retire')
else:
    print('Under age')

# For loop with range (0 to 10)

for i in range(0,10):
    print(i)

# While loop with a counter
c = 0
while c<10:
    print(c)
    c+=1

# Break out of a loop
for i in range(10):
    if i == 2:
        break
    print('not break until: ',i)

# Continue to next iteration
for i in range(5):
    if i==4:
        continue
    print('\ncontinue until: ',i)

# Function that takes two numbers and returns their sum

def summ(a,b):
    return a+b
print('\n \t sum= ',summ(1,2))

# List comprehension to double all numbers in a list
num = [1,2,3,4,5]

double = [nums*2 for nums in num ]
print(double)