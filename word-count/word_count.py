import re

def count_words(sentence):
    sentence = sentence.lower()
    sentence = re.findall(r"([a-z0-9]+(?:[']?[a-z0-9]+)*)", sentence)
    lists = dict()
    for word in sentence:
        if word in lists:
            lists[word] += 1
        else:
            lists[word] = 1
    return lists
    

