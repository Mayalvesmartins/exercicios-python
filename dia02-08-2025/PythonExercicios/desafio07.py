larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('sua parede tem a dimensão de {}x{} e sua area e de {}m².'.format(larg, alt,area))
tinta = area / 2
print ('para pintar essa parede, voce precisara de {}l de tinta.'.format(tinta))
