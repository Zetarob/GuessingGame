# Robert Aguilar
# CIS261
#GuessingGame

print("hello, welcolm to my game\n")
import random
n = random.randrange(1,100)
guess = int(input("Enter any number between 1 and 100:  "))
while n!= guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again:  "))
    elif guess > n:
            print("Too high")
            guess = int(input("Enter number again:  "))
    else:
            break
print("you guessed correct")
keepPlaying = input("\nDo you want to play again? Enter yes or no:  ")
while keepPlaying.lower() != "yes" and keepPlaying.lower() != "no":
    keepPlaying = input ("Please type yes or no to continue:  ")
