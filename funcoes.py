import random

#Q1
def rolar_dados (numero_dados):
  sorteados = [] 
  i = 0 
  while i < numero_dados:
    valor = random.randint(1,6)
    sorteados.append(valor)
    i+=1
  return sorteados 

#Q2
def guardar_dado (rolados, guardados, indice):
  lista = []
  
  guardados.append(rolados[indice])

  del(rolados[indice])

  lista.append(rolados)
  lista.append(guardados)
  
  return lista

#Q3
def remover_dado (rolados, guardados, indice):
  lista = []
  rolados.append(guardados[indice])

  del(guardados[indice])

  lista.append(rolados)
  lista.append(guardados)
  
  return lista

#Q4
def calcula_pontos_regra_simples (faces):

  dicio = {}

  i = 0 
  pontos1 = 0 
  pontos2 = 0
  pontos3 = 0
  pontos4 = 0
  pontos5 = 0
  pontos6 = 0

  while i < len(faces):
    if faces[i]== 1:
      pontos1 += 1 
    
    if faces[i]==2:
      pontos2 += 2
    
    if faces[i]==3:
      pontos3 += 3

    if faces[i]==4:
      pontos4 += 4

    if faces[i]==5:
      pontos5 += 5

    if faces[i]==6:
      pontos6 += 6

    i+=1

  dicio[1] = pontos1
  dicio[2] = pontos2
  dicio[3] = pontos3
  dicio[4] = pontos4
  dicio[5] = pontos5
  dicio[6] = pontos6

  return dicio

#Q5
def calcula_pontos_soma (faces):
  soma = 0 
  i = 0 
  while i < len(faces):
    soma += faces[i]
    i+=1
  return soma 

#Q6
def calcula_pontos_sequencia_baixa (faces):
  i = 0 
  lista = []
  
  while i < len(faces):
    if faces[i] not in lista:
      lista.append(faces[i])
    i+=1

  
  if 1 in lista and 2 in lista and 3 in lista and 4 in lista:
    return 15
  
  if 2 in lista and 3 in lista and 4 in lista and 5 in lista:
    return 15
  
  if 3 in lista and 4 in lista and 5 in lista and 6 in lista:
    return 15
  
  else:
    return 0 

#Q7 
def calcula_pontos_sequencia_alta (faces):
  i = 0 
  lista = []
  
  while i < len(faces):
    if faces[i] not in lista:
      lista.append(faces[i])
    i+=1

  
  if 1 in lista and 2 in lista and 3 in lista and 4 in lista and 5 in lista:
    return 30
  
  if 2 in lista and 3 in lista and 4 in lista and 5 in lista and 6 in lista:
    return 30
  
  else:
    return 0 
  
#Q8
def calcula_pontos_full_house (faces):
  i = 0
  qtd_3 = []
  qtd_2 = []
  outros = []
  soma = 0 

  while i < len(faces):

    if qtd_3 == []: 
      qtd_3.append(faces[i])
    else:
      if faces[i] in qtd_3:
        qtd_3.append(faces[i])

    if faces[i] not in qtd_3:
        if qtd_2 == []:
          qtd_2.append(faces[i])
        else:
          if faces[i] in qtd_2:
            qtd_2.append(faces[i])
        
          else: 
            outros.append(faces[i])
    
    i+=1

  j = 0 

  if len(outros) > 0:
    return 0 
  
  if len(qtd_3) > 3:
    return 0
  
  if len(qtd_2) > 3:
    return 0
  
  else:
    while j < len(faces):
      soma += faces[j]
      j+=1
    return soma
  
#Q9
def calcula_pontos_quadra (faces):
  i = 0 
  j = 0
  soma = 0 
  ig_1 = 0
  ig_2 = 0 
  ig_3 = 0 
  ig_4 = 0 
  ig_5 = 0
  ig_6 = 0

  while i < len(faces):
    if faces[i] == 1:
      ig_1+=1
    if faces[i] == 2:
      ig_2+=1
    if faces[i] == 3:
      ig_3+=1
    if faces[i] == 4:
      ig_4+=1
    if faces[i] == 5:
      ig_5+=1
    if faces[i] == 6:
      ig_6+=1
    i+=1

  if ig_1 >= 4 or ig_2 >= 4 or ig_3 >= 4 or ig_4 >= 4 or ig_5 >= 4 or ig_6 >= 4:
    while j < len(faces):
      soma += faces[j]
      j+=1
    return soma
  else:
    return 0 
  
#Q10
def calcula_pontos_quina (faces):
  i = 0 

  ig_1 = 0
  ig_2 = 0 
  ig_3 = 0 
  ig_4 = 0 
  ig_5 = 0
  ig_6 = 0

  while i < len(faces):
    if faces[i] == 1:
      ig_1+=1
    if faces[i] == 2:
      ig_2+=1
    if faces[i] == 3:
      ig_3+=1
    if faces[i] == 4:
      ig_4+=1
    if faces[i] == 5:
      ig_5+=1
    if faces[i] == 6:
      ig_6+=1
    i+=1

  if ig_1 >= 5 or ig_2 >= 5 or ig_3 >= 5 or ig_4 >= 5 or ig_5 >= 5 or ig_6 >= 5:
    return 50
  else:
    return 0 
  
#Q11
def calcula_pontos_regra_avancada (faces):

  cinco = calcula_pontos_quina(faces)
  house = calcula_pontos_full_house(faces)
  quatro = calcula_pontos_quadra(faces)
  sem = calcula_pontos_soma(faces)
  alta = calcula_pontos_sequencia_alta(faces)
  baixa = calcula_pontos_sequencia_baixa(faces)

  dicio = {'cinco_iguais':cinco, 'full_house':house, 'quadra':quatro, 'sem_combinacao': sem,'sequencia_alta':alta, 'sequencia_baixa':baixa}
  
  return dicio

#Q12
def faz_jogada (faces, categoria, cartela):
  simples = calcula_pontos_regra_simples(faces)
  avancada = calcula_pontos_regra_avancada(faces)

  if categoria in avancada:
    pontos = avancada[categoria]
    cartela["regra_avancada"][categoria] = pontos
  else:
    pontos = simples[int(categoria)]
    cartela["regra_simples"][int(categoria)] = pontos

  return cartela 

#Q13
def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)

