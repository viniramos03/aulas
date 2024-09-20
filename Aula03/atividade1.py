import random

class Calculadora:

    def soma(self, numero1, numero2):
        return numero1 + numero2

    def subtracao(self, numero1, numero2):
        return numero1 - numero2

    def multiplicacao(self, numero1, numero2):
        return numero1 * numero2

    def divisao(self, numero1, numero2):
        return numero1 / numero2
############################################
def main():
    calc = Calculadora()

    numero1 = random.randint(0, 100)
    numero2 = random.randint(0, 100)

    resultado_soma = calc.soma(numero1, numero2)
    print(f"A soma do número {numero1} e o número {numero2} é: {resultado_soma}")

    resultado_subtracao = calc.subtracao(numero1, numero2)
    print(f"A subtracao do número {numero1} e o número {numero2} é: {resultado_subtracao}")

    resultado_multiplicacao = calc.multiplicacao(numero1, numero2)
    print(f"A multiplicacao do número {numero1} e o número {numero2} é: {resultado_multiplicacao}")

    resultado_divisao = calc.divisao(numero1, numero2)
    print(f"A divisão do número {numero1} e o número {numero2} é: {resultado_divisao}")

if __name__ == "__main__":
  main()