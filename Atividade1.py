MinhaLista = []
while(True):

    Geracao = input("Digite sua geração(X,Y,Z): ")
    Sexo = input("Digite seu Sexo(F,M): ")
    Futebol = input("Digite se já praticou Futebol(S,N): ")
    Brasil = input("Digite se Brasil vai Ganha(S,N): ")
    Continuar = input("Digite se voçê deseja continuar(S,N)")

    MinhaLista.append([Geracao, Sexo, Futebol, Brasil])

    if Continuar == "N":
        break

print(MinhaLista)


