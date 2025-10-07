# def calcular_area (base, altura):
#     return base * altura
# area = calcular_area(5, 4)
# print(f'Area: {area} unidades quadradas. ')



# temperatura = float(input("Digite uma temperatura em Celsius: "))
# temperaturaEmFahrenheit = temperatura * (9 / 5) + 32
# print(f'A temperatura em Fahrenheit é: {temperaturaEmFahrenheit:.1f} ºF')

# def celsius_para_fahrenheit(celsius):
#     return(celsius * 9/5) + 32
# temp_f = celsius_para_fahrenheit (25)
# print(f'25°C = {temp_f} ºF')



def saudacao_horario (nome, hora):
    if 5 <= hora < 12:
        return (f'Bom dia, {nome}!')
    elif 12 <= hora < 18:
       return (f'Boa tarde, {nome}!')
    else:
        return (f'Boa noite, {nome}!')
msg = saudacao_horario ('mayara', 9)
print(msg)
    


        
