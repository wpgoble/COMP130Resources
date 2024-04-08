def summation(my_lst):
    answer = 0
    for value in my_lst:
        value_sqr = value ** 2
        answer += value_sqr
    return answer

# write a function that returns the
# most popular major
def most_popular(my_lst):
    popular_major = ""
    major_appearence = 0
    for major in my_lst:
        count = 0
        for second_major in my_lst:
            if major == second_major:
                count += 1
        if count > major_appearence:
            popular_major = major
            major_appearence = count
    return popular_major, major_appearence


def square_list(my_lst):
    answer = []
    for number in my_lst:
        number_sqr = number ** 2
        answer.append(number_sqr)
    return answer

def split_classes(my_lst):
    departments = []
    course_numbers = []
    for course in my_lst:
        departments.append(course[:4])
        course_numbers.append(course[4:])
    return departments, course_numbers

def find_computing(my_lst):
    computing = []
    for course in my_lst:
        department = course[0:4]
        if department  == "COMP":
            computing.append(course)
    return computing


numbers = [1,2,3,4,5]
##print(summation(numbers))
classes = ["COMP130", "COMP132", "ENGL222",
           "DATA180", "MATH171", "ARTH101",
           "FYSM100"]

majors = ["IBM", "QEcon", "QEcon",
          "BioChem", "Art History",
          "Data", "Law", "IBM", "QEcon"]
temp1, temp2 = most_popular(majors)
##print(temp1, temp2)

#print(square_list(numbers))
##departments, courses = split_classes(classes)
##print(most_popular(departments))

print(find_computing(classes))

