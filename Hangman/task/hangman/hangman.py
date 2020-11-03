# Write your code here
import random as r



word_list = ['python', 'java', 'kotlin', 'javascript']
random_word = r.choice(word_list)
hint = ["-"] * len(random_word)
guess_set = set()
answer_set = set(random_word)
lives = 8


def update_hint(char):
    guess_set.add(char)
    for i in range(len(random_word)):
        if random_word[i] == char:
            hint[i] = char

print("H A N G M A N")
choice = input('Type "play" to play the game, "exit" to quit:')
while choice not in ['play', 'quit']:
    choice = input('Type "play" to play the game, "exit" to quit:')
print("")

while choice != 'exit':
    while True:
        print("".join(hint))
        if "-" not in hint:
            print(f"You guessed the word {random_word}!")
            print("You survived!")
            break
        char = input("Input a letter: ")

        while True:
            if len(char) != 1:
                print("You should input a single letter")
            elif not (char.islower() and char.isalpha()):
                print("It is not an ASCII lowercase letter")
            else:
                break
            print("")
            print("".join(hint))
            char = input("Input a letter: ")

        if char in answer_set and char not in hint:
            update_hint(char)
        else:
            if char in guess_set:
                print("You already typed this letter")
            else:
                print("No such letter in the word")
                guess_set.add(char)
                lives -= 1
        if lives == 0:
            print("You lost!\n")
            break
        print("")
    choice = input('Type "play" to play the game, "exit" to quit:')
    while choice not in ['play', 'exit']:
        choice = input('Type "play" to play the game, "exit" to quit:')
        print("")





