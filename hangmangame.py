import random
print("welcome to hangman game")
words=["apple","orange","guava","grapes","banana","cherry"]
guessed_word=random.choice(words)
for let in guessed_word:
    print("_",end="")
print("Now start guessing letters")
for i in range(len(guessed_word+2)):
    guessed_letter=input("guess a letter")
    for ele in guessed_word:
        if guessed_letter==ele:
            print("match")
        else:
            print("no match")



