## CodeGuessr Game (v0.2)

## Author: Viten3d
## Created: 30 Dec 2025
## Python: 3.11.2

# Changes in v0.2.1:
# - Condense code generation and comparison into functions. [done]
# - Fix max score to change based on code length.           [done]
# - Condense setting range enforcement code blocks?         [wip]

# Potential changes coming in v0.3:
# - Option for duplicate digits?
# - Hard saving for settings and scores.
# - Option for multiple playthroughs with compound scoring.
# - Error checking for guess inputs.

# Import module(s):
from random import *

# Functions:
# - Code generator:
def num_code(nc_length):
    dupe_check = 0
    while dupe_check == 0:
        temp = 0
        code = str(randint(0,9))
        for k in range(0, nc_length - 1):
            code += str(randint(0,9))
        for k in range(0, nc_length):
            for n in range(k + 1, nc_length):
                if code[k] == code[n]:
                    temp = 1
                    break
            if temp == 1:
                break
        if temp != 1:
            dupe_check = 1
    return code
# - Digit checker:
def iter_dupe_check(iter_1, iter_2): # iter_2 -> code
    global dig_cor, place_cor
    dig_cor = place_cor = 0
    for n in range(0, len(iter_2)):
        if iter_1[n] == iter_2[n]:
            dig_cor += 1
            place_cor += 1
        for w in range(0, len(iter_2)):
            if n != w:
                if iter_1[n] == iter_2[w]:
                    dig_cor += 1

# Introduction:
print("Welcome to CodeGuessr!\n")
info = input('Review game information? (y/n)\n\n>>> ')
if info == 'y':
    print("\nA secret code with no repeating digits will be generated.\n")
    print("Hint codes will be generated with the following information:")
    print("- The number of matching digits;")
    print("- The number of matching digits in the correct position.\n")
    print("Your goal is to deduce what the secret code is based off of the hints.")

# Default settings:
hints_d = 5      # range: 1 - 10
guesses_d = 3    # range: 1 - 5
guess_fb_d = 'n' # range: 'y' or 'n'
code_len_d = 3   # range: 3 - 5

hints = hints_d
guesses = guesses_d
guess_fb = guess_fb_d
code_len = code_len_d

# Interactive settings:
settings = input('\nReview game settings? (y/n)\n\n>>> ')
if settings == 'y':
    print("\nNote: Enter nothing if no change is desired.")
    temp = 0
    while temp == 0:
        hints = input('\nNumber of hints. Default: 5\n\n>>> ')
        if hints == '':
            hints = hints_d
            temp = 1
        elif int(hints) < 1 or int(hints) > 10:
            print("\nHint value must be an integer from 1 to 10.")
        else:
            hints = int(hints)
            temp = 1
    temp = 0
    while temp == 0:
        guesses = input('\nNumber of guesses. Default: 3\n\n>>> ')
        if guesses == '':
            guesses = guesses_d
            temp = 1
        elif int(guesses) < 1 or int(guesses) > 5:
            print("\nGuess value must be an integer from 1 to 5.")
        else:
            guesses = int(guesses)
            temp = 1
    temp = 0
    while temp == 0:
        guess_fb = input('\nTurn on guess feedback? (y/n) Default: n\n\n>>> ')
        if guess_fb == '':
            guess_fb = guess_fb_d
            temp = 1
        elif guess_fb != 'y' and guess_fb != 'n':
            print("\nGuess feedback value must be y or n.")
        else:
            temp = 1
    temp = 0
    while temp == 0:
        code_len = input('\nNumber of digits for code. Default: 3\n\n>>> ')
        if code_len == '':
            code_len = code_len_d
            temp = 1
        elif int(code_len) < 3 or int(code_len) > 5:
            print("\nCode length value must be an integer from 3 to 5.")
        else:
            code_len = int(code_len)
            temp = 1

print() # newline

# Generate secret code:
code = num_code(code_len)

#print(f"\nCode: {code}") # debug (remove '#' at the start of this line)

# Generate hint codes:
code_hlist = []
for k in range(0, hints):
    code_hlist.append(num_code(code_len))

#print(f"\nHint code list: {code_hlist}") # debug (remove '#' at the start of this line)

# Determine hint data:
dc_list = pc_list = []
for k in range(0, hints):
    iter_dupe_check(code_hlist[k], code)
    dc_list.append(dig_cor)
    pc_list.append(place_cor)

#print(f"\nCorrect digit list: {dc_list}") # debug (remove '#' at the start of this line)
#print(f"Correct place list: {pc_list}\n\n") # debug (remove '#' at the start of this line)

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
    else:
        print("\nNope! Try again.")
        # Guess feedback:
        if guess_fb == 'y':
            iter_dupe_check(guess, code)
            print(f"\nGuess {k + 1}: {guess}")
            print(f"{dig_cor} digit(s) correct.")
            print(f"{place_cor} digit(s) correctly placed.")

# Score (based on final guess):
iter_dupe_check(guess, code)
print(f"\nScore: {dig_cor + place_cor}/{2 * code_len}")

# Prevent immediate program termination:
input('\nPress enter to end program.\n\n>>>')