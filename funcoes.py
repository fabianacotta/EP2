import random
def rolar_dados (numero_dados):
  sorteados = [] 
  i = 0 
  while i < numero_dados:
    valor = random.randint(1,6)
    sorteados.append(valor)
    i+=1
  return sorteados 

def guardar_dado (rolados, guardados, indice):
  lista = []
  
  guardados.append(rolados[indice])

  del(rolados[indice])

  lista.append(rolados)
  lista.append(guardados)
  
  return lista

def remover_dado (rolados, guardados, indice):
  lista = []
  rolados.append(guardados[indice])

  del(guardados[indice])

  lista.append(rolados)
  lista.append(guardados)
  
  return lista

def calcula_pontos_regra_simples (faces):
  dicio = {}
  i = 0 

  while i < len(faces):
    if faces[i]== 6 or faces[i]== 1:
      dicio[faces[i]]=0
    
    if faces[i]==2:
      dicio[faces[i]]=4
    
    if faces[i]==3:
      dicio[faces[i]]=3

    if faces[i]==4:
      dicio[faces[i]]=4

    if faces[i]==5:
      dicio[faces[i]]=5
    
    i+=1

  return dicio

#ex5