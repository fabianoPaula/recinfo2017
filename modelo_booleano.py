# encoding: UTF-8

import numpy as np
from numpy import log2
import sys

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


def preprocess_database(M,stopwords,separadores):
    index = [normalizar(tokenizador(doc,separadores),stopwords) for doc in M]

    # Calculando o número de tokens
    # essa lista funciona como um dicionário
    # de posição nas colunas da matriz de incidência
    tokens = []
    for doc_index in index:
	for word in doc_index:
            if not( word in tokens):
		tokens.append(word)

    n_docs = len(index)
    n_tokens = len(tokens)

    # Criando a matriz de incidência
    matriz_incidencia = np.zeros(n_docs*n_tokens).reshape(n_tokens,n_docs)
    matriz_pesos = np.zeros(n_docs*n_tokens).reshape(n_tokens,n_docs)
    n = np.zeros(n_tokens)

    for i in range(len(index)):
	for word in index[i]:
		matriz_incidencia[tokens.index(word),i] += 1

    # Calculando o vetor n
    # Esse vetor contém quantos documentos o token apareceu
    for i in range(matriz_incidencia.shape[0]):
        for num in matriz_incidencia[i]:
            if( num > 0):
                n[i] += 1
    # Calculando os pesos das consultas usando o esquema três
    for i in range(matriz_incidencia.shape[0]):
        for j in range(matriz_incidencia.shape[1]):
            if not( matriz_incidencia[i,j] == 0):
                matriz_pesos[i,j] = (1 + log2(matriz_incidencia[i,j]))* \
                                log2(n_docs/n[i])

    for i in range(len(tokens)):
        sys.stdout.write(str(matriz_incidencia[i]))
        print tokens[i]

    return(matriz_incidencia,matriz_pesos,tokens,n)


# preprocessamento da query
# mi = matriz de incidência
# mp = matriz de pesos

def preprocess_query(n,mi,tokens_d,query,stopwords,separadores):
    n_docs_d = mi.shape[1]
    index = [normalizar(tokenizador(query,separadores),stopwords)]

    # Calculando o número de tokens
    # essa lista funciona como um dicionário
    # de posição nas colunas da matriz de incidência
    tokens = []
    for doc_index in index:
	for word in doc_index:
            if not( word in tokens):
		tokens.append(word)

    n_docs = len(index)
    n_tokens = len(tokens)

    # Criando a matriz de incidência
    matriz_incidencia = np.zeros(n_docs*n_tokens).reshape(n_tokens,n_docs)
    matriz_pesos = np.zeros(n_docs*n_tokens).reshape(n_tokens,n_docs)

    for i in range(len(index)):
    	for word in index[i]:
  	    matriz_incidencia[tokens.index(word),i] += 1

    # Calculando os pesos das consultas usando o esquema três
    for i in range(matriz_incidencia.shape[0]):
        for j in range(matriz_incidencia.shape[1]):
            if not( matriz_incidencia[i,j] == 0):
                matriz_pesos[i,j] = (1 + log2(matriz_incidencia[i,j]))* \
                                log2(n_docs_d/n[tokens_d.index(tokens[i])])

    return(matriz_incidencia,matriz_pesos,tokens)


# função que processa a query
# mi = matriz de incidencia
# t = lista de tokens
def process(mi,t,query):
    lista_resposta = []
    listand = query.split(' ')




    if(len(listand) > 1):
	lista_resposta = list_and(mi[t.index(listand[0])],mi[t.index(listand[1])])
	for i in range(2,len(listand)):
		print lista_resposta
		lista_resposta = list_and(lista_resposta,mi[t.index(listand[i])])
    else:
	lista_resposta = mi[t.index(listand[0])]

	resposta = []
	for i in range(len(lista_resposta)):
		if( lista_resposta[i] == 1):
			resposta.append(i+1)
	return resposta


