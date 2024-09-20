class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 0

    def ligar(self):
        if self.__validar_status() != False:
            print("A TV está LIGADA")
        else:
            self.ligada = True
        print("A TV está LIGADA")

    def desligar(self):
        if self.__validar_status() != False:
            self.ligada = False
            print("A TV foi DESLIGADA")
        else:
            print(f"Cai aqui {self.__mensagem()}")
    
    def canal_maior(self):
        if self.__validar_status():
            self.canal += 1
            print(f"Canal atual {self.canal}")
        else:
            print(f"Cai aqui {self.__mensagem()}")
    
    def canal_menor(self):
        if self.__validar_status():
            if self.canal > 0:
                self.canal -= 1
                print(f"Canal atual {self.canal}")
            else:
                print(f"O canal está não pode ser menor que 0")
        else:
            print(f"Cai aqui {self.__mensagem()}")

    def __validar_status(self):
        if self.ligada == False:
            return False

    def __mensagem(self):
        return f"A TV está DESLIGADA"

##################################

def main():
    tv = Televisao()

    tv.ligar()

    tv.desligar()
    tv.canal_maior()
    tv.canal_menor()

if __name__ == "__main__":
  main()