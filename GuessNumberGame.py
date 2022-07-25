print("RULES: Computer choose a Number!!\nYou will guess a number.then COMPUTER tells you ,if your guess is higher or lower \nLets GO!!")
import random
num = random.randint(1,99)
guess = input("Please guess a Number: ")
guess = int(guess)
while guess != num:
    if guess > num:
        print("My Number is lower!! ")
    else:
        print("My Number is higher!! ")
    guess = input("Please guess a Number: ")
    guess = int(guess)
print("Congratulation !!!! ")

