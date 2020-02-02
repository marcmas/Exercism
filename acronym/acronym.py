import re 

def abbreviate(words):
    words = re.findall(r"([a-zA-Z0-9]+(?:[']?[a-z0-9]+)*)", words)
    name = ""
    for w in words:
        name += w[0].upper()
    return name

