#String Formating
#There are no. of ways for string formating 
#1=> using % operator 
# %s, %d, %f are format specifier
s = "Vaibhav"
year = 2021
happiness = 100.00
greeting = "Hello, %s to %d and we hope your happiness matric is %.2f" % (s, year, happiness)
print(greeting)

#2->using format function

greeting = "Hello, {x} to {y}".format(x = s,  y =  year)
print(greeting)
greeting = "Hello, {} to {} and we hope your happiness matric is {}".format(s, year , happiness)
print(greeting)
print(format(12, "b"))

#3->F-String
greeting = f"Hello, {s} to {year} and we hope your happiness matric is {happiness}"
print(greeting)
binary = 0b101
greeting = f"Hello, {s}  {~binary:0b} to {year} and we hope your happiness matric is {happiness}"
print(greeting)
