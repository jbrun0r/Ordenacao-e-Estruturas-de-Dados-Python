## JOÃO BRUNO RODRIGUES DE FREITAS
import numpy as np ## Para facilitar a maanipulação de Arrays
import time ## Para contar o tempo 
import matplotlib.pyplot as plt ## Para gerar o grafico
import random 
import sys 

##sys.setrecursionlimit(550000000) ## Aumentando o tamanho da recursão disponivel

## função Shell Sort

def shell_short(v):
  
  h = len(v) // 2 #distancia
  while h > 0:

    i = h
    while i < len(v):
      temp = v[i]
      trocou =  False
      j = i - h
      while j >= 0 and v[j] > temp:
        v[j+h] = v[j]
        trocou = True
        j -= h 

      if trocou:
        v[j+h] = temp

      i += 1    

    h = h // 2



print('\n=== Shell Sort ====')


## Criação dos arrays com seguintes tamanhos [1000,2000,3000,4000,5000,8000,11000,15000]: 
## Chamada da Função Buble sort, calculo do tempo de exercução e imprimir: 


## 10000

um = np.arange(10000) ## Ordenado
print('Ordenações de 10000 tamanho...')
## Ordenado
o1 = time.time()
shell_short(um) 
fo1 = time.time()
to1 = fo1 - o1
## Invertido
ium = um[::-1] ## Inversão
i1 = time.time()
shell_short(ium) 
f1 = time.time()
t1 = f1 - i1
## Aleatorio
random.shuffle(um) ## Aleatorio
a1 = time.time()
shell_short(um)
fa1 = time.time()
ta1 = fa1 - a1

## 20000

dois = np.arange(20000) ## Ordenado
print('Ordenações de 20000 tamanho...')
## Ordenado
o2 = time.time()
shell_short(dois) 
fo2 = time.time()
to2 = fo2 - o2
## Invertido
idois = dois[::-1] ## Inversão
i2 = time.time()
shell_short(idois) 
f2 = time.time()
t2 = f2 - i2
## Aleatorio
random.shuffle(dois) ## Aleatorio
a2 = time.time()
shell_short(dois)
fa2 = time.time()
ta2 = fa2 - a2

## 30000

tres = np.arange(30000) ## Ordenado
print('Ordenações de 30000 tamanho...')
## Ordenado
o3 = time.time()
shell_short(tres) 
fo3 = time.time()
to3 = fo3 - o3
## Invertido
itres = tres[::-1] ## Inversão
i3 = time.time()
shell_short(itres) 
f3 = time.time()
t3 = f3 - i3
## Aleatorio
random.shuffle(tres) ## Aleatorio
a3 = time.time()
shell_short(tres)
fa3 = time.time()
ta3 = fa3 - a3

## 40000

quatro = np.arange(40000) ## Ordenado
print('Ordenações de 40000 tamanho...')
## Ordenado
o4 = time.time()
shell_short(quatro) 
fo4 = time.time()
to4 = fo4 - o4
## Invertido
iquatro = quatro[::-1] ## Inversão
i4 = time.time()
shell_short(iquatro) 
f4 = time.time()
t4 = f4 - i4
## Aleatorio
random.shuffle(quatro) ## Aleatorio
a4 = time.time()
shell_short(quatro)
fa4 = time.time()
ta4 = fa4 - a4

## 50000

cinco = np.arange(50000) ## Ordenado
print('Ordenações de 50000 tamanho...')
## Ordenado
o5 = time.time()
shell_short(cinco) 
fo5 = time.time()
to5 = fo5 - o5
## Invertido
icinco = cinco[::-1] ## Inversão
i5 = time.time()
shell_short(icinco) 
f5 = time.time()
t5 = f5 - i5
## Aleatorio
random.shuffle(cinco) ## Aleatorio
a5 = time.time()
shell_short(cinco)
fa5 = time.time()
ta5 = fa5 - a5

## 80000

oito = np.arange(80000) ## Ordenado
print('Ordenações de 80000 tamanho...')
## Ordenado
o8 = time.time()
shell_short(oito) 
fo8 = time.time()
to8 = fo8 - o8
## Invertido
ioito = oito[::-1] ## Inversão
i8 = time.time()
shell_short(ioito) 
f8 = time.time()
t8 = f8 - i8
## Aleatorio
random.shuffle(oito) ## Aleatorio
a8 = time.time()
shell_short(oito)
fa8 = time.time()
ta8 = fa8 - a8

## 100000

onze = np.arange(100000) ## Ordenado
print('Ordenações de 100000 tamanho...')
## Ordenado
o11 = time.time()
shell_short(onze) 
fo11 = time.time()
to11 = fo11 - o11
## Invertido
ionze = onze[::-1] ## Inversão
i11 = time.time()
shell_short(ionze) 
f11 = time.time()
t11 = f11 - i11
## Aleatorio
random.shuffle(onze) ## Aleatorio
a11 = time.time()
shell_short(onze)
fa11 = time.time()
ta11 = fa11 - a11



## Atribuindo o eixo x e y do gráfico
x = ['10000', '20000', '30000', '40000', '50000', '80000', '100000'] ## tamanhos
y = [t1, t2, t3, t4, t5, t8, t11]  
a = [ta1, ta2, ta3, ta4, ta5, ta8, ta11]
o = [to1, to2, to3, to4, to5, to8, to11]

## Criação do Gráfico 
plt.plot(x, y,color='green')
plt.plot(x, a,color='blue')
plt.plot(x, o,color='red')
plt.title('Shell Sort - Tempo de ordenamento X Tamanho')
plt.legend(['Red = Ordenado', 'Green = Invertido', 'Blue = Aleatório'], loc=2)
plt.xlabel('Tamanho')
plt.ylabel('Tempo(s)')
plt.show() ## Mostrar Grafico
