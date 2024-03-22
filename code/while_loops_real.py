from answer import answer

# first attempt
##for letter in word:
##    if letter == target:
##        total = total + 1
##print(total)

# second attempt
##for i in range(len(word)):
##    if word[i] == target:
##        total += 1
##print(total)

def target_word(target, word):
    index = 0
    total = 0
    while index < len(word):
        if word[index] == target:
            total = total + 1
        index = index + 1
    return total

# find the occurance of target letter in word
##answer1 = target_word("e", "elephant")
##answer2 = target_word("a", "elephant")
##print(answer1, answer2)

# guessing game
guess = input("Guess my favorite music genre ")
guess = guess.lower()
while guess != answer:
    print("Incorrect")
    guess = input("Guess my favorite music genre ")
    guess = guess.lower()
print("Good job")
















