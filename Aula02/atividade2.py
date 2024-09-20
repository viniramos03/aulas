numeros_inteiros = []
numeros_pares = []
numeros_impares = []

for i in range(5):
  numero_digitado = int(input(f"Digite o número {i+1}: "))
  numeros_inteiros.append(numero_digitado)

  if numero_digitado % 2 == 0:
    numeros_pares.append(numero_digitado)
  else:
    numeros_impares.append(numero_digitado)

print(f"A lista digitada foi: {numeros_inteiros}")
print(f"A lista de números pares foi: {numeros_pares}")
print(f"A lista de números impares foi: {numeros_impares}")
