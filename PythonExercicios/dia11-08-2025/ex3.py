nota = float(input('Digite a nota (0 a 10): '))
if nota >+9:
    resultado = ('otimo')
elif nota >=7:
    resultado = ('bom')
elif nota >=5:
    resultado = ('regular')
else:
    print('insuficiente')
print('sua nota e' , nota , 'e seu resultado e' , resultado , 'para passar de ano.')