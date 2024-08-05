tries = 0 
guess = 0

print("You have 3 chances.")

while guess != 6 and tries < 3:
    guess = int(input("Guess the number:  "))
    tries += 1
if guess == 6:
    print("You got it!")
elif tries == 3:
    print("Game over.")