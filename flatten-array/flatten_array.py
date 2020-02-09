def flatten(iterable):
    lists = []

    for x in iterable:
        if type(x) == list:
            lists += flatten(x)
        elif x != None and x != ():
            lists.append(x)
    return lists


