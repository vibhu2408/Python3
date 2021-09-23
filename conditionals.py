if (2 < 4) :
    print("Hello")
elif (4 > 2) : #Equivalent to else if
    print("Hi")


if(True) :
    if(8 > 5) :
        if(9 > 7) :
            print("Reached on time")
else :
    print("You are late")

#checked whether number is fibonacci or not?
# The ratio of sequential fibonacci number(2/1,3//2,5/3...etc) are approches to golden ratio.
from math import sqrt 
n = 12
val1 = 5 * (n*n) + 4
val2 = 5 * (n*n) - 4

v1 = int(sqrt(val1))
v2 = int(sqrt(val2))

if(v1 * v1 == val1 or v2 * v2 == val2) :
    print("yes")
else :
    print("No")