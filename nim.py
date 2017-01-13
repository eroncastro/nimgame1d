def computador_escolhe_jogada(n, m):
    for i in range(m):
        if (n - (i + 1)) % (m + 1) == 0:
            print('O computador retirou %s peça(s).' % (i + 1))
            if (n - (i + 1)) > 0:
                print('Agora restam %s peças no tabuleiro.' % (n - (i + 1)))
            else:
                print('Fim do jogo! O computador ganhou!')
            return i + 1

def usuario_escolhe_jogada(n, m):
    while True:
        jogadas_usuario = int(input('Quantas peças você vai tirar? '))
        if jogadas_usuario > m:
            print('Numero inválido de jogadas')
        if n - jogadas_usuario > 0:
            print('Você tirou %s peça(s)' % jogadas_usuario)
        else:
            print('Fim do jogo! Você ganhou!')
        return jogadas_usuario

def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    if (n % (m + 1)) != 0:
        print('Computador começa!')
        n = n - computador_escolhe_jogada(n, m)
    else:
        print('Você começa')

    while n > 0:
        n = n - usuario_escolhe_jogada(n, m)
        if n == 0:
            break

        n = n - computador_escolhe_jogada(n, m)
        if n == 0:
            break

print('Bem-vindo ao jogo do NIM! Escolha:')
print('1 - para jogar uma partida isolada')
print('2 - para jogar um campeonato')
game_type = int(input())

matches = 3 if game_type == 2 else 1

while matches > 0:
    partida()
    matches = matches - 1

print('**** Final do campeonato! ****')
