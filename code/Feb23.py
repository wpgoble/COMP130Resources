# Implement a function which translates a word
# from english into pig latin. create a helper
# function which detects vowels.

# This should return True if the letter is a vowel
# and return False otherwise
def isVowel(letter):
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        return True
    return False

def getRestOfWord(word):
    rest = ""
    for i in range(1, len(word)):
        rest += word[i]
    return rest

# This should translate a given word into Pig Latin
def pigLatin(word):
    first = word[0]
    answer = ""
    # test if the first letter is a vowel
    if isVowel(first):
        answer = word + "way"    
    else:
        rest = getRestOfWord(word)
        answer = rest + first + "ay"

    return answer

def test_pigLatin():
    result1 = pigLatin("baseball")
    result2 = pigLatin("algebra")

    assert result1 == "aseballbay", f"Expected aseballbay, received {result1}"
    assert result1 == "algebraway", f"Expected algebraway, received {result1}"
    print("Success")

word1 = pigLatin("baseball")
word2 = pigLatin("algebra")

test_pigLatin()

##print(f"baseball in pig latin is {word1}")
##print(f"algebra in pig latin is {word2}")
