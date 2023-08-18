import random

sampleWords = ["Mercedes", "Ferrari", "Red Bull", "Mclaren", "Alpine", "Alphatauri", "Aston Martin", "Haas", "Alfa Romeo", "Williams"]
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

oneWord = random.choice(sampleWords).replace(" ","").lower()
#oneWord = sampleWords[2].replace(" ","").lower()
hangmanWord = []
guessWord = []
print(oneWord)
originallength = len(oneWord)
print(originallength)

default = list(oneWord)

guesses = 10
for i in oneWord:
    hangmanWord.append(i)

j = 0
while j < originallength:
    guessWord.append("")
    j += 1


while guesses > 0:
    print(guessWord)
    
    print("You have ",guesses," guesses left.")
    guess = input("Enter a letter: ")
    if guess in hangmanWord and len(guess) == 1:
        k = 0
        # Replace blanks with guess letter here
        while k < originallength:
            if default[k] == guess:
                guessWord[k] = guess
            k += 1
        
        while guess in hangmanWord:
            hangmanWord.remove(guess)
            #guessWord.append(guess)       

        letters.remove(guess)
        if len(hangmanWord) == 0:
            print(oneWord)
            print("You win!")
            break

    elif guess not in letters:
        continue
      
    else:
        guesses -= 1
        letters.remove(guess)
        if guesses == 0:
            print("You lose!")
# STILL DOING THIS

