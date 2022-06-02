## JOÃO BRUNO RODRIGUES DE FREITAS
import numpy as np ## Para facilitar a maanipulação de Arrays
import time ## Para contar o tempo 
import matplotlib.pyplot as plt ## Para gerar o grafico
import random 
import sys 

##sys.setrecursionlimit(550000000) ## Aumentando o tamanho da recursão disponivel

def counting_sort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calcule a contagem de elementos
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calcular a contagem cumulativa
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Coloque os elementos em ordem de classificação
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Função principal para implementar classificação
def radiz_sort(array):
    # Pegar o maxmimo de elementos
    max_element = max(array)

    # Aplicar classificação de contagem para classificar os elementos com base no valor do lugar
    place = 1
    while max_element // place > 0:
        counting_sort(array, place)
        place *= 10



print('\n=== Radix Sort ====')


## Criação dos arrays com seguintes tamanhos [1000,2000,3000,4000,5000,8000,100000]: 
## Chamada da Função Radix sort, calculo do tempo de exercução e imprimir: 


## 10000

um = np.arange(10000) ## Ordenado
print('Ordenações de 10000 tamanho...')
## Ordenado
o1 = time.time()
radiz_sort(um) 
fo1 = time.time()
to1 = fo1 - o1
## Invertido
ium = um[::-1] ## Inversão
i1 = time.time()
radiz_sort(ium) 
f1 = time.time()
t1 = f1 - i1
## Aleatorio
random.shuffle(um) ## Aleatorio
a1 = time.time()
radiz_sort(um)
fa1 = time.time()
ta1 = fa1 - a1

## 20000

dois = np.arange(20000) ## Ordenado
print('Ordenações de 20000 tamanho...')
## Ordenado
o2 = time.time()
radiz_sort(dois) 
fo2 = time.time()
to2 = fo2 - o2
## Invertido
idois = dois[::-1] ## Inversão
i2 = time.time()
radiz_sort(idois) 
f2 = time.time()
t2 = f2 - i2
## Aleatorio
random.shuffle(dois) ## Aleatorio
a2 = time.time()
radiz_sort(dois)
fa2 = time.time()
ta2 = fa2 - a2

## 30000

tres = np.arange(30000) ## Ordenado
print('Ordenações de 30000 tamanho...')
## Ordenado
o3 = time.time()
radiz_sort(tres) 
fo3 = time.time()
to3 = fo3 - o3
## Invertido
itres = tres[::-1] ## Inversão
i3 = time.time()
radiz_sort(itres) 
f3 = time.time()
t3 = f3 - i3
## Aleatorio
random.shuffle(tres) ## Aleatorio
a3 = time.time()
radiz_sort(tres)
fa3 = time.time()
ta3 = fa3 - a3

## 40000

quatro = np.arange(40000) ## Ordenado
print('Ordenações de 40000 tamanho...')
## Ordenado
o4 = time.time()
radiz_sort(quatro) 
fo4 = time.time()
to4 = fo4 - o4
## Invertido
iquatro = quatro[::-1] ## Inversão
i4 = time.time()
radiz_sort(iquatro) 
f4 = time.time()
t4 = f4 - i4
## Aleatorio
random.shuffle(quatro) ## Aleatorio
a4 = time.time()
radiz_sort(quatro)
fa4 = time.time()
ta4 = fa4 - a4

## 50000

cinco = np.arange(50000) ## Ordenado
print('Ordenações de 50000 tamanho...')
## Ordenado
o5 = time.time()
radiz_sort(cinco) 
fo5 = time.time()
to5 = fo5 - o5
## Invertido
icinco = cinco[::-1] ## Inversão
i5 = time.time()
radiz_sort(icinco) 
f5 = time.time()
t5 = f5 - i5
## Aleatorio
random.shuffle(cinco) ## Aleatorio
a5 = time.time()
radiz_sort(cinco)
fa5 = time.time()
ta5 = fa5 - a5

## 80000

oito = np.arange(80000) ## Ordenado
print('Ordenações de 80000 tamanho...')
## Ordenado
o8 = time.time()
radiz_sort(oito) 
fo8 = time.time()
to8 = fo8 - o8
## Invertido
ioito = oito[::-1] ## Inversão
i8 = time.time()
radiz_sort(ioito) 
f8 = time.time()
t8 = f8 - i8
## Aleatorio
random.shuffle(oito) ## Aleatorio
a8 = time.time()
radiz_sort(oito)
fa8 = time.time()
ta8 = fa8 - a8

## 100000

onze = np.arange(100000) ## Ordenado
print('Ordenações de 100000 tamanho...')
## Ordenado
o11 = time.time()
radiz_sort(onze) 
fo11 = time.time()
to11 = fo11 - o11
## Invertido
ionze = onze[::-1] ## Inversão
i11 = time.time()
radiz_sort(ionze) 
f11 = time.time()
t11 = f11 - i11
## Aleatorio
random.shuffle(onze) ## Aleatorio
a11 = time.time()
radiz_sort(onze)
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
plt.title('Bucket Sort - Tempo de ordenamento X Tamanho')
plt.legend(['Red = Ordenado', 'Green = Invertido', 'Blue = Aleatório - PIOR CASO'], loc=2)
plt.xlabel('Tamanho')
plt.ylabel('Tempo(s)')
plt.show() ## Mostrar Grafico
