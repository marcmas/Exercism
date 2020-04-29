def rotate(text, key):
    alfabet = ('abcdefghijklmnopqrstuvwxyz')
    main_result = ''
    for t in text:
        if t.lower() in alfabet:
            value = alfabet.index(t.lower())
            all_value = key + value
            part_result = ''
            part_result = alfabet[all_value] if all_value < 26 else alfabet[all_value-26]
            main_result += part_result.upper() if t.isupper() else part_result
        else:
            main_result += t
    return main_result
