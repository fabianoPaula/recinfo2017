#!/usr/bin/env python
# encoding: UTF-8

import numpy as np


M= [u"O peã e o caval são pec de xadrez. O caval é o melhor do jog.",
    u"A jog envolv a torr, o peã e o rei.",
    u"O peã lac o boi",
    u"Caval de rodei!",
    u"Polic o jog no xadrez."]; #conjunto de documentos

stopwords=[u"a",u"o",u"e",u"é",u"de",u"do",u"no",u"são"]; #lista de stopwords
q=u"xadrez peã caval torr"; #consulta
separadores=[u" ",u",",u".",u"!",u"?"]; #separadores para tokenizacao

def tokenizador(palavra,separadores):
    lista_tokens = []
    last_sep = -1
    next_sep = 0
    while(last_sep < len(palavra)):
        if( next_sep == len(palavra)):
            lista_tokens.append(palavra[last_sep+1:next_sep])
            break
        if( palavra[next_sep] in separadores ):
            lista_tokens.append(palavra[last_sep+1:next_sep])
            last_sep = next_sep
            if next_sep < len(palavra):
                next_sep += 1
        else:
            if next_sep < len(palavra):
                next_sep += 1
    lista_tokens_sem_vazios = []
    for word in lista_tokens:
        if( not (word == '') ):
            lista_tokens_sem_vazios.append(word)
    return lista_tokens_sem_vazios

def normalizar(lista_tokens,stopwords):
    lista_tokens_sem_stopwords = []
    for w in lista_tokens:
        if(not(w.lower() in stopwords) ):
            lista_tokens_sem_stopwords.append(w.lower())
    return lista_tokens_sem_stopwords

index = [normalizar(tokenizador(doc,separadores),stopwords) for doc in M]

# Calculando o número de tokens 
# essa lista funciona como um dicionário 
# de posição nas colunas da matriz de incidência

tokens = []

for doc_index in index:
	for word in doc_index:
		if not( word in tokens):
			tokens.append(word)

#for w in tokens:
#	print w

n_docs = len(index)
n_tokens = len(tokens)


# Criando a matriz de incidência
matriz_incidencia = np.zeros(n_docs*n_tokens).reshape(n_tokens,n_docs)

for i in range(len(index)):
	for word in index[i]:
		matriz_incidencia[tokens.index(word),i] += 1

def list_and(lista1,lista2):
	resposta = []
	for i in range(len(lista1)):
		if not( lista1[i]*lista2[i] == 0):
			resposta.append(1)
		else:
			resposta.append(0)
	return resposta
	
def list_or(lista1,lista2):
	resposta = []
	for i in range(len(lista1)):
		if not( lista1[i] + lista2[i] == 0):
			resposta.append(1)
		else:
			resposta.append(0)
	return resposta

def list_not(lista):
	resposta = []
	for i in range(len(lista1)):
		resposta.append(1**lista[i])
	return resposta

# mi = matriz de incidencia
# t = lista de tokens 

def process(mi,t,query):
	lista_resposta = []
	listand = query.split(' ')

	print query
	
	if(len(listand) > 1):
		lista_resposta = list_and(mi[t.index(listand[0])],mi[t.index(listand[1])])
		for i in range(2,len(listand)):
			print lista_resposta
			lista_resposta = list_and(lista_resposta,mi[t.index(listand[i])])
		print lista_resposta
	else:
		lista_resposta = mi[t.index(listand[0])]

	resposta = []
	for i in range(len(lista_resposta)):
		if( lista_resposta[i] == 1):
			resposta.add(i)
	return resposta

print process(matriz_incidencia,tokens,q)


	


