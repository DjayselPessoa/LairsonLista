class Invertido:

    def invertido(self, active):
        self.active = active
        valor = 500
        for i in range(501):
            ordem = int(i) + 1
            if valor == 0:
                return self.active
            print(f"{ordem}º número: {valor}")
            valor -= 1
        return self.active


ObjInvertido = Invertido()