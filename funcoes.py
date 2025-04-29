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