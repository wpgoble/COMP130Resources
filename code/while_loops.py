from answer import answer

def isWeekend(day):
    assert type(day) == str, "We need a string"
    day = day.lower()
    day = day.capitalize()
    daysOfWeek = day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday" or day == "Sunday"    
    assert daysOfWeek == True, "please give us a valid day"
    
    if day == "Saturday" or day == "Sunday":
        return True
    else:
        return False

def isWeekday(day):
    return not isWeekend(day)

def test_isWeekend():
    assert isWeekend("SaTuRdAy") == True, "This should be True"
    assert isWeekend("sunday") == True, "This should be True"
    assert isWeekend("MONDAY") == False, "This should be False"
    print("weekend tests passed")

test_isWeekend()
