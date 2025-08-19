mochila = ["camiseta", "calça", "meias", "escova", "carregador", "livro"]
mochila.remove ("livro") 
mochila.pop (2)
mochila.append ("remédios")
mochila[0] = "blusa" 
mochila_ordenada = sorted(mochila)  
print("Mochila final:")
for item in mochila_ordenada:
    print(f"- {item}")
