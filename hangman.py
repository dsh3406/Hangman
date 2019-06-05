import getpass
answer = getpass.getpass(prompt="What is your secret word? ")
answer_list = []
guesses = []
guessed_letter = []
for char in answer:
    answer_list.append(char.upper())
    guesses.append("_")    
print(guesses)

hangman = ["""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
"""]

attempt = 0

while True:
    guess = input("Enter your guess: ")

    if guess == "":
        print("Please enter a letter.")
        continue
    if len(guess) > 1:
        print("Please enter a single character.")
        continue

    if guess.upper() in guessed_letter:
        print("You already tried this letter: %s" % guessed_letter)
        continue
    guessed_letter.append(guess.upper())

    for index in range(len(answer_list)):
        if answer_list[index] == guess.upper():
            guesses[index] = guess.upper()

    if guess not in answer:
        if attempt == len(hangman):
            print("You Lose")
            print("Hangman has died.")
            break
        print(hangman[attempt])
        attempt += 1
        print("Wrong. Try again")

    print(guesses)

    if guesses == answer_list:
        print("You win")
        print("You have guessed all the letters correctly.")
        break