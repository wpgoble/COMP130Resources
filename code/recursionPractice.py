def sumList(my_list):
    if len(my_list) == 1:
        return my_list[0]
    else:
        first = my_list[0]
        remainder = sumList(my_list[1:])
        return first + remainder

def reverse(word):
    if word == word[0]:
        return word
    else:
        first = word[0]
        remainder = reverse(word[1:])
        return remainder + first

print(reverse("Time"))
