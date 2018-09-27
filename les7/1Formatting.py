def convert(temperatuurCelsius):
    temperatuurFahrenheit = temperatuurCelsius * 1.8 + 32
    return temperatuurFahrenheit

def table():
    print('{:4} {:5}'.format('  C', '  F'))
    for temperatuurCelsius in range(-30, 41, 10):
        temperatuurFahrenheit = convert(temperatuurCelsius)
        print('{:4} {:5}'.format(temperatuurCelsius, temperatuurFahrenheit))

table()