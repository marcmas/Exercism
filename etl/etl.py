def transform(legacy_data):
    result = dict()
    for i in legacy_data:
        for x in legacy_data[i]:
            result[x.lower()] = i
    return result
