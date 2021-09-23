#Add two numbers:
a = int(input("Enter first num:"))
b = int(input("Enter the second num:"))
print(a+b)

#maximum of two number
a = int(input("Enter first num:"))
b = int(input("Enter the second num:"))
if a < b:
    print(b)
else:
    print(a)

#simple Interest 
p = float(input("Principle amount "))
r = float(input("Rate % "))
t = float(input("Time "))
SI = p*r*t/100
print(float(SI))


#Compound Interest
p = float(input("Principle amount "))
r = float(input("Rate % "))
n = float(input("Number of times interest compounded per time period "))
t = float(input("Time "))
CI = p((1 + r/n)**(n*t))
print(float(CI))

#