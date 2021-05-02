import math

print("-----------------------------------")
print("Calculadora de Orçamento Sanitizant")
print("-----------------------------------")

precoMetro = float(3.33)
larg = float(input("Informe a largura do ambiente: "))
alt = float(input("Informe a altura do ambiente: "))
comp = float(input("informe o comprimento do ambiente: "))
print("-----------------------------------")

area = (larg * alt * comp)
orcamento = (precoMetro * area)

if area <= 27:
    orcamentoCheio = orcamento
    desconto = 15
    desconto = desconto/100
    orcamento = float(orcamento * (1-(desconto)))
    print("As dimensões correspondem a área confinada, aplicando desconto de ", (desconto * 100), "%", sep="")
    print("-----------------------------------")
    print("Você recebeu um desconto de R$:", round((orcamentoCheio * desconto), 2))

print("A área total de aplicação é: ", area, "m³", "e o seu orçamento é R$: ", round(orcamento, 2), ".", sep="")
print("-----------------------------------")
print("Não esqueça de preparar o ambiente para o tratamento, o processo de oxi-sanitização não substitui a limpeza.\n")