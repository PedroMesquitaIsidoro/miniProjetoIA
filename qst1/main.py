import csv

def funcao(v, alfabeto, ant):
    ant = [item.replace(" ", "") for item in ant]
    k = 0
    aux = []
    aux2 = []
    cont = 0
    while cont < 10:
        k = 0
        for i in alfabeto:
            if i in v:
                aux.append(1)
            else:
                aux.append(0)
        print("auxiliar 1")
        print(aux)
        for j in alfabeto:
            aux2.append(alfabeto[k] + " = " + str(aux[k]))
            k = k + 1
        print("auxiliar 2")
        print(aux2)

        if "pelo = 1" in aux2:
            aux2 = [l.replace("mamifero = 0", "mamifero = 1") for l in aux2 ]

        elif "leite = 1" in aux2:
            aux2 = [l.replace("mamifero = 0", "mamifero = 1") for l in aux2 ]

        elif "penas = 1" in aux2:
            aux2 = [l.replace("ave = 0", "ave = 1") for l in aux2 ]

        elif "plana = 1" and "bota-ovos = 1" in aux2:
            aux2 = [l.replace("ave = 0", "ave = 1") for l in aux2 ]

        elif "mamifero = 1" and "come-carne = 1" in aux2:
            aux2 = [l.replace("carnivoro = 0", "carnivoro = 1") for l in aux2 ]

        elif "mamifero = 1" and "dentes-pontiagudos = 1" and "garras = 1" and "olhos-frontais = 1" in aux2:
            aux2 = [l.replace("carnivoro = 0", "carnivoro = 1") for l in aux2 ]

        elif "mamifero = 1" and "casco = 1" in aux2:
            aux2 = [l.replace("ungulado = 0", "ungulado = 1") for l in aux2 ]

        elif "mamifero = 1" and "rumina = 1" and "dedos-pares = 1" in aux2:
            aux2 = [l.replace("ungulado = 0", "ungulado = 1") for l in aux2 ]

        elif "carnivoro = 1" and "amarelo-tostado = 1" and "manchas-escuras = 1" in aux2:
            aux2 = [l.replace("leopardo = 0", "leopardo = 1") for l in aux2]

        elif "carnívoro = 1" and "amarelo-tostado = 1" and "listaNegra = 1" in aux2:
            aux2 = [l.replace("tigre = 0", "tigre = 1") for l in aux2]

        elif "ungulado = 1" and "pernas-longas = 1" and "pescoco-comprido = 1" and "amarelo-tostado = 1" and "manchas-escuras = 1" in aux2:
            aux2 = [l.replace("girafa = 0", "girafa = 1") for l in aux2]

        elif "ungulado = 1" and "branca = 1" and "listaNegra = 1" in aux2:
            aux2 = [l.replace("zebra = 0", "zebra = 1") for l in aux2]

        elif "ave = 1" and "pernas-longas = 1" and "pescoco-comprido = 1" and "preto-e-branco = 1" in aux2:
            aux2 = [l.replace("avestruz = 0", "avestruz = 1") for l in aux2]

        elif "ave = 1" and "nao-voa = 1" and "nada = 1" and "preto-e-branco = 1" in aux2:
            aux2 = [l.replace("pinguim = 0", "pinguim = 1") for l in aux2]

        elif "ave = 1" in aux2:
            if "bonvoador = 1" in aux2:
                aux2 = [l.replace("albatroz = 0", "albatroz = 1") for l in aux2]

        elif "ave = 1" and "corpo-arredondado = 1" and "plumas-densas = 1" and "nao-voa = 1" and "domestico = 1" in aux2:
            aux2 = [l.replace("galinha = 0", "galinha = 1") for l in aux2]

        elif "ave = 1" and "pernas-longas = 1" and "pescoco-comprido = 1" and "cauda-curta = 1" and "rosa = 1" in aux2:
            aux2 = [l.replace("flamingo = 0", "flamingo = 1") for l in aux2]
        cont = cont + 1
    bichos = ["leopardo", "tigre", "girafa", "zebra", "avestruz", "pinguim", "albatroz", "galinha", "flamingo"]

    for bicho in bichos:
        if bicho + " = 1" in aux2:
            print("O ANIMAL EH: ")
            print(bicho)
            return
    print(("Bicho nao encontrado"))


if __name__ == "__main__":
    alfabeto = []
    ant = []
    dec = []
    ant_and_dec = []
    v = []
    caracteristicas = ["pelo", "mamifero", "leite", "penas", "ave", "plana", "bota-ovos", "come-carne", "carnivoro",
           "dentes-pontiagudos", "garras", "olhos-frontais", "casco", "ungulado", "rumina", "dedos-pares",
           "amarelo-tostado", "manchas-escuras", "leopardo", "listaNegra", "tigre", "pernas-longas",
           "pescoco-comprido", "girafa", "branca", "zebra", "preto-e-branco", "avestruz", "nao-voa", "nada", "pinguim",
           "bonvoador", "albatroz", "corpo-arredondado", "plumas-densas", "domestico", "galinha", "cauda-curta", "rosa",
           "flamingo"]
    perguntas = ["Seu animal tem pelo? - S/N",
                 "Seu animal dá leite? - S/N",
                 "Seu animal tem penas? - S/N",
                 "Seu animal plana? - S/N",
                 "Seu animal bota ovos? -S/N",
                 "Seu animal come carne? - S/N",
                 "Seu animal tem dentes pontiagudos? - S/N",
                 "Seu animal tem garras? - S/N",
                 "Seu animal tem olhos frontais - S/N",
                 "Seu animal tem casco - S/N",
                 "Seu animal rumina - S/N",
                 "Seu animal tem dedos pares - S/N",
                 "Seu animal tem cor amarelo tostado- S/N",
                 "Seu animal tem manchas escuras - S/N",
                 "Seu animal tem listaNegra - S/N",
                 "Seu animal tem pernas longas- S/N",
                 "Seu animal tem pescoco comprido- S/N",
                 "Seu animal tem cor branca - S/N",
                 "Seu animal tem cor preto e branco - S/N",
                 "Seu animal tem plumas-densas- S/N",
                 "Seu animal nao voa- S/N",
                 "Seu animal nada?- S/N",
                 "Seu animal eh um bonvoador- S/N",
                 "Seu animal tem corpo arredondado - S/N",
                 "Seu animal tem pernas densas - S/N",
                 "Seu animal eh domestico- S/N",
                 "Seu animal tem cauda curta - S/N",
                 "Seu animal eh rosa?- S/N",]

    with open("./ConjuntoRegras.csv", "r") as regras:
        regras = csv.reader(regras)
        next(regras)

        for i in regras:
            ant.append(i[0])
            dec.append(i[1])
            ant_and_dec.append(i[0]+">"+i[1])


    for i in caracteristicas:
        if i in caracteristicas and i not in alfabeto:
            alfabeto.append(i)
    #print(alfabeto)


    print("------------- animal ------------")
    k = -1
    while k != 0:
        print(k)
        print("[0] SAIR")
        print("[1] VISUALIZAR AS REGRAS")
        print("[2] FAZER AS PERGUNTAS E EXECUTAR")
        k = int(input("Digite uma opcao: "))
        if k == 0:
            print("saindo...")
        elif k == 1:
            print("----------------REGRAS------------------")
            with open("./ConjuntoRegras.csv", "r") as regras:
                regras = csv.reader(regras)
                next(regras)

                for i in regras:
                    print(i)
            print("-----------------------------------------")
        elif k == 2:
            x = 0
            while x < 28:

                if "pelo" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("pelo")

                elif "leite" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("leite")

                elif "penas" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("penas")

                elif "plana" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("plana")

                elif "bota ovos" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("bota-ovos")

                elif "come carne" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("come-carne")

                elif "dentes pontiagudos" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("dentes-pontiagudos")

                elif "garras" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("garras")

                elif "olhos frontais" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("olhos-frontais")

                elif "casco" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("casco")

                elif "rumina" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("rumina")

                elif "dedos pares" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("dedos-pares")

                elif "amarelo tostado" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("amarelo-tostado")

                elif "manchas escuras" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("manchas-escuras")

                elif "listaNegra" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("listaNegra")

                elif "pernas longas" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("pernas-longas")

                elif "pescoco comprido" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("pescoco-comprido")

                elif "cor branca" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("branca")

                elif "cor preto e branco" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("preto-e-branco")

                elif "plumas-densas" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("plumas-densas")

                elif "nao voa" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("nao-voa")

                elif "nada" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("nada")

                elif "bonvoador" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("bonvoador")

                elif "corpo arredondado" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("corpo-arredondado")

                elif "pernas densas" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))

                elif "domestico" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("domestico")

                elif "cauda curta" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("cauda-curta")

                elif "eh rosa" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("rosa")
                x = x + 1
            print("alfabeto")
            print(alfabeto)
            print("verdadeiros")
            print(v)
            funcao(v, alfabeto, ant)
            k = 0







