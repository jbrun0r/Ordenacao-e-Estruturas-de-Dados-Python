## João Bruno Rodrigues de Freitas
import numpy as np ## Para facilitar a maanipulação de Arrays
import time ## Para contar o tempo 
import matplotlib.pyplot as plt ## Para gerar o grafico
import random 
import sys 

sys.setrecursionlimit(550000000) ## Aumentando o tamanho da recursão disponivel

## função Quick Sort

def quick_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    if inicio < fim:
        p = partir(lista, inicio, fim)
        quick_sort(lista, inicio, p-1)
        quick_sort(lista, p+1, fim)


def partir(lista, inicio, fim):
    pivo = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivo:
            lista[j], lista[i] = lista[i], lista[j]
            i=i+1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i



print('\n=== Quick Sort ====')


## Criação dos arrays com seguintes tamanhos [1000,2000,3000,4000,5000,8000,11000,15000]: 
## Chamada da Função Buble sort, calculo do tempo de exercução e imprimir: 


## 1000

um = np.arange(1000) ## Ordenado
print('Ordenações de 1000 tamanho...')
## Ordenado
o1 = time.time()
quick_sort(um) 
fo1 = time.time()
to1 = fo1 - o1
## Invertido
ium = um[::-1] ## Inversão
i1 = time.time()
quick_sort(ium) 
f1 = time.time()
t1 = f1 - i1
## Aleatorio
random.shuffle(um) ## Aleatorio
a1 = time.time()
quick_sort(um)
fa1 = time.time()
ta1 = fa1 - a1

## 2000

dois = np.arange(2000) ## Ordenado
print('Ordenações de 2000 tamanho...')
## Ordenado
o2 = time.time()
quick_sort(dois) 
fo2 = time.time()
to2 = fo2 - o2
## Invertido
idois = dois[::-1] ## Inversão
i2 = time.time()
quick_sort(idois) 
f2 = time.time()
t2 = f2 - i2
## Aleatorio
random.shuffle(dois) ## Aleatorio
a2 = time.time()
quick_sort(dois)
fa2 = time.time()
ta2 = fa2 - a2

## 3000

tres = np.arange(3000) ## Ordenado
print('Ordenações de 3000 tamanho...')
## Ordenado
o3 = time.time()
quick_sort(tres) 
fo3 = time.time()
to3 = fo3 - o3
## Invertido
itres = tres[::-1] ## Inversão
i3 = time.time()
quick_sort(itres) 
f3 = time.time()
t3 = f3 - i3
## Aleatorio
random.shuffle(tres) ## Aleatorio
a3 = time.time()
quick_sort(tres)
fa3 = time.time()
ta3 = fa3 - a3

## 4000

quatro = np.arange(4000) ## Ordenado
print('Ordenações de 4000 tamanho...')
## Ordenado
o4 = time.time()
quick_sort(quatro) 
fo4 = time.time()
to4 = fo4 - o4
## Invertido
iquatro = quatro[::-1] ## Inversão
i4 = time.time()
quick_sort(iquatro) 
f4 = time.time()
t4 = f4 - i4
## Aleatorio
random.shuffle(quatro) ## Aleatorio
a4 = time.time()
quick_sort(quatro)
fa4 = time.time()
ta4 = fa4 - a4

## 5000

cinco = np.arange(5000) ## Ordenado
print('Ordenações de 5000 tamanho...')
## Ordenado
o5 = time.time()
quick_sort(cinco) 
fo5 = time.time()
to5 = fo5 - o5
## Invertido
icinco = cinco[::-1] ## Inversão
i5 = time.time()
quick_sort(icinco) 
f5 = time.time()
t5 = f5 - i5
## Aleatorio
random.shuffle(cinco) ## Aleatorio
a5 = time.time()
quick_sort(cinco)
fa5 = time.time()
ta5 = fa5 - a5

## 8000

oito = np.arange(8000) ## Ordenado
print('Ordenações de 8000 tamanho...')
## Ordenado
o8 = time.time()
quick_sort(oito) 
fo8 = time.time()
to8 = fo8 - o8
## Invertido
ioito = oito[::-1] ## Inversão
i8 = time.time()
quick_sort(ioito) 
f8 = time.time()
t8 = f8 - i8
## Aleatorio
random.shuffle(oito) ## Aleatorio
a8 = time.time()
quick_sort(oito)
fa8 = time.time()
ta8 = fa8 - a8

## 11000

onze = np.arange(11000) ## Ordenado
print('Ordenações de 11000 tamanho...')
## Ordenado
o11 = time.time()
quick_sort(onze) 
fo11 = time.time()
to11 = fo11 - o11
## Invertido
ionze = onze[::-1] ## Inversão
i11 = time.time()
quick_sort(ionze) 
f11 = time.time()
t11 = f11 - i11
## Aleatorio
random.shuffle(onze) ## Aleatorio
a11 = time.time()
quick_sort(onze)
fa11 = time.time()
ta11 = fa11 - a11

## 15000

##quinze = np.arange(15000) ## Ordenado
print('NÃO AGUENTA ORDENAR A PARTIR DO TAMANHO DE 15MIL\n MATA O PROCESSO POR ERRO DE SEGMENTO')
# Ordenado
o15 = time.time()
#quick_sort(quinze) 
fo15 = time.time()
to15 = fo15 - o15
## Invertido
#iquinze = quinze[::-1] ## Inversão
i15 = time.time()
#quick_sort(iquinze) 
f15 = time.time()
t15 = f15 - i15
## Aleatorio
##random.shuffle(quinze) ## Aleatorio
a15 = time.time()
#quick_sort(quinze)
f15 = time.time()
ta15 = f15 - a15


## Atribuindo o eixo x e y do gráfico
x = ['1000', '2000', '3000', '4000', '5000', '8000', '11000'] ## tamanhos
y = [t1, t2, t3, t4, t5, t8, t11]  
a = [ta1, ta2, ta3, ta4, ta5, ta8, ta11]
o = [to1, to2, to3, to4, to5, to8, to11]

## Criação do Gráfico 
plt.plot(x, y,color='green')
plt.plot(x, a,color='blue')
plt.plot(x, o,color='red')
plt.title('Quick Sort - Tempo de ordenamento X Tamanho\nGreen-invertido\nBlue-Aleatório\nRed-Ordenado')
plt.xlabel('Tamanho')
plt.ylabel('Segundos')
plt.show() ## Mostrar Grafico
