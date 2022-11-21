def encoder(txt):
    encode = ''
    char_0 = ''
    count = 1
    if not txt:
        return ''
    for char in txt:
        if char != char_0:
            if char_0:
                encode += str(count) + char_0
            count = 1
            char_0 = char
        else:
            count += 1
    else:
        encode += str(count) + char_0
        return encode
