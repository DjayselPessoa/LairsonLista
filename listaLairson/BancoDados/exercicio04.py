class Position:

    def position(self, numLista, active):
        self.numLista = numLista
        self.active = active
        cont = 0
        numLista2 = []
        for i in range(len(self.numLista)):
            if 10 <= numLista[i] <= 50:
                cont += 1
                numLista2.append(numLista[i])
            else:
                continue

        print(f"\nVocê escolheu {cont} valor(es) entre 10 e 50: {numLista2}")
        return self.active


ObjPosition = Position()
