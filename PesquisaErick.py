from asyncore import write
import csv
import datetime


class Perguntas():
    resposta1 = 1
    resposta2 = 1
    resposta3 = 1
    resposta4 = 1
    def __init__(self,idade,genero):
        self.idade = idade
        self.genero = genero

    def respostas(self):
        while True:
            try:
                escolha = int(input('Pergunta1:\n[1]Sim\n[2]Não\n[3]Não sei responder\n'))
                if (escolha != 1) and (escolha!=2) and (escolha != 3):
                    print('Escolha inválida.Tente novamente...')
                else:
                    self.resposta1 = escolha
                    break
            except:
                print('Escolha inválida.Tente  novamente...')
        while True:
            try:
                escolha = int(input('Pergunta2:\n[1]Sim\n[2]Não\n[3]Não sei responder\n'))
                if (escolha != 1) and (escolha!=2) and (escolha != 3):
                    print('Escolha inválida.Tente novamente...')
                else:
                    self.resposta2 = escolha
                    break
            except:
                print('Escolha inválida.Tente  novamente...')
        while True:
            try:
                escolha = int(input('Pergunta3:\n[1]Sim\n[2]Não\n[3]Não sei responder\n'))
                if (escolha != 1) and (escolha!=2) and (escolha != 3):
                    print('Escolha inválida.Tente novamente...')
                else:
                    self.resposta3 = escolha
                    break
            except:
                print('Escolha inválida.Tente  novamente...')
        while True:
            try:
                escolha = int(input('Pergunta4:\n[1]Sim\n[2]Não\n[3]Não sei responder\n'))
                if (escolha != 1) and (escolha!=2) and (escolha != 3):
                    print('Escolha inválida.Tente novamente...')
                else:
                    self.resposta4 = escolha
                    break
            except:
                print('Escolha inválida.Tente  novamente...')
        exato = datetime.datetime.now()
        data = exato.strftime('%d/%m/%y')
        momento = exato.strftime("%I:%M%p")
        return [self.idade,self.genero,self.resposta1,self.resposta2,self.resposta3,self.resposta4,data,momento]

# def inserirRespostas(pessoa = None):
#     with open('teste.csv', mode = 'a') as arquivo:
#         for coluna in leitor:
#             if linhas == 0:
#                 conc = ' '.join(coluna)
#                 print(f'\tColunas: {conc}')
#                 linhas += 1
#             else:
                
#                 print(f'\tPessoa {linhas}: {coluna}')
#                 linhas += 1
#         print(f'Foram lidas {linhas} linhas.') 

pessoa = []
print('Programa iniciando')
while True:
    while True:
        try:
            idade = int(input('Qual a sua idade?(Digite 0 para sair do programa.)\n'))
            if idade >= 0 and idade <= 120:
                break
            else:
                print('Idade inválida,digite um número inteiro positivo entre 0 e 120')
        except ValueError:
            print('Idade inválida,digite um número Inteiro positivo por favor.')
    if idade == 0:
        print('Saindo do questionário...')
        break
    genero = input('Qual o seu gênero? ')
    convidado = Perguntas(idade,genero)
    pessoa.append(convidado.respostas())
pessoa    
    

