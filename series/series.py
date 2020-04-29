def slices(series, length):
    if length > len(series) or length < 1:
        raise ValueError("Lenght can't be smaller than series or smaller than zero")

    result = []
    for i in range(len(series)):
        if len(series[i:]) >= length:
            result.append(series[i:i + length])
    return result