class Tratamento:

    def tratamento(self, tratarValor, activeRecebido):
        try:
            self.tratarValor = tratarValor
            self.activeRecebido = activeRecebido
            active = self.activeRecebido
            qnt_catactere = len(tratarValor)
            cont = 0
            tratarValor = str(self.tratarValor)

            if tratarValor in "Ss":
                active = False
                tratarValor = 0.0
                return tratarValor, active

            if tratarValor.find(","):
                tratarValor = tratarValor.replace(",", ".")
                for i in range(qnt_catactere):
                    if tratarValor[i] in "0123456789.":
                        if tratarValor[i] == ".":
                            cont += 1
                            if cont > 1:
                                print("DADO INCORRETO! - REINICIANDO!")
                                tratarValor = 0.0
                                return tratarValor, active
                    else:
                        print("DADO INCORRETO! - REINICIANDO!")
                        tratarValor = 0.0
                        return tratarValor, active
                tratarValor = float(tratarValor)
                return tratarValor, active
            elif tratarValor.find("."):
                for i in range(qnt_catactere):
                    if tratarValor[i] in "0123456789.":
                        if tratarValor[i] == ".":
                            cont += 1
                            if cont > 1:
                                print("DADO INCORRETO! - REINICIANDO!")
                                tratarValor = 0.0
                                return tratarValor, active
                    else:
                        print("DADO INCORRETO! - REINICIANDO!")
                        tratarValor = 0.0
                        return tratarValor, active
                tratarValor = float(tratarValor)
                return tratarValor, active

            if not -999999999.9 <= tratarValor <= 999999999.9:
                raise ValueError("DADO INCORRETO!")

            else:
                tratarValor = float(tratarValor)
                return tratarValor, active
        except ValueError as e:
            print("LOG: -> ", e)


ObjTratamento = Tratamento()
