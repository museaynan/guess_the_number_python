import random
print("Hello! Today we are going to play Guess The Number!")
number = int(input("Guess a number between 0 and 5"))
random_number = random.randint(0, 5)
if number == random_number:
    print("You won!")
    print("Your prize is...")
    print("Nothing!")
else:
    print("You lost!")
    print("The number was {0}.".format(random_number))
