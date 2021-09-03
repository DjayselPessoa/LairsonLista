from BancoDados.exercicio01 import ObjTabuada
from Core.TratamentoStrFloat import ObjTratamento
from BancoDados.exercicio02 import ObjListaMenor
from BancoDados.exercicio03 import ObjInvertido
from BancoDados.exercicio04 import ObjPosition
from BancoDados.exercicio05 import ObjGenero
from BancoDados.exercicio06 import ObjSomatorio

active = True

while active:
    try:
        print("\n")
        print("-" * 50)
        print("-" * 20, "LISTA 02", "-" * 20)
        print("-" * 50)

        print(f"\nTODOS OS EXERCÍCIOS ABAIXO:\n1 - exercício 01 ->\n2 - exercício 02 ->\n3 - exercício 03 ->\n4 - exercício 04 ->\n5 - exercício 05 ->\n6 - exercício 06 ->\n")

        escolha = str(input("\nEscolha de 1 a 6 ou S para sair: "))
        escolha_tratada, active = ObjTratamento.tratamento(escolha, active)
        if active == False:
            raise ValueError("\nDESLIGANDO!")
        elif active == True and escolha_tratada == 0.0:
            raise ValueError("\nDADO INCORRETO - REINICIANDO!")

        else:
            escolha_tratada = int(escolha_tratada)

        if str(escolha_tratada) in "123456":
            if escolha_tratada == 1:
                x = str(input("\nInforme qual TABUADA deseja de 1 a 100: "))
                tratar_x, active = ObjTratamento.tratamento(x, active)
                if active == False:
                    raise ValueError("\nSAINDO!")
                elif active == True and tratar_x == 0.0:
                    raise ValueError("\nDADO INCORRETO! - REINICIANDO!\n")
                else:
                    tratado_x = int(tratar_x)
                active = ObjTabuada.tabuada(tratado_x, active)
                continue
            elif escolha_tratada == 2:
                numLista = []
                for i in range(5):
                    valor = str(input("\nInforme o número desejado: "))
                    valor_tratado, active = ObjTratamento.tratamento(valor, active)

                    if active == False:
                        raise ValueError("\nSAINDO!")
                    elif active == True and valor_tratado == 0.0:
                        raise ValueError("\nDADO INCORRETO! - REINICIANDO!\n")
                    else:
                        valor_tratado = int(valor_tratado)

                    numLista.append(valor_tratado)
                print(numLista)
                active = ObjListaMenor.listaMenor(numLista, active)
                if active == False:
                    raise ValueError("\nSAINDO!")
                else:
                    raise ValueError("\nREINICIANDO!\n")

            elif escolha_tratada == 3:
                active = ObjInvertido.invertido(active)
                if active == False:
                    raise ValueError("\nSAINDO!\n")
                else:
                    raise ValueError("\nREINICIANDO!\n")

            elif escolha_tratada == 4:
                numListaPosition = []
                cont = 1
                for i in range(10):
                    valor_position = str(input(f"Informe o {cont}º valor: "))
                    valor_tratado_position, active = ObjTratamento.tratamento(valor_position, active)

                    if active == False:
                        raise ValueError("\nSAINDO!")
                    if active == True and valor_tratado_position == 0.0:
                        raise ValueError("\nDADO INCORRETO - REINICIANDO!\n")
                    else:
                        valor_tratado_position = int(valor_tratado_position)
                        numListaPosition.append(valor_tratado_position)
                    cont += 1
                active = ObjPosition.position(numListaPosition, active)
            elif escolha_tratada == 5:
                genLista = []
                idadeLista = []
                cont = 1
                for i in range(10):
                    entrada1 = str(input(f"{cont}º - Informe H para homem e M para mulher: "))
                    if entrada1 in "HhMm":
                        genLista.append(entrada1)
                    else:
                        raise ValueError("DADO INCORRETO! - REINICIANDO!")
                    entrada2 = str(input(f"{cont}º - Informe a idade: "))

                    entrada2_final, active = ObjTratamento.tratamento(entrada2, active)

                    if active == False:
                        raise ValueError("SAINDO!")
                    elif active == True and entrada2_final == 0.0:
                        raise ValueError("DADO INCORRETO! - REINICIANDO!")
                    else:
                        entrada2_final = int(entrada2_final)

                    if not 0 <= entrada2_final <= 120:
                        raise ValueError("DADO INCORRETO - REINICIANDO!")
                    else:
                        idadeLista.append(entrada2_final)
                    
                    cont += 1
                active = ObjGenero.genero(idadeLista, genLista, active)
                if active == False:
                    raise ValueError("SAINDO!")
                else:
                    raise ValueError("REINICIANDO!")
            elif escolha_tratada == 6:
                active = ObjSomatorio.somatorio(active)
        else:
            raise ValueError("DADOS INCORRETOS - REINICIANDO!")
    except ValueError as e:
        print("LOG: -> ", e)
