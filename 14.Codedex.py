## Setting
print("Hi")

import random

## Hello World
print("Hello World")

## Pattern
print("            1")
print("        2", "  3")
print("    4", "  5", "  6")
print(" 7", " 8", "  9", " 10")

#Initials
print("DDDD", "     L")
print("D", "  D", "    L")
print("D", "  D", "    L")
print("D", "  D", "    L")
print("D", "  D", "    L")
print("D", "  D", "    L")
print("DDDD", "     LLLLL")

# Data Types

name = "Erlich Bachman"
print(name)
user_id = 16180339887
print(user_id)
progress = 0,75
print(progress)
exp = 60
print(exp)
verified = True
print(True)

print(name, user_id, progress, exp, True)

## Operators

temperature = (36 - 32)/1.8
print(temperature)

## Exponents

mass = 85
heigh = 1.82
body_mass_index = (mass / heigh ** 2)
print(body_mass_index)

## Pythagorean Theorem (User Input)

side_a = int(input("¿Cuanto mide el lado a? "))
side_b = int(input("¿Cuanto mide el lado b? "))
hipothenuse_c = (side_a ** 2 + side_b ** 2) // 2
print(side_a)
print(side_b)
print(hipothenuse_c)

## Currency
# 4,348.50 Peso colombiano = 1 dólar
# 3.76 Sol peruano = 1 dólar
# 6.11 Reales = 1 dólar
def my_money(pesos=0, soles=0, reais=0):
    if pesos:
        print(pesos * 4348.5)
    if soles:
        print(soles * 3.76) 
    if reais:
        print(reais * 6.11)

pesos = float(input("¿What do you left in Pesos?: "))
soles = float(input("¿What do you left in Soles?: "))
reais = float(input("¿What do you left in Reais?: "))

my_money(pesos=pesos)
my_money(soles=soles)
my_money(reais=reais)

print(sum([pesos, soles, reais]))

## Control Flow

num = random.randint(0, 1)   # Generates a random number that's either 0 or 1
# Corre el programa tantas veces, hasta que salga 5 veces Heads or Tails.
if num > 0.5:
  print('Heads')
else:
  print('Tails')

## Grades

grade = 56

if grade >= 55:
    print("You passed.")
else:
   print("You failed.")

## PH Levels / Relational Operators

ph = int(input("Enter a ph value (0-14): "))
if ph > 7:
  print("Basic")
elif ph < 7:
  print("Acid")
else:
  print("Neutral")

## Magic 8 Ball / Random

import random
num = random.randint(1, 9)
print(num)
question = input("Is codédex better than Udemy yet?: ")
random_number = random.randint(1, 9)
answers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Yes, definitely")
answers = [
    "Yes, definitely",
    "It is decidedly so",
    "Without a doubt",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
]
print(answers[random_number - 1])

## The Cyclone / Logical Operators

height = int(input("What is your height in cm?: "))
credits = int(input("How many credits do you have?: "))
if height >= 137 and credits >= 10:
    print("Enjoy the ride")
elif height < 137 and credits >= 10:
    print("You are not tall enough to ride")
elif height >= 137 and credits < 10:
    print("You don't have enough credits")
else:
   print("You have not met either requirement")

## Sorting Hat / Congrats!

quiz_One = int(input("Do you like Dawn or Dusk (1-2)" ))
if quiz_One == 1:
    print("Dawn")
else:
   print("Dusk")
quiz_Two = int(input("When I'm dead, I want people to remember me as? (1-4): "))
if quiz_Two == 1:
    print("Hufflepuff")
elif quiz_Two == 2:
    print("Slytherin")
elif quiz_Two == 3:
    print("Ravenclaw")
elif quiz_Two == 4:
   print("Gryffindor")
else:
   print("Wrong input")
quiz_three = int(input("Which kind of instrument most pleases your ear? (1-4): "))
if quiz_three == 1:
    print("Slytherin")
elif quiz_three == 2:
    print("Hufflepuff")
elif quiz_three == 3:
    print("Ravenclaw")
elif quiz_three == 4:
    print("Griffindor")
else:
    print("Wrong input")

## Enter Pin / Loop

print("BANK OF CODÉDEX")

pin = int(input("Enter your PIN: "))

while pin != 1234:
  pin = int(input("Incorrect PIN. Enter your PIN again: "))

if pin == 1234:
  print('PIN accepted!')

## Guess Number / While Loop

guess = 0

while guess != 6:
  guess = int(input('Guess the number: '))

while guess != 6:
  guess = int(input('Guess the number: '))

## Detention / range

for i in range(6):
  print(i)

## Bottles / Squares

for x in range(99, 98, -1):
    print(f"{x} bottles of beer on the wall")
    print(f"{x} bottles of beer")
    print("Take one down, pass it around")
    print(f"{x-1} bottles of beer on the wall")
print(x)

## Fizz Buzz / Congrats

for num in range(1, 100):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")