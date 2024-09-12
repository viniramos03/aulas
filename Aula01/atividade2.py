
try:
  
  i = 0
  while i < 10:
    nota1 = float(input("Digite novamente o valor nota 1: "))

    if nota1 < 0 or nota1 > 10.0:
      print("Valor inválido para nota1: {}".format(nota1))
    else:
      break;

  j = 0
  while j < 10:
    nota2 = float(input("Digite novamente o valor nota 2: "))

    if nota2 < 0 or nota2 > 10.0:
      print("Valor inválido para nota2: {}".format(nota2))
    else:
      break

except:
  print("Valor inválido!!!")
  
media = (nota1 + nota2) / 2

if media >= 0.0 and media <= 3.9:
  conceito = "E"

elif media >= 4.0 and media <= 5.9:
  conceito = "D"

elif media >= 6.0 and media <= 7.4:
  conceito = "C"

elif media >= 7.5 and media <= 8.9:
  conceito = "B"

else:
  conceito = "A"

if conceito == "A" or conceito == "B" or conceito == "C":
  resultado = "Aprovado"
else:
  resultado = "Reprovado"

print("=============================")
print("A nota 1 foi: {}".format(nota1))
print("A nota 2 foi: {}".format(nota2))
print("A média foi: {}".format(media))
print("O conceito foi: {}".format(conceito))
print("O resultado foi: {}".format(resultado))

