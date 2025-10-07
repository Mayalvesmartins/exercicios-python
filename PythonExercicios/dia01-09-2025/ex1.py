def div(i,j):
    if j==0:
        print('O valor do j nunca pode ser zero')
    else:
        return i/j
    
if __name__=='__main__':
        j =float(input('Digite o primeiro numero: '))
        i = float(input('Digite o segundo numero: '))

        r =div(i,j)
        print(f'A divisão de {i} por {j} e {r:.2f}')


# def soma(i,j):
#     if j==0:
#         print('O valor do j nunca pode ser zero')
#     else:
#         return i+j
    
# if __name__=='__main__':
#         j =float(input('Digite o primeiro numero: '))
#         i = float(input('Digite o segundo numero: '))

#         r =soma(i,j)
#         print(f'A soma de {i} por {j} e {r:.2f}')


# def potencia(i,j):
#     if j==0:
#         print('O valor do j nunca pode ser zero')
#     else:
#         return i**j
    
# if __name__=='__main__':
#         j =float(input('Digite o primeiro numero: '))
#         i = float(input('Digite o segundo numero: '))

#         r =potencia(i,j)
#         print(f'A potencia de {i} por {j} e {r:.2f}')