import random

sampleWords = ["Mercedes", "Ferrari", "Red Bull", "Mclaren", "Alpine", "Alphatauri", "Aston Martin", "Haas", "Alfa Romeo", "Williams"]

oneWord = random.choice(sampleWords).replace(" ","").lower()
hangmanWord = []
guessWord = []
print(oneWord)
originallength = len(oneWord)
print(originallength)

guesses = 10
for i in oneWord:
    hangmanWord.append(i)

while guesses > 0:
    #print(hangmanWord)
    #print(len(hangmanWord))
    print("You have ",guesses," guesses left.")
    guess = input("Enter a letter: ")
    if guess in hangmanWord and len(guess) == 1:
        hangmanWord.remove(guess)
        guessWord.append(guess)
        if originallength == len(guessWord):
            print("You win!")
            break
    else:
        guesses -= 1
        if guesses == 0:
            print("You lose!")
# STILL DOING THIS

