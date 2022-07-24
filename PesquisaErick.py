import tabulate
import datetime
import pandas as pd


class Questionario():
    __Idade = []
    __Genero = []
    __Resposta1 = []
    __Resposta2 = []
    __Resposta3 = []
    __Resposta4 = []
    __Data = []
    __Hora = []

    __dic = {
        'Idade': __Idade,
        'Gênero':__Genero,
        'Pergunta1':__Resposta1,
        'Pergunta2':__Resposta2,
        'Pergunta3':__Resposta3,
        'Pergunta4':__Resposta4,
        'Data da Resposta':__Data,
        'Horário da Resposta':__Hora
    }
    def __init__(self,idade,genero):
        self.__Idade.append(str(idade))
        self.__Genero.append(str(genero))
        

    def respostas(self):
        while True:
            try:
                escolha = int(input('Pergunta1:\n[1]Sim\n[2]Não\n[3]Não sei responder\n'))
                if (escolha != 1) and (escolha!=2) and (escolha != 3):
                    print('Escolha inválida.Tente novamente...')
                else:
                    if escolha == 1:
                        self.__Resposta1.append('Sim')
                        break
                    elif escolha == 2:
                        self.__Resposta1.append('Não')
                        break
                    elif escolha == 3:
                        self.__Resposta1.append('Não sei responder')
                        break
            except:
                print('Escolha inválida.Tente  novamente...')
        while True:
            try:
                escolha = int(input('Pergunta2:\n[1]Sim\n[2]Não\n[3]Não sei responder\n'))
                if (escolha != 1) and (escolha!=2) and (escolha != 3):
                    print('Escolha inválida.Tente novamente...')
                else:
                    if escolha == 1:
                        self.__Resposta2.append('Sim')
                        break
                    elif escolha == 2:
                        self.__Resposta2.append('Não')
                        break
                    elif escolha == 3:
                        self.__Resposta2.append('Não sei responder')
                        break
            except:
                print('Escolha inválida.Tente  novamente...')
        while True:
            try:
                escolha = int(input('Pergunta3:\n[1]Sim\n[2]Não\n[3]Não sei responder\n'))
                if (escolha != 1) and (escolha!=2) and (escolha != 3):
                    print('Escolha inválida.Tente novamente...')
                else:
                    if escolha == 1:
                        self.__Resposta3.append('Sim')
                        break
                    elif escolha == 2:
                        self.__Resposta3.append('Não')
                        break
                    elif escolha == 3:
                        self.__Resposta3.append('Não sei responder')
                        break
            except:
                print('Escolha inválida.Tente  novamente...')
        while True:
            try:
                escolha = int(input('Pergunta4:\n[1]Sim\n[2]Não\n[3]Não sei responder\n'))
                if (escolha != 1) and (escolha!=2) and (escolha != 3):
                    print('Escolha inválida.Tente novamente...')
                else:
                    if escolha == 1:
                        self.__Resposta4.append('Sim')
                        break
                    elif escolha == 2:
                        self.__Resposta4.append('Sim')
                        break
                    elif escolha == 3:
                        self.__Resposta4.append('Não sei responder')
                        break
            except:
                print('Escolha inválida.Tente  novamente...')
        exato = datetime.datetime.now()
        data = exato.strftime('%d/%m/%y')
        self.__Data.append(data)
        momento = exato.strftime("%I:%M %p")
        self.__Hora.append(momento)

       
    def get_info(self):
        return self.__dic

        


class Tabela():
    def __init__(self,dicionario):
        self.__dicionario = dicionario

    def criarTabela(self): # Equivalente a um set_tabela
        self.__pesquisa = pd.DataFrame(self.__dicionario,index= [f'Participante {i+1}:' for i in range(len(self.__dicionario['Idade']))])
        self.__pesquisa.to_csv('teste.csv')    
    def lerTabela(self): # Equivalente a um get_tabela
        print(tabulate.tabulate(self.__pesquisa, headers = 'keys',tablefmt = 'github'))
        print(self.__pesquisa)

count = 0
print('Iniciando a pesquisa...')
while True:
    count += 1
    while True:
        idade = input(f'Participante {count},qual a sua idade?(Digite 00 para sair do programa.)\n')
        if idade != '00': # Verifica se é 00
            if idade.isnumeric(): # Verifica se é um número escrito em formato de string
                idade = int(idade) # Se for,transforma em inteiro e faz o resto.
                if idade >= 0 and idade <= 120:
                    break
                else:
                    print('Idade inválida,digite um número inteiro positivo entre 0 e 120')
            else:
                print('Idade inválida,digite um número Inteiro positivo por favor.')
        else:
            break
    if idade == '00':
        print('Saindo do questionário...')
        break
    while True:
        try:
            escolha_genero = int(input('Qual o seu gênero?\n[1]Masculino\n[2]Feminino\n[3]LGBTQIA+\3\n'))
            if escolha_genero != 1 and escolha_genero != 2 and escolha_genero != 3:
                print('Escolha inválida,tente novamente...')
            else:
                break
        except ValueError:
            print('Digite um número entre 1 e 3 para fazer sua escolha.')
    convidado = Questionario(idade,escolha_genero)
    convidado.respostas()




 

tabela = Tabela(convidado.get_info()) # Entro no objeto tabela passando como argumento um dicionário
tabela.criarTabela()   # Crio a tabela com o pandas
tabela.lerTabela() # Leio oque foi criado