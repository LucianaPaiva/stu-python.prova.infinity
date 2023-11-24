lista1 = []
lista2 = []

print("-"*30)
print("Digite os números inteiros para a LISTA 1")
print("Para interromper a inclusão, digite SAIR.")
print("-"*30)

while True:
    item = input("Digite um número para a lista1: ")
    if item == 'sair':
        break
    else:
        lista1.append(int(item))

print("-"*30)
print("Digite os números inteiros para a LISTA 2")
print("Para interromper a inclusão, digite SAIR.")
print("-"*30)

while True:
    item = input("Digite um número para a lista 2: ")
    if item == 'sair':
        break
    else:
        lista2.append(int(item))

print("-"*30)

conjunto1 = set(lista1)
conjunto2 = set(lista2) 
resultado = conjunto1.intersection(conjunto2)
print(resultado)
print(sum(resultado))