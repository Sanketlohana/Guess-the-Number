import random

# First we take 2 inputs for range from the User

A = int(input('Enter the 1st number = '))
B = int(input('Enter the last number = '))

# The system is made to store one random number from the user specified range

z = random.randint(A, B)

# User Input is taken for Specified number of chances
# Then the Counter is increased for each Guess made by the User

for count in range(10):
    guess_num = int(input("Guess a number = "))
    count += 1

# The Guessed Number is then compared with the system selected number
# If the user is out of chances or other comparisons are made accordingly

    if count == 10:
        print(" Sorry you are out of chances the Number was =", int(z))
        break

    elif z > guess_num:
        print("Guessed number is smaller than the Required Number ")

    elif z < guess_num:
        print("Entered Number is greater than Required Number ")

    elif z == guess_num:
        print("Congratulations you made a Correct Guess ")
        break

print("Thank You For Playing ")