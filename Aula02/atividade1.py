numeros_digitados = []
numeros_somados = 0
numeros_multiplicados = 1

for i in range(5):
  numero_digitado = int(input(f"Digite o valor {i+1}: "))
  numeros_digitados.append(numero_digitado)

  numeros_somados += numero_digitado
  numeros_multiplicados *= numero_digitado

print(f"A lista digitada é: {numeros_digitados}")
print(f"A soma dos números é: {numeros_somados}")
print(f"A multiplicação dos números é: {numeros_multiplicados}")
print(f"O valor a ser retirado da lista é: {numeros_digitados.pop()}")
print(f"Lista atualizada: {numeros_digitados}")