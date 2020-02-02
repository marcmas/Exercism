def is_isogram(string):
    string = string.upper()
    for l in string:
        if l == " " or l == "-":
            continue
        elif string.count(l) > 1:
            return False
    return True