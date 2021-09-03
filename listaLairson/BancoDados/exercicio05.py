class Genero:

    def genero(self, idadeGenLista, sexoGenLista, active):
        self.idadeGenLista = idadeGenLista
        self.sexoGenLista = sexoGenLista
        self.active = active
        idadeMulher = 0
        idadeHomem = 0
        contMulher = 0
        contHomem = 0

        for i in range(len(idadeGenLista)):
            if self.sexoGenLista[i] in "Mm":
                idadeMulher = idadeMulher + idadeGenLista[i]
                contMulher += 1
            elif self.sexoGenLista[i] in "Hh":
                idadeHomem = idadeHomem + idadeGenLista[i]
                contHomem += 1
            else:
                print("DADO INFORMADO INCORRETO!")
                return self.active
        calc1 = idadeMulher // contMulher
        calc2 = idadeHomem // contHomem
        calc3 = (idadeHomem + idadeMulher) // 10
        print(f"\nNesta lista existem: ->\n{contMulher} mulheres -> idade média: {calc1}\n{contHomem} homens -> idade média: {calc2}\nGrupo -> idade média: {calc3}")

        return self.active


ObjGenero = Genero()