import re

def is_valid(isbn):
    isbn = isbn.replace("-", "")
    # Check if isbn has 10 numbers or 9 numbers and "X"
    if not re.match("^[0-9]{9}[0-9X]$", isbn):
        return False

    result = 0
    j = 10
    for i in isbn:
        if i == "X":
            result += 10
        else:
            result += j * int(i)
            j -= 1
    return result % 11 == 0

