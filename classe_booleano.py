# encoding: UTF-8

import numpy as np
from numpy import log2
import sys

from base_class_ri import BaseModel

class BooleanModel(BaseModel):

    def list_and(self,list1,list2):
        response = []
        for i in range(len(list1)):
            if not( list1[i]*list2[i] == 0):
                response.append(1)
            else:
                response.append(0)
        return response

    def list_or(self,list1,list2):
        response = []
        for i in range(len(list1)):
            if not( list1[i] + list2[i] == 0):
                response.append(1)
            else:
                response.append(0)
        return response

    def list_not(self,list1):
        response = []
        for i in range(len(list1)):
            if( list1[i] == 0)
                response.append(1)
            else:
                response.append(0)
        return response

    # preprocessamento da matriz 

    def preprocess_database(self,database):
        self.index = [super(BooleanModel).normalizar(super(BooleanModel,self).tokenizador(doc)) for doc in database]

        # Calculando o número de tokens
        # essa lista funciona como um dicionário
        # de posição nas colunas da matriz de incidência
        self.tokens = []
        for doc_index in self.index:
            for word in doc_index:
                if not(word in tokens):
                    self.tokens.append(word)

        self.n_docs   = len(self.index)
        self.n_tokens = len(self.tokens)

        # Criando a matriz de incidência
        # Incidence Matrix
        self.im = np.zeros(self.n_docs*self.n_tokens).reshape(self.n_tokens,self.n_docs)
        # weigth matrix
        self.wm = np.zeros(self.n_docs*self.n_tokens).reshape(self.n_tokens,self.n_docs)
        self.n = np.zeros(self.n_tokens)

        for i in range(len(self.index)):
            for word in index[i]:
                im[self.tokens.index(word),i] += 1

        # Calculando o vetor n
        # Esse vetor contém quantos documentos o token apareceu
        for i in range(self.im.shape[0]):
            for num in self.im[i]:
                if( num > 0):
                    self.n[i] += 1

        # Calculando os pesos das consultas usando o esquema três
        for i in range(self.im.shape[0]):
            for j in range(self.im.shape[1]):
                if not( self.im[i,j] == 0):
                    self.wm[i,j] = (1 + log2(self.wm[i,j]))* \
                                    log2(self.n_docs/self.n[i])

        return self


    # preprocessamento da query
    # mi = matriz de incidência
    # mp = matriz de pesos

    def preprocess_query(query):
        query_index = super(BooleanModel,self).normalizar(super(BooleanModel,self).tokenizador(query))

        # Calculando o número de tokens
        # essa lista funciona como um dicionário
        # de posição nas colunas da matriz de incidência
        tokens = []
        for word in query_index:
            if not(word in tokens):
                tokens.append(word)

        n_tokens = len(tokens)

        # Criando a matriz de incidência
        im = np.zeros(n_tokens)
        wp = np.zeros(n_tokens)

        for word in query_index:
            im[tokens.index(word)] += 1

        # Calculando os pesos das consultas usando o esquema três
        for i in range(matriz_incidencia.shape[0]):
            for j in range(matriz_incidencia.shape[1]):
                if not( matriz_incidencia[i,j] == 0):
                    wm[i,j] = (1 + log2(im[i,j]))*log2(self.n_docs/n[self.tokens.index(tokens[i])])

        return(im,wm)


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

