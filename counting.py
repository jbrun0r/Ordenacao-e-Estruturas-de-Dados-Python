## João Bruno Rodrigues de Freitas
import numpy as np ## Para facilitar a maanipulação de Arrays
import time ## Para contar o tempo 
import matplotlib.pyplot as plt ## Para gerar o grafico
import random 
##import sys

##sys.setrecursionlimit(50000000)


print('Ordenando...')


## 1000

um = np.arange(10000) ## Ordenado
## Ordenado
o1 = time.time()
um = np.repeat(np.arange(1+um.max()), np.bincount(um))
fo1 = time.time()
to1 = fo1 - o1
## Invertido
ium = um[::-1] ## Inversão
i1 = time.time()
ium = np.repeat(np.arange(1+ium.max()), np.bincount(ium))
f1 = time.time()
t1 = f1 - i1
## Aleatorio
random.shuffle(um) ## Aleatorio
a1 = time.time()
um = np.repeat(np.arange(1+um.max()), np.bincount(um))
fa1 = time.time()
ta1 = fa1 - a1

## 2000

dois = np.arange(20000) ## Ordenado
## Ordenado
o2 = time.time()
dois = np.repeat(np.arange(1+dois.max()), np.bincount(dois))
fo2 = time.time()
to2 = fo2 - o2
## Invertido
idois = dois[::-1] ## Inversão
i2 = time.time()
idois = np.repeat(np.arange(1+idois.max()), np.bincount(idois))
f2 = time.time()
t2 = f2 - i2
## Aleatorio
random.shuffle(dois) ## Aleatorio
a2 = time.time()
dois = np.repeat(np.arange(1+dois.max()), np.bincount(dois))
fa2 = time.time()
ta2 = fa2 - a2

## 3000

tres = np.arange(30000) ## Ordenado
## Ordenado
o3 = time.time()
tres = np.repeat(np.arange(1+tres.max()), np.bincount(tres))
fo3 = time.time()
to3 = fo3 - o3
## Invertido
itres = tres[::-1] ## Inversão
i3 = time.time()
itres = np.repeat(np.arange(1+itres.max()), np.bincount(itres))
f3 = time.time()
t3 = f3 - i3
## Aleatorio
random.shuffle(tres) ## Aleatorio
a3 = time.time()
tres = np.repeat(np.arange(1+tres.max()), np.bincount(tres))
fa3 = time.time()
ta3 = fa3 - a3

## 4000

quatro = np.arange(40000) ## Ordenado
## Ordenado
o4 = time.time()
quatro = np.repeat(np.arange(1+quatro.max()), np.bincount(quatro))
fo4 = time.time()
to4 = fo4 - o4
## Invertido
iquatro = quatro[::-1] ## Inversão
i4 = time.time()
iquatro = np.repeat(np.arange(1+iquatro.max()), np.bincount(iquatro))
f4 = time.time()
t4 = f4 - i4
## Aleatorio
random.shuffle(quatro) ## Aleatorio
a4 = time.time()
quatro = np.repeat(np.arange(1+quatro.max()), np.bincount(quatro))
fa4 = time.time()
ta4 = fa4 - a4

## 50000

cinco = np.arange(50000) ## Ordenado
## Ordenado
o5 = time.time()
cinco = np.repeat(np.arange(1+cinco.max()), np.bincount(cinco))
fo5 = time.time()
to5 = fo5 - o5
## Invertido
icinco = cinco[::-1] ## Inversão
i5 = time.time()
icinco = np.repeat(np.arange(1+icinco.max()), np.bincount(icinco))
f5 = time.time()
t5 = f5 - i5
## Aleatorio
random.shuffle(cinco) ## Aleatorio
a5 = time.time()
cinco = np.repeat(np.arange(1+cinco.max()), np.bincount(cinco))
fa5 = time.time()
ta5 = fa5 - a5

## 80000

oito = np.arange(80000) ## Ordenado
## Ordenado
o8 = time.time()
oito = np.repeat(np.arange(1+oito.max()), np.bincount(oito))
fo8 = time.time()
to8 = fo8 - o8
## Invertido
ioito = oito[::-1] ## Inversão
i8 = time.time()
ioito = np.repeat(np.arange(1+ioito.max()), np.bincount(ioito))
f8 = time.time()
t8 = f8 - i8
## Aleatorio
random.shuffle(oito) ## Aleatorio
a8 = time.time()
oito = np.repeat(np.arange(1+oito.max()), np.bincount(oito))
fa8 = time.time()
ta8 = fa8 - a8

## 110000

onze = np.arange(110000) ## Ordenado
## Ordenado
o11 = time.time()
onze = np.repeat(np.arange(1+onze.max()), np.bincount(onze))
fo11 = time.time()
to11 = fo11 - o11
## Invertido
ionze = onze[::-1] ## Inversão
i11 = time.time()
ionze = np.repeat(np.arange(1+ionze.max()), np.bincount(ionze)) 
f11 = time.time()
t11 = f11 - i11
## Aleatorio
random.shuffle(onze) ## Aleatorio
a11 = time.time()
onze = np.repeat(np.arange(1+onze.max()), np.bincount(onze))
fa11 = time.time()
ta11 = fa11 - a11

## 150000

quinze = np.arange(150000) ## Ordenado
# Ordenado
o15 = time.time()
quinze = np.repeat(np.arange(1+quinze.max()), np.bincount(quinze))
fo15 = time.time()
to15 = fo15 - o15
## Invertido

iquinze = quinze[::-1] ## Inversão
i15 = time.time()
iquinze = np.repeat(np.arange(1+iquinze.max()), np.bincount(iquinze))
f15 = time.time()
t15 = f15 - i15
## Aleatorio
random.shuffle(quinze) ## Aleatorio
a15 = time.time()
quinze = np.repeat(np.arange(1+quinze.max()), np.bincount(quinze))
f15 = time.time()
ta15 = f15 - a15

print('Concluído!')

## Atribuindo o eixo x e y do gráfico
x = ['10000', '20000', '30000', '40000', '50000', '80000', '110000', '150000'] ## tamanhos
y = [t1, t2, t3, t4, t5, t8, t11, t15]  
a = [ta1, ta2, ta3, ta4, ta5, ta8, ta11, ta15]
o = [to1, to2, to3, to4, to5, to8, to11, to15]

## Criação do Gráfico 
plt.plot(x, y,color='green')
plt.plot(x, a,color='blue')
plt.plot(x, o,color='red')
plt.legend(['Red = Ordenado', 'Green = Invertido', 'Blue = Aleatório'], loc=2)
plt.title('COUNTING SORT\n')
plt.xlabel('Tamanho')
plt.ylabel('Tempo(s)')
plt.show() ## Mostrar Grafico
