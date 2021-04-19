weight = float(input("Digite seu peso em kg: "))
height = float(input("Digite sua altura em metros: "))

imc = weight / height ** 2 

if imc < 16:
  print("Seu IMC é de {} e enquadra-se como 'Baixo peso Grau III".format(imc))
elif imc >= 16 and imc <= 16.99:
  print("Seu IMC é de {} e enquadra-se como 'Baixo peso Grau II".format(imc))
elif imc >= 17 and imc <= 18.49:
  print("Seu IMC é de {} e enquadra-se como 'Baixo peso Grau I".format(imc))
elif imc >= 18.5 and imc <= 24.99:
  print("Seu IMC é de {} e enquadra-se como 'Peso Ideal".format(imc))
elif imc >= 25 and imc <= 29.99:
  print("Seu IMC é de {} e enquadra-se como 'Sobrepeso".format(imc))
elif imc >= 30 and imc <= 34.99:
  print("Seu IMC é de {} e enquadra-se como 'Obesidade Grau I".format(imc))
elif imc >= 35 and imc <= 39.99:
  print("Seu IMC é de {} e enquadra-se como 'Obesidade Grau II".format(imc))
elif imc >= 40:
  print("Seu IMC é de {} e enquadra-se como 'Obesidade Grau III".format(imc))
  