def score(word):
    result = 0
    word = word.upper()
    for w in word:
        if w in "AEIOULNRST":
            result += 1
        if w in "DG":
            result += 2
        if w in "BCMP":
            result += 3
        if w in "FHVWY":
            result += 4
        if w in "K":
            result += 5
        if w in "JX":
            result += 8
        if w in "QZ":
            result += 10
    return result

