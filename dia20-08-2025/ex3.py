# livro = {'titulo': 'O conde de monte cristo' , 'autor': 'alexndre dumas' , 'ano': 1844 }
# print(f'titulo: {livro['titulo']}')
# print(f'autor: {livro['autor']}')
# print(f'ano: {livro['ano']}')


# agenda =  {'Mayara': '(62) 9 93882920', 'joao': '(62) 9 12345678' , 'pedro': '(62) 9 87654321'}
# print('agenda de contatos: ')
# print('-' * 20)
# for nome, telefone in agenda.items():
#     print(f'nome: {nome}')
#     print(f'telefone: {telefone}')
#     print('-' * 20)




# aluno1 = {'nome': 'mayara', 'idade': 27 , 'nota': 8.0 , 'curso': 'PYthon'}
# aluno2 = {'nome': 'joao' , 'idade': 30 , 'nota': 9.0 , 'curso': 'java'}
# aluno3 = {'nome': 'pedro' , 'idade': 25 , 'nota': 7.5 , 'curso': 'c++'}
# alunos = [aluno1, aluno2 , aluno3]
# alunos_ordenados = sorted(alunos, key=lambda a: a['idade'])




      
linguagens = {'python' , 'java', 'c++', 'javascript', 'ruby'}
print('Lista original: ')
print(linguagens)
print(f'Tamanho da lista: {len(linguagens)}')
linguagens_unicas = set(linguagens)
print('\nconjunto sem duplicatas: ')
print(linguagens_unicas)
print('f tamanho do conjunto: ', len(linguagens_unicas))
