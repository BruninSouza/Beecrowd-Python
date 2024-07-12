entrada = input()
valores = entrada.split()
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])
pi = 3.14159

triangulo_retangulo = (a * c) / 2
circulo = pi * c ** 2
trapezio = ((a+b) * c) / 2
quadrado = b ** 2
retangulo = a * b

print(f'TRIANGULO: {triangulo_retangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')