class Somatorio:

    def somatorio(self, active):
        self.active = active
        calc = 1
        for i in range(100):
            x = int(i) + 1
            calc = calc + x

        print(f"O resultado final do somatório de 1 até 100 é: ", calc)
        return self.active


ObjSomatorio = Somatorio()