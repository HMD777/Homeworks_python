def decoder(txt):
    decode = ''
    count = ''
    for char in txt:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode
