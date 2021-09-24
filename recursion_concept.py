def sum_of_num(a, b):
    c = a + b
    print(c)

sum_of_num(2, 4)

def discriminant(a, b, c):
   x = (b**2 - 4*a*c)**0.5
   print("dispaly the value of discriminant on the output screen: ",x)
   return x

def Quadratic_equation(a, b, c):
    """
    ax**2 + bx + c
    """
    root1 = (-b + discriminant(a, b, c)) / 2*a
    root2 = (-b - discriminant(a, b, c)) / 2*a
    print(root1,root2)
    return (root1, root2)

Quadratic_equation(1, -5, 6)
print(Quadratic_equation)

