v = "Vaibhav"
g = "Gupta"
#Concatenate two string each other
c = print(v + g)

#replicate two string
print((v + " ") * 3)

#Replication on list
li = [1,2,3]
li = print(li * 3)

print(li + [2,3,4]) #it makes a new list
print(li)

li.extend([2,3,4])
print(li)

li = li + [1,2,3]
print(li)

#Mutability in strings
li =  [1,2,33,4,5,6] #this work bcoz list are mutable /updated
li[2] = 22

s = "Vaibhav" #this wont work string are immutable
s[2] = 'r'

#we can also assign a value to the list
li = [22,33,44,55,66]
print(li[1:5])