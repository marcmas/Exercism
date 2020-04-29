def find_anagrams(word, candidates):
    result = []
    for candidate in candidates:
        if sorted(candidate.lower()) == sorted(word.lower()) and word.lower() != candidate.lower():
            result.append(candidate)
    return result