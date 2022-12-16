def bmi (weight, height):
    return weight / height ** 2

peso = float(input('Peso?'))
altura = float(input('Altura?'))
imc = bmi(peso, altura)
if imc == None:
    print('Altura e peso tem que ser > 0')
elif imc < 18.5:
    print('IMC de '+str(imc)+' a baixo do recomendado' )
