def conta_palavras(frase):
    palavras = frase.split()  
    return len(palavras)      

print(conta_palavras("Python é divertido"))  


print(conta_palavras("Python    é    divertido"))  


print(conta_palavras(""))  


