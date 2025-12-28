## CodeGuessr Game (v0.1)

## Author: Jeff [redacted]
## Created: 26 Dec 2025
## Python: 3.11.2

# Potential features coming soon:
# - Option for variable code length.
# - Option for duplicate numbers.
# - Option for guess feedback.
# - Hard saving for setting preferences.

# Import module(s):
from random import *

# Introduction:
print("Welcome to CodeGuessr!\n")
info = input('Review game information? (y/n)\n\n>>> ')
if info == 'y':
    print("\nA secret 3-digit code with no repeating digits will be generated.\n")
    print("Hint codes will be generated with the following information:")
    print("- The number of matching digits;")
    print("- The number of matching digits in the correct position.\n")
    print("Your goal is to deduce what the secret code is based off of the hints.")

# Game settings:
settings = input('\nReview game settings? (y/n)\n\n>>> ')
if settings == 'y':
    print("\nNote: Enter default value if no change is desired.")
    hints = int(input('\nNumber of hints. Default: 5\n\n>>> '))
    guesses = int(input('\nNumber of guesses. Default: 3\n\n>>> '))
else:
    # edit default settings here
    hints = 5
    guesses = 3

print() # newline

# Generate secret code:
dupe_check = 0
while dupe_check == 0:
    code = str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
    if code[0] != code[1] and code[0] != code[2] and code[1] != code[2]: 
        dupe_check = 1

# Generate hint codes:
code_hlist = []
for k in range(0, hints):
    dupe_check = 0
    while dupe_check == 0:
        code_hint = str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
        if code_hint[0] != code_hint[1] and code_hint[0] != code_hint[2] and code_hint[1] != code_hint[2]: 
            dupe_check = 1
    code_hlist.append(code_hint)

# Determine hint data:
dc_list = []
pc_list = []
for k in range(0, hints):
    dig_cor = 0
    place_cor = 0
    for n in range(0,3):
        if n == 0:
            if code_hlist[k][0] == code[1]:
                dig_cor += 1
            if code_hlist[k][0] == code[2]:
                dig_cor += 1
            if code_hlist[k][1] == code[0]:
                dig_cor += 1
            if code_hlist[k][1] == code[2]:
                dig_cor += 1
            if code_hlist[k][2] == code[0]:
                dig_cor += 1
            if code_hlist[k][2] == code[1]:
                dig_cor += 1
        if code_hlist[k][n] == code[n]:
            dig_cor += 1
            place_cor += 1     
    dc_list.append(dig_cor)
    pc_list.append(place_cor)

# Hints output:
for k in range(0, hints):
    print(f"Hint {k + 1}: {code_hlist[k]}")
    print(f"{dc_list[k]} digit(s) correct.")
    print(f"{pc_list[k]} digit(s) correctly placed.\n")

# Guess loop:
for k in range(0, guesses):
    guess = input(f'\nGuess {k + 1}/{guesses}:\n\n>>> ')
    if guess == code:
        print("\nCorrect! You win!")
        break
    elif k + 1 == guesses:
        print(f"\nSorry :C The correct answer was {code}.")
        print("Better luck next time!")
        break
    else:
        print("\nNope! Try again.")

# Prevent immediate program termination:
input('\nPress enter to end program.\n\n>>>')