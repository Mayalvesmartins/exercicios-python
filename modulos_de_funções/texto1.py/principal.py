import util_texto

texto = input("Digite um texto: ")

print("\n--- Resultados ---")
print("Capitalizado:", util_texto.capitalizar(texto))
print("Número de palavras:", util_texto.contar_palavras(texto))
print("Texto invertido:", util_texto.inverter_texto(texto))


