#Listas
lista = [1,2,"Guilherme",5.5,True,'a']

for x in lista:
    print(x)

lista.append("Soares")  #adicionar nova variável na lista, coloca o soares no 7 elemento(índice 6)
lista[0] = 55 

for x in range(0,len(lista)): #imita o for do c++, vai de 0 até o tamanho da lista(de 0 até 7, mas o 7 n é incluído)
    if x == 2:
        continue
    print(lista[x])

#Dicionário  
dicionario = {"curso":"Informática Industrial","númeroCréditos":4}  #declara sempre em pares, coloca uma chave e um valor

print(dicionario)

dicionario["curso"] = "Robótica Móvel"
dicionario["NumeroHoras"] = 60

print(dicionario)

#Tuplas

tupla = (1,2,"Guilherme",5.5,True,'a')

print()

for x in tupla:
    print(x)


#Coleções ordenadas
pilha = []

for i in range(0,10):
    pilha.append(i)

for i in range(0,10):
    print(pilha.pop(),end=" ")

print()

from collections import deque

fila = deque() #fila é implementada com a classe deque

for i in range(0,10):
    fila.append(i) #insere no final

for i in range(0,10):
    print(fila.popleft(),end=" ")  #remove no início
