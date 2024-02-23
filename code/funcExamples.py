# exercise 1
# reverse a string
def reverse(str):
    answer = ""
    for letter in str:
        #answer += letter
        answer = letter + answer
    return answer

def reverse2(str):
    answer = ""
    for i in range(len(str)-1, -1, -1):
        answer = answer + str[i]
    return answer

print(reverse2("dog"))
print(reverse2("cat"))
print(reverse2("kayak"))
