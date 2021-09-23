li = [1,2,3,4,"Vaibhav", "Gupta",5.5,True]

print(li)

#print length of the list 
print(len(li))

#indexing -> in python indexing done as 0 based on from left to right or -1 based on from right to left 
print(li[0])
print(li[2])

print(li[5])

for i in range(0, len(li)) :
    print(li[i])

print(li[-1])
print(li[-3])

print("#######")
for i in range(-1, -7, -1) :
    print(li[i], i)

    #nested list
li1 = [[1,2,3,4], [5,6,7,8], [9,6,8,3], [5,7]]
print(li1)
print(li1[2])
print(li1[0][3])
print(li1[3])

#li = {[1,2,3,4], [5,6,7,8], [9,6,8,3], [5,7]}
length = int(len(li1))

for i in range(length) :
    print(li1)
    for j in range(length) :
        print(li1[i])
        print(li1[i][1], end= " ")


for row in li1 :
    for el in row :
        print(el ,end = " ")
    #print()

#list are mutable
li[0] =99
print(li)

#slices of lists
li = [1,2,3,4,5,6,7,8,9]
print(li[0:4])#print from 0th index to (4-1)
print(li[1:])#print  form 1 to end 
print(li[:7])#print from begin to (7-1)th index
print(li[:])#print from begin to end
print(li[1:7:2])#start end jump

#Given a binary list of all the zeros ,1s and 2s sort the list in non descending order
#in single read of an array without taking any extraspaces  and no  counting elements is allowed 
#TC -0(n)
#Sc -0(n)
# #[1,1,2,0,1,0] -> [0,0,1,1,1l

li = [0,0,2,2,1,1,0,0,2,1,1] ##This algorithm known as DNF (Does National Flag algorithm)
lo , mid , hi =  0,0,len(li)-1
while mid <= hi :
    if li[mid] == 1 :
        mid += 1
    elif li[mid] == 2 :
        li[mid], li[hi] = li[hi], li[mid]
        hi -= 1
    else :
        li[mid], li[lo] = li[lo], li[mid]
        lo += 1
        mid += 1
    
print(li)
