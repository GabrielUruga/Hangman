'''
Pseudocódigo

1. Definir uma lista com palavras possíveis
2. Escolher uma palavra aleatória dessa lista
3. Criar uma lista vazia para armazenar as letras advinhadas
4. Definir qual o limite de tentativas
5. Enquanto não atingir o limite de tentativas:
    a. Mostrar underscore com letras nos lugares corretos
    b. Pedir para o user advinhar uma letra
    c. Verificar se a letra está na palavra
    d. Se a letra pertencer a palavra, adicionar na lista de letras advinhadas e exibir via atualização
    e. Se a letra não pertencer a palavra, reduzir o n° de tentativas e exibir que a letra não está na palavra
'''
import random
from os import system, name

# Função para limpar tela em qualquer sistema operacional
def clearscreen():
    # clear WINDOWS/nt -> versão interna do Windows
    if name == 'nt':
        _ = system('cls')
    
    # clear MAC/LINUX
    else:
        _ = system('clear')

# Função para exibir boas vindas e armazenar a lista de palavras possíveis 
def hangname():
    # limpando tela para começar o game
    clearscreen()

    # boas vindas ao user
    print('\nSeja bem-vindo ao Jogo da Forca Python!\nAdvinhe qual é o artista:\n')

    # nome disponíveis dos artistas
    artistas = ['kyan','yunk vino','veigh','borges','bc raff','tz da coronel','vulgo fk','kayblack']

    # escolhendo aleatoriamente qual artista com função CHOICE do módulo RANDOM
    artista = random.choice(artistas) 

    # imprimindo a quantia de underscores da palavra na tela
    letracerta = ['_' for letra in artista]

    # limite de erro
    limite = 8

    # Lista vazia para armazenar letras erradas
    letraerrada = []
    
    while limite > 0:
        print(' '.join(letracerta))
        print('\nTentativas: ', limite)
        print('Letra errada: ', ' '.join(letraerrada))
        # o método JOIN junta o que há na direita com o que há na esquerda

        letra = input('\nInsira uma letra: ').lower()

        # check se a letra está correta ou errada
        if letra in artista:
            index = 0
            for tentativa in artista:
                if letra == tentativa:
                    letracerta[index] = tentativa
                index += 1
        else:
            limite -=1
            letraerrada.append(letra)

        if '_' not in letracerta:
            print('\nVocê venceu, o artista era: ', artista.capitalize())
            break
    if '_' in letracerta:
        print('Você perdeu, o artista era: ', artista.capitalize())
    
# Bloco MAIN -> para informar ao programa que o script é um módulo python
if __name__ == '__main__':
    hangname()
    print('Estou aprendendo Python no curso da DSA')