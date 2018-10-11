def code(invoerstring):
    for char in invoerstring:
        nummer = ord(char)
        optellen = nummer + 3
        codeAscii = chr(optellen)
        print(codeAscii, end='')
code('RutteAlkmaarDen Helder')