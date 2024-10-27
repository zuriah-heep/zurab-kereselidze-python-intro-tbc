def invert1(text):
    return text[::-1]

def invert2(text):
    x = ''
    for i in range(len(text)):
        x += text[-i-1]
    return x

print(invert1('abcd'), invert2('abcd'))