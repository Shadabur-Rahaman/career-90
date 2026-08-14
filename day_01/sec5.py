# Create a list, add/remove items
ls = [1,2,3]
ls.append(4)
print(ls)
ls.pop()
print(ls)
ls.remove(2)
print(ls)

# Create a tuple, unpack it
ls = 1,2,3,

l = (1,2,3,4,5)
for i in l:
    print(i)

# Create a dict, access values, add keys
dt = {1:'a', 2:'b'}
print(dt[1])
dt[3]='c'

# Dict .keys(), .values(), .items()
print(dt.items())
print(dt.keys())
print(dt.values())

# Create a set, add/remove items
s = set()
st = {2,3,4,5,6}
st.add(9)
print(st)
st.pop()
print(st)
st.remove(4)
print(st)

# List indexing and slicing

ls = [1,2,4,5]
print(ls[0])
print(ls[1:3])
print(ls[0:4:2])