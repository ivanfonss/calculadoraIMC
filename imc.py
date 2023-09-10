# Solicita peso e a altura
peso = float(input("Digite o peso em quilogramas no formato 75.300 : "))
altura = float(input("Digite a altura em metros no formato 1.75: "))

# Calcula IMC
imc = peso / (altura ** 2)

# Exibe resultado
print("Seu IMC é: {:.2f}".format(imc))

# Classifica IMC
if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 24.9:
    print("Seu peso está normal.")
elif 25 <= imc < 29.9:
    print("Você está com sobrepeso.")
else:
    print("Você está obeso.")