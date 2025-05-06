# 12 rodadas
# Rodada comeca: jogar 5 dados
# Rodada termina: preencher cartela com valores
# Só pode preencher cada linha uma vez (cada jogador a sua)
# Fim do jogo: jogador preenche todas as linhas 

# Oq jogador pode fazer na rodada:
#  1: guardar dado
#  2: remover dado
#  3: rolar novamente dados (so rolam os q n estao guardados),(so pode ser feito 2x por rodada)
#  4: verificar cartela (chamar imprime_cartela)
#  5: fazer a jogada
#  *: se escolher opcao inválida: opcao invalida, tente novamente 

import random 

from funcoes import *

i = 0 
while i < 12:
    faces = rolar_dados(5)
    cartela = imprime_cartela(cartela)
    guardar = []

    print(f"Cartela de Pontos: {cartela}")
    print(f"Dados rolados: {faces}")
    print("Dados guardados: []")
    
    opcoes = ("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    if opcoes != 1 or opcoes != 2 or opcoes != 3 or opcoes != 4 or opcoes != 0:
        print("Opção inválida. Tente novamente.")

    if opcoes == 1:
        indice = input("Digite o índice do dado a ser guardado (0 a 4):")
        guardados = guardar_dado(faces, guardar, indice)
        print(f"Dados rolados: {faces}")
        print(f"Dados guardados: {guardados}")
    
    if opcoes == 2:
        indice = input("Digite o índice do dado a ser removido (0 a 4):")
        removido = remover_dado(faces, guardados, indice)
        print(f"Dados rolados: {faces}")
        print(f"Dados guardados: {guardados}")

    j=0
    if opcoes ==3:
        j +=1
        if j < 3:
            if opcoes == 3:
                faces = rolar_dados(5)
                print(f"Dados rolados: {faces}")
                print(f"Dados guardados: {guardados}")
        else:
            print ("Você já usou todas as rerrolagens.")
    
    if opcoes == 4:
        cartela= imprime_cartela(cartela)
        print(f"Cartela de Pontos: {cartela}")
    
    if opcoes == 0:
        categoria = ("Digite a combinação desejada:")
        jogada = faz_jogada(faces, categoria, cartela)
        print(f"Dados rolados: {faces}")
        print(f"Dados guardados: {guardados}")

    i+=1

pontos = 0

for k in cartela:
    for x in cartela[k]:
        pontos += cartela[k][x]

if pontos >= 63:
    pontos += 35

print(cartela)
print(f"Pontuação total: {pontos}")

