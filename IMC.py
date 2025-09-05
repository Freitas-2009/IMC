print ("SEU IMC")

Nome = input("Digite seu nome: ")
Peso = float(input ("Digite seu peso: "))
ALtura = float(input ("Digite sua altura: "))
IMC = Peso / (ALtura * ALtura)

print("--------------------------------------")
print (f"{Nome} seu IMC é: {IMC}")

if IMC < 18.5:
     print("ABAIXO DO PESO")
elif IMC < 24.9:
    print("NORMAL")
elif IMC < 29.9:
    print("SOBREPESO")
elif IMC < 34.9:
    print("OBESIDADE GRAU 1")
elif IMC < 39.9:
    print("OBESIDADE GRAU 2")
else:
    print("OBESIDADE GRAU 3")

if IMC >= 30.0:
    print("❗CUIDADO COM A SAÚDE❗")
else:
    print("TUDO OK ✅")
print("--------------------------------------")
