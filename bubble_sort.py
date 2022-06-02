## João Bruno Rodrigues de Freitas
import numpy as np ## Para facilitar a maanipulação de Arrays
import time ## Para contar o tempo 
import matplotlib.pyplot as plt ## Para gerar o grafico

## função bubble sort
def bubble_sort(objeto):
  tamanho = len(objeto) ## len() retorna o número de itens em um objeto
  for j in range(tamanho - 1):
    for indice in range(tamanho - 1):
      if objeto[indice] > objeto[indice + 1]: ##verificando se o atual é maior que o atual +1(o próximo)
        objeto[indice], objeto[indice + 1] = objeto[indice+1], objeto[indice] ##trocar as posições como se usasse uma VAR aux


print('\n=== bubble sort ====')


## Criação dos arrays com seguintes tamanhos [1000,2000,3000,4000,5000,8000,11000,15000]: 

um = np.arange(1000) ## tamanho 1000: de 0 a 999
um_pior = um[::-1]  ## inversão: 999 a 0

dois = np.arange(2000)
dois_pior = dois[::-1]

tres = np.arange(3000)
tres_pior = tres[::-1]

quatro = np.arange(4000)
quatro_pior = quatro[::-1]

cinco = np.arange(5000)
cinco_pior = cinco[::-1]

oito = np.arange(8000)
oito_pior = oito[::-1]

onze = np.arange(11000)
onze_pior = onze[::-1]

quinze = np.arange(15000)
quinze_pior = quinze[::-1]

# Chamada da Função Buble sort, calculo do tempo de exercução e imprimir: 

## 1000
print('\n1000 pior caso:\n',um_pior)
i_um = time.time()
bubble_sort(um_pior)
f_um = time.time()
t1 = f_um - i_um
print('\n1000 ordenado:\n',um_pior)
print('\nTempo de  execução:',t1)

## 2000
print('\n2000 pior caso:\n',dois_pior)
i_dois = time.time()
bubble_sort(dois_pior)
f_dois = time.time()
t2 = f_dois - i_dois
print('\n2000 ordenado:\n',dois_pior)
print('\nTempo de  execução:',t2)

## 3000
print('\n3000 pior caso:\n',tres_pior)
i_tres = time.time()
bubble_sort(tres_pior)
f_tres = time.time()
t3 = f_tres - i_tres
print('\n3000 ordenado:\n',tres_pior)
print('\nTempo de  execução:',t3)

## 4000
print('\n4000 pior caso:\n',quatro_pior)
i_quatro = time.time()
bubble_sort(quatro_pior)
f_quatro = time.time()
t4 = f_quatro - i_quatro
print('\n4000 ordenado:\n',quatro_pior)
print('\nTempo de  execução:',t4)

## 5000
print('\n5000 pior caso:\n',cinco_pior)
i_cinco = time.time()
bubble_sort(cinco_pior)
f_cinco = time.time()
t5 = f_cinco - i_cinco
print('\n5000 ordenado:\n',cinco_pior)
print('\nTempo de  execução:',t5)

## 8000
print('\n8000 pior caso:\n',oito_pior)
i_oito = time.time()
bubble_sort(oito_pior)
f_oito = time.time()
t8 = f_oito - i_oito
print('\n8000 ordenado:\n',oito_pior)
print('\nTempo de  execução:',t8)

## 11000
print('\n11000 pior caso:\n',onze_pior)
i_onze = time.time()
bubble_sort(onze_pior)
f_onze = time.time()
t11 = f_onze - i_onze
print('\n11000 ordenado:\n',onze_pior)
print('\nTempo de  execução:',t11)

## 15000
print('\n15000 pior caso:\n',quinze_pior)
i_quinze = time.time()
bubble_sort(quinze_pior)
f_quinze = time.time()
t15 = f_quinze - i_quinze
print('\n15000 ordenado:\n',quinze_pior)
print('\nTempo de  execução:',t15)

## Atribuindo o eixo x e y do gráfico
x = ['1000', '2000', '3000', '4000', '5000', '8000', '11000', '15000'] ## tamanhos
y = [t1, t2, t3, t4, t5, t8, t11, t15] ## tempo de ordenação 

## Criação do Gráfico 
plt.bar(x, y)
plt.title('Bubble Sort - Pior Caso')
plt.xlabel('Tamanho')
plt.ylabel('Tempo segs')
plt.show() ## Mostrar Grafico 