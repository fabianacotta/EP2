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

  j=0
  ordem = []

  while j+1 < len(lista):
    if lista[j] < lista[j+1]:
      ordem.append(lista[j])
      j+=1
      
  if ordem[0] == 1 and ordem[1]== 2 and ordem[2]== 3 and ordem[3]== 4:
    return 15
  if ordem[0] == 2 and ordem[1]== 3 and ordem[2]== 4 and ordem[3]== 5:
    return 15
  if ordem[0] == 3 and ordem[1]== 4 and ordem[2]== 5 and ordem[3]== 6:
    return 15
  else: 
    return 0 

    