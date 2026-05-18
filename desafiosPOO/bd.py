from desafiosPOO.clasCB005 import *
from desafiosPOO.modulo_aux import linha
conta = ContaBancaria

def pastaExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a=open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro inesperado!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        for n in a:
            dado = n.split(';')
            dado[1] = dado[1].replace('\n','')
            conta.informacoes(dado)
    finally:
        a.close()

def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at') # 'at' para anexar (append) ao texto
    except:
        print('Erro ao abrir o arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao escrever os dados!')
        else:
            a.close()