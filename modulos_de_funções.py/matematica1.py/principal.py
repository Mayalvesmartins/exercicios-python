
import util_matematica

n = float(input("Digite um número: "))
t = float(input("Digite uma temperatura em Celsius: "))

print("\n--- Resultados Matemáticos ---")
print(f"O dobro de {n} é: {util_matematica.dobro(n)}")
print(f"A raiz quadrada de {n} é: {util_matematica.raiz_quadrada(n)}")
print(f"{t}°C em Fahrenheit é: {util_matematica.celsius_para_fahrenheit(t)}°F")