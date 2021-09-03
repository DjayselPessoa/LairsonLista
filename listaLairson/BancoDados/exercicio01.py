class Tabuada:

    def tabuada(self, x, active):
        self.x = x # inteiro

        try:
            print(f"TABUADA do {self.x}\n", "-" * 13)
            for i in range(10):
                calc = int(i) + 1
                resultado = calc * self.x
                print(f"{calc} x {self.x} = {resultado}")
            
            sair = str(input("S para sair ou C para continuar: "))
            if sair in "SsCc":
                if sair in "Ss":
                    active = False
                    print("DESLIGANDO!")
                    return active
                elif sair in "Cc":
                    print("REINICIANDO!")
                    return active
            else:
                print("DADO INCORRETO - REINICIANDO!")
                return active

        except ValueError as e:
            print("LOG: -> ", e)


ObjTabuada = Tabuada()