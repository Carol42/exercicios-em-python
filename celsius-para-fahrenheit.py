# Converte um dado valor em Celsius para Fahrenheit

print("Insira o valor em Celsius que deseja converter para Fahrenheit: ")
celsius = int(input())

def conv(c):
    x = 9/5 * c + 32
    return x

fahrenheit = conv(celsius)
print(fahrenheit)