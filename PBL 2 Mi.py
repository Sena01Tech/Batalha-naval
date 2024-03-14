# Autor: Luiz Felipe Santana Sena
# Componente Curricular: Algoritmos I
# Concluído em: //202
# Declaro que este código foi elaborado por mim de forma individual e não contém
# nenhum trecho de código de colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação do autor e a fonte do
# código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

#como fazer para identificar que o navio foi abatido 
#fazer um contador para navios derrubados para printar em jogadas 
#usar lista de tuplas para guardar a posição do navio
#Usar a dicionario de tuplas para definir se o navio afundou ou não
#se variavel contCaseNavioAbatido = 16 o jogo acaba e temos um vitorioso
#começar o laço principal do jogo


import random

# numero 0 sem cor significa agua não atngida sem cor no fundo
# numero 0 vermelho significa navio não atingido  '\033[0;30;41m0\033[m'

# numero 0 azul significa parte da agua onde ja levou tiro '\033[0;30;44m0\033[m'
# numero 0 verde significa parte do navio derrubado '\033[0;30;42m0\033[m'



# contador para cases de navios abatidos, quando chegar a 16 o jogo acaba
# navios abatidos somente até 6
contCaseNavioAbatidoPC = 0
contCaseNavioAbatidoJogador = 0

# só precisa de 3 tabuleiros pq não precisa ocultar para o PC
# alocando espaço de memoria para as matrizes
campoJogador = []
campoComputador = []
campoComputadorExibido = [] 



# criando 3 matrizes,como o campo de batalha com 10 listas de 10 variaveis formato STR '0'
for a in range(10):
    campoJogador.append(['0'] * 10)
for a in range(10):
    campoComputador.append(['0'] * 10)
for a in range(10):
    campoComputadorExibido.append(['0'] * 10)

# Tratamento para retorar o valor caso seja inteiro, se não retorna booleano falso, alem disso verifica max e min 
def tratamentoValueError(teste_Menor, teste_Maior, mensagemIntro):
    print(mensagemIntro)
    x = 5
    while x == 5:
        try:
            teste = int(input('digite:'))
            if teste >= teste_Menor and teste <= teste_Maior:
                print('Numero valido ! :)')
                x = 4
            else:
                print('Caractere/numero invaido ! :(')
        except ValueError:
            print('Caractere/numero invalido !')
    new_var = teste
    return new_var

# fazer a matriz se parecer com um tabuleiro ou campo de 10x10
# para facilitar visualização durante o jogo 
d = 'o campo do jogador 1 ficou assim:'
x = 'o campo do computador ficou assim '

def tabuleiro(arrumar):
    print('   1 2 3 4 5 6 7 8 9 10')
    linhaM = 1
    for linha in arrumar:
        if linhaM == 10:
            print('%d|%s|' % (linhaM,' '.join(linha)))
        else:
            print('%d |%s|' % (linhaM, ' '.join(linha)))
        linhaM += 1

# fazer o jogador posicionar seus barcos, sem superpor e nem distanciar as cases do barco
# o Usuario vai escolher a primeira ordenada e escolher se deseja o navio vai ser na horizontal ou vertical, assim o programa vai completar com as proximas cases na horizontal ou vertical 

def gerarNavioGJogador():
    print('crie um navio grande, sendo ele de 4x1 ou 1x4')
    c = 'Escolha 1 para colocar o navio na horizontal e 2 para seu navio na vertical'
    orientacao = tratamentoValueError(1,2,c) # '1' para navio 4x1 e '2' para navio 1x4
    if orientacao == 1:
        a = 'escolha em que linha seu navio vai ficar de 1 a 10'
        linha = tratamentoValueError(1,10,a)
        b = 'escolha em qual coluna seu navio vai começar de 1 a 7, lembrando que como ele é grande, ele se estende por mais 3 colunas'
        coluna = tratamentoValueError(1,7,b)
        campoJogador[linha - 1][coluna - 1], campoJogador[linha - 1][coluna], campoJogador[linha - 1][coluna + 1], campoJogador[linha - 1][coluna + 2] = '\033[0;30;41m0\033[m', '\033[0;30;41m0\033[m', '\033[0;30;41m0\033[m', '\033[0;30;41m0\033[m' # numero 0 vermelho
    elif orientacao == 2:
        a = 'escolha em qual coluna seu navio vai começar de 1 a 7, lembrando que como ele é grande, ele se estende por mais 3 linhas'
        linha = tratamentoValueError(1,7,a)
        b = 'escolha em que linha seu navio vai ficar de 1 a 10'
        coluna = tratamentoValueError(1,10,b)
        campoJogador[linha - 1][coluna - 1], campoJogador[linha][coluna - 1], campoJogador[linha + 1][coluna - 1], campoJogador[linha + 2][coluna - 1] = '\033[0;30;41m0\033[m', '\033[0;30;41m0\033[m', '\033[0;30;41m0\033[m', '\033[0;30;41m0\033[m' # numero 0 vermelho
    print('o navio grande ficou assim:')
    tabuleiro(campoJogador)

def gerar2NavioMJogador():
    print('crie dois navios medios, sendo cada um deles de 3x1 ou 1x3')
    for i in range(2):
        c = 'escolha 1 para usar o navio 3x1 e 2 pra usar o navio 1x3'
        orientacao = tratamentoValueError(1,2,c) # '1' para navio 3x1 e '2' para navio 1x3
        if orientacao == 1:
            a = 'escolha em que linha seu navio vai ficar de 1 a 10'
            linha = tratamentoValueError(1,10,a)
            b = 'escolha em qual coluna seu navio vai começar de 1 a 8, lembrando que como ele é grande, ele se estende por mais 2 colunas'
            coluna = tratamentoValueError(1,8,b)
            while campoJogador[linha - 1][coluna - 1] == '\033[0;30;41m0\033[m' or campoJogador[linha - 1][coluna] == '\033[0;30;41m0\033[m' or campoJogador[linha - 1][coluna + 1] == '\033[0;30;41m0\033[m':
                print('já existe navio nesta posição')
                print('-'* 50)
                a = 'escolha em que linha seu navio vai ficar de 1 a 10'
                linha = tratamentoValueError(1,10,a)
                b = 'escolha em qual coluna seu navio vai começar de 1 a 8, lembrando que como ele é grande, ele se estende por mais 2 colunas'
                coluna = tratamentoValueError(1,8,b)
            campoJogador[linha - 1][coluna - 1], campoJogador[linha - 1][coluna], campoJogador[linha - 1][coluna + 1] = '\033[0;30;41m0\033[m', '\033[0;30;41m0\033[m', '\033[0;30;41m0\033[m' # numero 0 vvermelho
        elif orientacao == 2:
            a = 'escolha em qual coluna seu navio vai começar de 1 a 8, lembrando que como ele é grande, ele se estende por mais 2 linhas'
            linha = tratamentoValueError(1,8,a)
            b = 'escolha em que linha seu navio vai ficar de 1 a 10'
            coluna = tratamentoValueError(1,10,b)
            while campoJogador[linha - 1][coluna - 1] == '\033[0;30;41m0\033[m' or campoJogador[linha][coluna - 1] == '\033[0;30;41m0\033[m' or campoJogador[linha + 1][coluna - 1] == '\033[0;30;41m0\033[m':
                print('já existe navio nesta posição')
                print('-'* 50)
                a = 'escolha em qual coluna seu navio vai começar de 1 a 8, lembrando que como ele é grande, ele se estende por mais 2 linhas'
                linha = tratamentoValueError(1,8,a)
                b = 'escolha em que linha seu navio vai ficar de 1 a 10'
                coluna = tratamentoValueError(1,10,b)
            campoJogador[linha - 1][coluna - 1], campoJogador[linha][coluna - 1], campoJogador[linha + 1][coluna - 1] = '\033[0;30;41m0\033[m', '\033[0;30;41m0\033[m', '\033[0;30;41m0\033[m' # numero 0 vermelho
    print('os navios medios ficaram assim:')
    tabuleiro(campoJogador)

def gerar3NavioPJogador():
    print('crie três navios pequenos, sendo cada um deles de 2x1 ou 1x2')
    for i in range(3):
        c = 'escolha 1 para usar o navio 2x1 e 2 pra usar o navio 1x2'
        orientacao = tratamentoValueError(1,2,c) # '1' para navio 3x1 e '2' para navio 1x3
        if orientacao == 1:
            a = 'escolha em que linha seu navio vai ficar de 1 a 10'
            linha = tratamentoValueError(1,10,a)
            b = 'escolha em qual coluna seu navio vai começar de 1 a 9, lembrando que como ele é grande, ele se estende por mais 1 coluna'
            coluna = tratamentoValueError(1,9,b)
            while campoJogador[linha - 1][coluna - 1] == '\033[0;30;41m0\033[m' or campoJogador[linha - 1][coluna] == '\033[0;30;41m0\033[m':
                print('já existe navio nesta posição')
                print('-'* 50)
                a = 'escolha em que linha seu navio vai ficar de 1 a 10'
                linha = tratamentoValueError(1,10,a)
                b = 'escolha em qual coluna seu navio vai começar de 1 a 9, lembrando que como ele é grande, ele se estende por mais 1 coluna'
                coluna = tratamentoValueError(1,9,b)
            campoJogador[linha - 1][coluna - 1], campoJogador[linha - 1][coluna] = '\033[0;30;41m0\033[m', '\033[0;30;41m0\033[m' # numero 0 vermelho
        elif orientacao == 2:
            a = 'escolha em qual coluna seu navio vai começar de 1 a 9, lembrando que como ele é pequeno, ele se estende por mais 1 linha'
            linha = tratamentoValueError(1,9,a)
            b = 'escolha em que linha seu navio vai ficar de 1 a 10'
            coluna = tratamentoValueError(1,10,b)
            while campoJogador[linha - 1][coluna - 1] == '\033[0;30;41m0\033[m' or campoJogador[linha][coluna - 1] == '\033[0;30;41m0\033[m':
                print('já existe navio nesta posição')
                print('-'* 50)
                a = 'escolha em qual coluna seu navio vai começar de 1 a 9, lembrando que como ele é grande, ele se estende por mais 1 linha'
                linha = tratamentoValueError(1,9,a)
                b = 'escolha em que linha seu navio vai ficar de 1 a 10'
                coluna = tratamentoValueError(1,10,b)
            campoJogador[linha - 1][coluna - 1], campoJogador[linha][coluna - 1] = '\033[0;30;41m0\033[m', '\033[0;30;41m0\033[m' # numero 0 vermelho
    print('Os navios pequenos ficaram assim')
    tabuleiro(campoJogador)

# fazer o computador gerar seus navios, grande de 4x1 ou 1x4, medio de 3x1 ou 1x3, pequeno de 2x1 ou 1x2
def gerarNavioGComputador():
    orientacao = random.randint(1,2) # '1' para navio 4x1 e '2' para navio 1x4
    if orientacao == 1:
        linha = random.randint(0,9)
        coluna = random.randint(0,6)
        campoComputador[linha][coluna], campoComputador[linha][coluna + 1], campoComputador[linha][coluna + 2], campoComputador[linha][coluna + 3] = '\033[0;30;41m0\033[m', '\033[0;30;41m0\033[m', '\033[0;30;41m0\033[m', '\033[0;30;41m0\033[m' # numero 0 vermelho
    elif orientacao == 2:
        linha = random.randint(0,6)
        coluna = random.randint(0,9)
        campoComputador[linha][coluna], campoComputador[linha + 1][coluna], campoComputador[linha + 2][coluna], campoComputador[linha + 3][coluna] = '\033[0;30;41m0\033[m', '\033[0;30;41m0\033[m', '\033[0;30;41m0\033[m', '\033[0;30;41m0\033[m' # numero 0 vermelho

def gerar2NavioMComputador():
    for i in range(2):
        orientacao = random.randint(1,2) # '1' para navio 3x1 e '2' para navio 1x3
        if orientacao == 1:
            linha = random.randint(0,9)
            coluna = random.randint(0,7)
            while campoComputador[linha][coluna] == '\033[0;30;41m0\033[m' or campoComputador[linha][coluna + 1] == '\033[0;30;41m0\033[m' or campoComputador[linha][coluna + 2] == '\033[0;30;41m0\033[m':
                linha = random.randint(0,9)
                coluna = random.randint(0,7)
            campoComputador[linha][coluna], campoComputador[linha][coluna + 1], campoComputador[linha][coluna + 2] = '\033[0;30;41m0\033[m', '\033[0;30;41m0\033[m', '\033[0;30;41m0\033[m' # numero 0 vermelho
        elif orientacao == 2:
            linha = random.randint(0,7)
            coluna = random.randint(0,9)
            while campoComputador[linha][coluna] == '\033[0;30;41m0\033[m' or campoComputador[linha + 1][coluna] == '\033[0;30;41m0\033[m' or campoComputador[linha + 2][coluna] == '\033[0;30;41m0\033[m':
                linha = random.randint(0,7)
                coluna = random.randint(0,9)
            campoComputador[linha][coluna], campoComputador[linha + 1][coluna], campoComputador[linha + 2][coluna] = '\033[0;30;41m0\033[m', '\033[0;30;41m0\033[m', '\033[0;30;41m0\033[m' # numero 0 vermelho

def gerar3NavioPComputador():
    for i in range(3):
        orientacao = random.randint(1,2) # '1' para navio 2x1 e '2' para navio 1x2
        if orientacao == 1:
            linha = random.randint(0,9)
            coluna = random.randint(0,8)
            while campoComputador[linha][coluna] == '\033[0;30;41m0\033[m' or campoComputador[linha][coluna + 1] == '\033[0;30;41m0\033[m':
                linha = random.randint(0,9)
                coluna = random.randint(0,8)
            campoComputador[linha][coluna], campoComputador[linha][coluna + 1] = '\033[0;30;41m0\033[m', '\033[0;30;41m0\033[m' # numero 0 vermelho
        elif orientacao == 2:
            linha = random.randint(0,8)
            coluna = random.randint(0,9)
            while campoComputador[linha][coluna] == '\033[0;30;41m0\033[m' or campoComputador[linha + 1][coluna] == '\033[0;30;41m0\033[m':
                linha = random.randint(0,8)
                coluna = random.randint(0,9)
            campoComputador[linha][coluna], campoComputador[linha + 1][coluna] = '\033[0;30;41m0\033[m', '\033[0;30;41m0\033[m' # numero 0 vermelho

contCaseNavioAbatidoJogador = int(0)
# Função para o jogador atirar 
def atirarPC():
    print('Vez do PC jogar')
    linha = random.randint(0,9)
    coluna = random.randint(0,9)
    while campoJogador[linha][coluna] == '\033[0;30;44m0\033[m' or campoJogador[linha][coluna] == '\033[0;30;42m0\033[m': # cores que de localizações que ja foram atingidas
        linha = random.randint(0,9)
        coluna = random.randint(0,9)
    while campoJogador[linha][coluna] == '\033[0;30;41m0\033[m': # localização onde tem navio que não foi atingido
        campoJogador[linha][coluna] = '\033[0;30;42m0\033[m' # transforma em localização com navio ja atingido
        global contCaseNavioAbatidoJogador
        contCaseNavioAbatidoJogador += 1
        print(' O PC acertou um navio do seu tabuleiro! Ele jogará novamente')
        linha = random.randint(0,9)
        coluna = random.randint(0,9)
        while campoJogador[linha][coluna] == '\033[0;30;44m0\033[m' or campoJogador[linha][coluna] == '\033[0;30;42m0\033[m':
            linha = random.randint(0,9)
            coluna = random.randint(0,9)
    if campoJogador[linha][coluna] == '0': # localização onde tem agua
        campoJogador[linha][coluna] = '\033[0;30;44m0\033[m' #  transforma em localização com agua ja atingida
        print('O PC acertou a agua e agora vai ser sua vez de jogar')
        print('Seu tabuleiro ficou assim após a jogada do PC')
        tabuleiro(campoJogador)

def atirarJogador():
    print('Sua vez de jogar')
    a = 'escolha em que linha seu você vai atirar entre 1 e 10'
    linha = tratamentoValueError(1,10,a)
    b = 'escolha em que coluna seu você vai atirar entre 1 e 10'
    coluna = tratamentoValueError(1,10,b)
    while campoComputador[linha - 1][coluna - 1] == '\033[0;30;44m0\033[m' or campoComputador[linha - 1][coluna - 1] == '\033[0;30;42m0\033[m': # cores que de localizações que ja foram atingidas
        print('você ja atirou nesses lugares')
        a = 'escolha em que linha seu você vai atirar entre 1 e 10'
        linha = tratamentoValueError(1,10,a)
        b = 'escolha em que coluna seu você vai atirar entre 1 e 10'
        coluna = tratamentoValueError(1,10,b)
    while campoComputador[linha - 1][coluna - 1] == '\033[0;30;41m0\033[m': # localização onde tem navio que não foi atingido
        campoComputador[linha - 1][coluna - 1] = '\033[0;30;42m0\033[m' # transforma em localização com navio ja atingido
        campoComputadorExibido[linha - 1][coluna - 1] = '\033[0;30;42m0\033[m' # tranforma a localização do tabuleiro que será mostrado na cor de navio atingido
        global contCaseNavioAbatidoPC
        contCaseNavioAbatidoPC += 1
        print('Você acertou acertou uma localização de navio do tabuleiro inimigo! Você jogará novamente')
        a = 'escolha em que linha seu você vai atirar entre 1 e 10'
        linha = tratamentoValueError(1,10,a)
        b = 'escolha em que coluna seu você vai atirar entre 1 e 10'
        coluna = tratamentoValueError(1,10,b)
        while campoComputador[linha - 1][coluna - 1] == '\033[0;30;44m0\033[m' or campoComputador[linha - 1][coluna - 1] == '\033[0;30;42m0\033[m': # cores que de localizações que ja foram atingidas
            print('você ja atirou nesses lugares')
            a = 'escolha em que linha seu você vai atirar entre 1 e 10'
            linha = tratamentoValueError(1,10,a)
            b = 'escolha em que coluna seu você vai atirar entre 1 e 10'
            coluna = tratamentoValueError(1,10,b)
    if campoComputador[linha - 1][coluna - 1] == '0': # localização onde tem agua
        campoComputador[linha - 1][coluna - 1] = '\033[0;30;44m0\033[m' #  transforma em localização em com agua ja atingida
        campoComputadorExibido[linha - 1][coluna - 1] = '\033[0;30;44m0\033[m'# tranforma a localização do tabuleiro que será mostrado na cor de agua atingida
        print('você acertou a agua e agora vai ser vez do PC jogar')
        print('O tabuleiro do PC ficou assim')
        tabuleiro(campoComputadorExibido)

vezJogador = 0
contadorLoop = 1
while True:
    print('Bem vindo a Batalha Naval SENAs')
    # Gerando navios do tabuleiro do PC
    gerarNavioGComputador()
    gerar2NavioMComputador()
    gerar3NavioPComputador()
    print('Este é o tabuleiro do PC onde você deverá tentar destruir todos os navios')
    print('Porem seja inteligente ou o PC irá lhe derrotar')
    # Gerando navios no tabuleiro do jogador
    gerarNavioGJogador()
    gerar2NavioMJogador()
    gerar3NavioPJogador()
    print('A cada localização de navio atingido seu score aumenta em 1 unidade, ao chegar a 16 nós ja teremos um vitorioso')
    print('Placar:')
    print('User 1:|%d|  PC:|%d|' % (contCaseNavioAbatidoPC, contCaseNavioAbatidoJogador))
    while vezJogador >= 0:
        atirarPC()
        atirarJogador()
        print('Placar:')
        print('User 1:|%d|  PC:|%d|' % (contCaseNavioAbatidoPC, contCaseNavioAbatidoJogador))
        if contCaseNavioAbatidoJogador == int(16):
            print('O computador ganhou')
        elif contCaseNavioAbatidoPC == int(16):
            print('Você ganhou')
        print('Placar:')
        print('User 1:|%d|  PC:|%d|' % (contCaseNavioAbatidoPC, contCaseNavioAbatidoJogador))










