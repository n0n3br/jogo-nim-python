def calcula_limite(n, m):
    return n if (m > n) else m

def nome_impressao(j):
    return 'O computador' if j == 'computador' else 'Você'

def imprime_pecas_retiradas(pecas, j):
    quatidade_pecas = "uma" if (pecas == 1) else pecas
    plural = "peça" if (pecas == 1) else "peças"
    print(nome_impressao(j), "tirou", quatidade_pecas, plural)

def imprime_pecas_restantes(pecas):
    quatidade_pecas = "uma" if (pecas == 1) else pecas
    resta = "resta" if (pecas == 1) else "restam"
    plural = "peça" if (pecas == 1) else "peças"
    print("Agora", resta, quatidade_pecas, plural,"no tabuleiro!")

def imprime_ganhador(j):
    print("Fim do jogo!",nome_impressao(j),"ganhou!")

def computador_escolhe_jogada(n, m):
    limite = calcula_limite(n, m)
    contador = 1
    pecas = 0
    while(contador <= limite and pecas == 0):
        if ((n -contador) % (m + 1) ==  0):
            pecas = contador
        contador+=1
    return pecas if (pecas > 0) else limite
    
def usuario_escolhe_jogada(n, m):
    limite = calcula_limite(n, m)
    pecas = 0
    while True:
        pecas = int(input("Quantas peças você vai tirar? "))
        if (pecas > 0 and pecas <= limite):
            break
        print("Oops! Jogada inválida! Tente de novo.")
    return pecas

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    j = 'jogador' if n % (m + 1) == 0 else 'computador'
    print()
    print('Computador começa!' if j == 'computador' else 'Você começa!')
    print()
    while True:
        if (j == 'computador'):
            pecas = computador_escolhe_jogada(n,m)
        else:

            pecas = usuario_escolhe_jogada(n, m)
        imprime_pecas_retiradas(pecas, j)
        n = n - pecas
        if (n == 0):
            break
        imprime_pecas_restantes(n)
        print()
        j = 'jogador' if j == 'computador' else 'computador'
    imprime_ganhador(j)
    return j

def campeonato():
    contador = 1
    partidas_computador = 0
    partidas_jogador = 0
    while(contador <= 3):
        print()
        print("**** Rodada",contador,"****")
        print()
        ganhador = partida()
        if ganhador == 'computador':
            partidas_computador += 1
        else:
            partidas_jogador += 1
        contador+=1
    print()
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você", partidas_jogador, "X",partidas_computador,"Computador")

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato 2")
    opcao = int(input())
    if (opcao == 1):
        partida()
    else:
        campeonato()

main()
