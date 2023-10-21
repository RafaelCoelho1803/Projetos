Contagem = 0
Cont1 = 0
Cont2 = 0
Cont3 = 0
Cont4 = 0
IdadeMaior = 0
IdadeMenor = 100
AvaliacaoMaiorIdade = ""  # Variável para armazenar a avaliação da maior idade
AvaliacaoMenorIdade = ""  # Variável para armazenar a avaliação da menor idade
Avaliacao = ""
AvaliacaoM = ""

def verificar_idade_e_avaliacao(Idade, IdadeMaior, Qualidade):
    if Idade > IdadeMaior:
        return Idade, Qualidade
    else:
        return IdadeMaior, AvaliacaoMaiorIdade

def verificar_idade_e_avaliacao_Menor(Idade, IdadeMenor, Qualidade):
    if Idade < IdadeMenor:
        return Idade, Qualidade
    else:
        return IdadeMenor, AvaliacaoMenorIdade

while True:
    Contagem = Contagem + 1
    Idade = int(input("Qual a sua idade?"))
    Qualidade = input("Qualidade do Atendimento 1-Ótimo, 2-Bom, 3-Regular, 4-Péssimo")
    Refazer = input("Deseja refazer o formulário? (S , N)")

    IdadeMaior, AvaliacaoMaiorIdade = verificar_idade_e_avaliacao(Idade, IdadeMaior, Qualidade)
    IdadeMenor, AvaliacaoMenorIdade = verificar_idade_e_avaliacao_Menor(Idade, IdadeMenor, Qualidade)

    if Contagem == 1:
        Cont1 += 1
    elif Contagem == 2:
        Cont2 += 1
    elif Contagem == 3:
        Cont3 += 1
    elif Contagem == 4:
        Cont4 += 1

    if Refazer == "N":
        break



if AvaliacaoMaiorIdade == "1":
    Avaliacao = "Ótimo"
elif AvaliacaoMaiorIdade == "2":
    Avaliacao = "Bom"
elif AvaliacaoMaiorIdade == "3":
    Avaliacao = "Regular"
elif AvaliacaoMaiorIdade == "4":
    Avaliacao = "Ruim"

if AvaliacaoMenorIdade == "1":
    AvaliacaoM = "Ótimo"
elif AvaliacaoMenorIdade == "2":
    AvaliacaoM = "Bom"
elif AvaliacaoMenorIdade == "3":
    AvaliacaoM = "Regular"
elif AvaliacaoMenorIdade == "4":
    AvaliacaoM = "Ruim"



print("O número de respostas ao formulário foi:", Contagem)
print("Quantidade de avaliações foi de:", Cont1, "-Ótimo, ", Cont2, "-Bom, ", Cont3, "-Regular, ", Cont4, "-Ruim.")
print("A maior idade registrada foi:", IdadeMaior,"e sua avialição foi: ", Avaliacao)
print("A menor idade registrada foi:", IdadeMenor,"e sua avialição foi: ", AvaliacaoM)

