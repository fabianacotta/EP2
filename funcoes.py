import random
def rolar_dados (numero_dados):
  sorteados = [] 
  i = 0 
  while i < numero_dados:
    valor = random.randint(1,6)
    sorteados.append(valor)
    i+=1
  return sorteados 
    
