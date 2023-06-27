
def computador_escolhe_jogada(n, m):
    computadorTira = 1
    while computadorTira != m:
        if((n - computadorTira)%(m+1)==0):
            return computadorTira
        else:
            computadorTira += 1

    return computadorTira




def usuario_escolhe_jogada(n,m):
    jogadaOK = False
    while not jogadaOK:
        jogaRemove = int(input("Quantas peças quer tirar ?"))
        if jogaRemove > m or jogaRemove < 1:
         print('\nOops! Jogada inválida! Tente de novo.\n')
        else:
            jogadaOK = True
    return jogaRemove



def partida():
 n = int(input("\nQuantas Peças? "))
 m = int(input("\nLimite de peças retiradas"))
 
 vezPc = False

 if n % (m+1) == 0:
     print("\n Voce Começa! ")
 else:
      print("\n PC Começa! ")
      vezPc = True

 while n > 0 :
     if vezPc == True :
         compRemove = computador_escolhe_jogada(n,m)
         n = n - compRemove
         if compRemove == 1:
             print("\nO computador removeu uma peça")
         else:
              print(f"\nO computador removeu {compRemove} peças")
         vezPc = False
     else:
         jogaRemove = usuario_escolhe_jogada(n,m)
         n = n - jogaRemove
         if jogaRemove== 1:
             print("\nJogador removeu uma peça")
         else:
              print(f"\nO Jogador removeu {jogaRemove} peças")
         vezPc = True    
     if n == 1:
        print('\nAgora resta apenas uma peça no tabuleiro.')
       
     else:
        if n != 0:
         print('\nAgora restam,', n, 'peças no tabuleiro.')
       
 print("Fim do jogo! O computador ganhou!")
          

def Campeonato():
    Turno = 1
    while Turno <= 3:
        print(f"\n****** Rodada {Turno} ********\n")
        partida()
        Turno += 1
    print(f"\n Placar: Voce 0 X 3 Computador")
        

print("Bem-vindo ao jogo do NIM! Escolha:")
escolha = 0
escolha = int(input("Escolha 1 para partida individual e 2 para campeonato!"))
if escolha == 1:
    partida()
elif escolha == 2:
    Campeonato()
else:
    print("Valor Invalido!!")

