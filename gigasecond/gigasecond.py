import datetime
def add(moment):
    time = moment + datetime.timedelta(seconds=10 ** 9)
    return time