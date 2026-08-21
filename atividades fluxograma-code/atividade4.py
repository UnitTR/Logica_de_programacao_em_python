# Crie um fluxograma que leia uma temperatura em graus Celsius e a converta para Fahrenheit. Ao término, mostre o resultado. (Fórmula: F = (C × 9/5) + 32)
celsius = int(input("Bem vindo(a) ao convertor de temperatura mais rápido do Brasil!, por favor indique a temperatura em Celsius:  "))
fahrenheit = (celsius * 9/5) + 32

print("Aqui está a temperatura convertida em fahrenheit:  ", fahrenheit)