def square_of_sum(number):
    result = 0
    result = [result + i for i in range(1, number + 1)]
    return sum(result)**2


def sum_of_squares(number):
    result = 0
    result = [result + i**2 for i in range(1, number + 1)]
    return sum(result)


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
