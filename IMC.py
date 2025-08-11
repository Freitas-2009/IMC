print ("SEU IMC")

Nome = input("Digite seu nome")
Peso = float(input ("Digite seu peso:"))
ALtura = float(input ("Digite sua altura"))
IMC = Peso / (ALtura * ALtura)

print("--------------------------------------")
print (f" {Nome} seu IMC é: {IMC}")

if IMC < 18.5:
     print("ABAIXO DO PESO")
elif IMC < 24.9:
    print("NORMAL")
else:
    print("OBESIDADE")
print("--------------------------------------")
