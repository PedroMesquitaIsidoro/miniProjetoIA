import csv

def funcao(v, alfabeto, ant, confianca):

    ant = [item.replace(" ", "") for item in ant]
    k = 0
    aux = []
    aux2 = []
    cont = 0
    while cont < 10:
        k = 0
        for i in alfabeto:
            if i in v:
                aux.append("1")
            else:
                aux.append("0")
        print("auxiliar 1")
        print(aux)
        for i in alfabeto:
            aux2.append(alfabeto[k] + " = " + aux[k])
            k = k + 1
        print("auxiliar 2")
        print(aux2)

        if "fadiga = 1" in aux2 and "dorCabeca = 1" in aux2 and "dorCorpo = 1" in aux2 and "dorGarganta = 1" in aux2 and "tosse = 1" in aux2:
            aux2 = [l.replace("covid = 0", "covid= 1") for l in aux2 ]

        if "dorCabeca = 1" in aux2 and "gargantaInflamada = 1" in aux2 and "tosse = 1" in aux2:
            aux2 = [l.replace("gripe = 0", "gripe = 1") for l in aux2 ]

        if "cansaco = 1" in aux2 and "dorCabeca = 1" in aux2:
            aux2 = [l.replace("mononucleoseInfecciosa = 0", "mononucleoseInfecciosa = 1") for l in aux2 ]

        if "cansaco = 1" in aux2 and "gargantaInflamada = 1" in aux2:
            aux2 = [l.replace("emigdalite = 0", "emigdalite = 1") for l in aux2 ]

        if "cansaco = 1" in aux2:
            aux2 = [l.replace("estresse = 0", "estresse = 1") for l in aux2 ]

        if "fadiga = 1" in aux2 and "dorCabeca  = 1" in aux2 and "pulsacaoElevada = 1" in aux2 and "baixoNivelOxigenio = 1" in aux2 and "perdaOlfato = 1" in aux2 and "perdaPaladar = 1" in aux2:
            aux2 = [l.replace("covid = 0", "covid = 1") for l in aux2 ]

        if "coriza = 1" in aux2 and "espirro = 1" in aux2:
            aux2 = [l.replace("riniteAlergica = 0", "riniteAlergica = 1") for l in aux2 ]

        if "dorCabeca = 1" in aux2 and "coriza = 1" in aux2:
            aux2 = [l.replace("sinusite = 0", "sinusite = 1") for l in aux2 ]
        cont = cont + 1

    diagnostico = ["covid", "gripe", "mononucleoseInfecciosa", "emigdalite", "estresse", "riniteAlergica", "sinusite", "dengue", "chicungunha"]
    grauCerteza = 1
    for diagnostico in diagnostico:
        if diagnostico + " = 1" in aux2:
            if diagnostico == "covid":
                if "fadiga = 1" in aux2 and "dorCabeca = 1" in aux2 and "dorCorpo = 1" in aux2 and "dorGarganta = 1" in aux2 and "tosse = 1" in aux2:
                   grauCerteza = 0.8 * confianca[0] * confianca[1] * confianca[2] * confianca[3] * confianca[4]

                elif "fadiga = 1" in aux2 and "dorCabeca  = 1" in aux2 and "pulsacaoElevada = 1" in aux2 and "baixoNivelOxigenio = 1" in aux2 and "perdaOlfato = 1" in aux2 and "perdaPaladar = 1" in aux2:
                    grauCerteza = 0.9 * confianca[0] * confianca[1] * confianca[8] * confianca[9] * confianca[10] * confianca[11]

            elif diagnostico == "gripe":
                if "dorCabeca = 1" in aux2 and "gargantaInflamada = 1" in aux2 and "tosse = 1" in aux2:
                    grauCerteza = 0.9 * confianca[1] * confianca[5] * confianca[4]

            elif diagnostico == "mononucleoseInfecciosa":
                if "cansaco = 1" in aux2 and "dorCabeca = 1" in aux2:
                    grauCerteza = 0.95 * confianca[1] * confianca[7]

            elif diagnostico == "emigdalite":
                if "cansaco = 1" in aux2 and "gargantaInflamada = 1" in aux2:
                    grauCerteza = 0.9 * confianca[7] * confianca[5]

            elif diagnostico == "estresse":
                if "cansaco = 1" in aux2:
                    grauCerteza = 0.7 * confianca[7]

            elif diagnostico == "riniteAlergica":
                if "coriza = 1" in aux2 and "espirro = 1" in aux2:
                    grauCerteza = 0.85 * confianca[12] * confianca[13]

            elif diagnostico == "sinusite":
                if "dorCabeca = 1" in aux2 and "coriza = 1" in aux2:
                    grauCerteza = 0.8 * confianca[1] * confianca[12]
            print("Diagnostico eh: ")
            print(diagnostico)
            print("Grau de certeza eh porcentagem %: ")
            print(grauCerteza*100)

    return

if __name__ == "__main__":
    alfabeto = []
    ant = []
    dec = []
    ant_and_dec = []
    v = []
    confianca = []
    caracteristicas = ["fadiga", "dorCabeca", "dorCorpo", "dorGarganta", "tosse", "covid",
                       "gargantaInflamada", "gripe",
                       "cansaco", "mononucleoseInfecciosa",
                       "emigdalite",
                       "estresse",
                       "pulsacaoElevada", "baixoNivelOxigenio", "perdaOlfato", "perdaPaladar",
                       "coriza", "espirro", "riniteAlergica",
                       "sinusite",
                       "dengue", "chicungunha"]
    perguntas = ["Voce esta com fadiga? - S/N",
                 "Voce esta com dor de cabeca? - S/N",
                 "Voce esta com dor no corpo? - S/N",
                 "Voce esta com dor de garganta? - S/N",
                 "Voce esta com tosse? - S/N",
                 "Voce esta com garganta inflamada? - S/N",
                 "Voce esta com cansaco? - S/N",
                 "Voce esta com pulsacao elevada? - S/N",
                 "Voce esta com baixo nivel de oxigenio? - S/N",
                 "Voce esta com perda de olfato? - S/N",
                 "Voce esta com perda de paladar? - S/N",
                 "Voce esta com coriza - S/N",
                 "Voce esta com espirro? - S/N"]

    with open("./regrasDoencas.csv", "r") as regras:
        regras = csv.reader(regras)
        next(regras)

        for i in regras:
            ant.append(i[0])
            dec.append(i[1])
            ant_and_dec.append(i[0]+">"+i[1])

    for i in caracteristicas:
        if i in caracteristicas and i not in alfabeto:
            alfabeto.append(i)

    # comecando

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
            with open("./regrasDoencas.csv", "r") as regras:
                regras = csv.reader(regras)
                next(regras)

                for i in regras:
                    print(i)
            print("-----------------------------------------")
        elif k == 2:
            x = 0
            while x < 13:

                if "fadiga" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("fadiga")
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)
                    else:
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)

                if "cabeca" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("dorCabeca")
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)
                    else:
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)

                if "corpo" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("dorCorpo")
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)
                    else:
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)

                if "garganta" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("dorGarganta")
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)
                    else:
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)

                if "tosse" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("tosse")
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)
                    else:
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)

                if "inflamada" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("gargantaInflamada")
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)
                    else:
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)

                if "cansaco" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("cansaco")
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)
                    else:
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)

                if "pulsacao elevada" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("pulsacaoElevada")
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)
                    else:
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)

                if "oxigenio" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("baixoNivelOxigenio")
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)
                    else:
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)

                if "olfato" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("perdaOlfato")
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)
                    else:
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)

                if "paladar" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("perdaPaladar")
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)
                    else:
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)

                if "coriza" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("coriza")
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)
                    else:
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)

                if "espirro" in perguntas[x]:
                    r = str(input(f"{perguntas[x]}"))
                    if r.upper() == "S":
                        v.append("espirro")
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)
                    else:
                        r2 = float(input("Grau de certeza: - x%"))
                        confianca.append(r2/100)

                x = x + 1
            print("alfabeto")
            print(alfabeto)
            print("verdadeiros")
            print(v)
            print(confianca)
            k = 0
            funcao(v, alfabeto, ant, confianca)