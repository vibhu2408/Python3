"""
import random

num = random.randint(1,7)
guess = None

while guess != num:
  guess = int(input("Guess a number b/w 1 to 7\n"))
  
  if guess == num:
    print("congrats you win!")
    break
  else:
      print("sorry!you lose")
"""

x = int(input("Enter the number:\n"))

guess = None
for i in range(0,7):
    while guess != x:
        guess = int(input("Guess a number between 1 to 100:\n"))

        if guess == x:
            print("Congrats you win!")
            break
        else:
            print("Sorry you lose!")




