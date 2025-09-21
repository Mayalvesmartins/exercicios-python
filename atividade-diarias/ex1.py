"""
    Variáveis numéricas
"""

# Int: Número sem decimais
dia = 10
print("Inteiro:", dia)

# Float: Número com decimais
valor = 10.25
print("Float:", valor)

# Complex: Número com parte real e parte imaginária (real + IMAG J)
# Extraindo a parte real e a parte imaginária:
complexo = 5 + 7j
real = complexo.real
imaginario = complexo.imag
print("Complexo:", complexo)
print("Parte real:", real)
print("Parte imaginária:", imaginario)

# Transformar números reais em números complexos
complexo2 = complex(25, 6)
print("Complexo2:", complexo2)