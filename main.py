import os
import math

def baskara(a, b, c):
    soma = ax + b=0
    yield soma
    subtracao = x - y
    yield subtracao
    multiplicacao = x*y
    yield multiplicacao
    divisao = x/y
    yield divisao

delta = b -4*a*c

math.sqrt(delta)

x = int(input('Informe o primeiro número: '))
y = int(input('Informe o segundo número: '))

resultados = calcular_tabuada(x, y)

print(f'A soma é {next(resultados)}. ')
print(f'A subtração é {next(resultados)}. ')
print(f'A multiplicação é {next(resultados)}. ')
print(f'A divisão é {next(resultados)}. ')