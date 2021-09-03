class ListaMenor:

    def listaMenor(self, numLista, active):
        self.numLista = numLista
        self.active = active

        X = 0
        maior = 0
        cont = 0

        for i in range(5):
            X = int(numLista[cont])
            if i == 0:
                cont += 1
                continue
            else:
                if X > maior:
                    maior = X
                    cont += 1
                else:
                    cont += 1
                    continue

        print(f"\nO maior número dentre os cinco informados é: {maior}")
        print("-" * 50)

        return active





ObjListaMenor = ListaMenor()