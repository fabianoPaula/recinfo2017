# encoding: UTF-8

from numpy import log2,zeros,dot
from numpy import linalg as LA
from numpy import average as avg


from base_model import BaseModel

class BM25Model(BaseModel):

    def __init__(self,stopwords = [],separators = [],steammer = None, k1 = 1.0,b = 0.75):
        super(BM25Model,self).__init__(stopwords,separators,steammer)
        self.K1 = k1
        self.b  = b
        
    #-------------------------------------------------------------------------
    #             PROCESS AND PREPROCESS FUNCTIONS
    #-------------------------------------------------------------------------

    # Preprocessing of database

    # avg_doclen = média do tamanho dos documentos
    # len(d_j)   = tamanho do documento
    def preprocess_database(self,database):
        self.index = []
        for doc in database:
            token_list = super(BM25Model,self).tokenizer(doc)
            self.index.append(super(BM25Model,self).normalizer(token_list))

        # this list is a position token dicionary 
        # of lines in the incidence matrix 
        self.tokens = []
        # quantidade de tokens no documento/tamanho do documento
        self.doclen = zeros(len(self.index))
        for i,doc_index in enumerate(self.index):
            self.doclen[i] = len(doc_index)
            for word in doc_index:
                if not(word in self.tokens):
                    self.tokens.append(word)

        # média da quantidade de tokens no documento/tamanho do documento
        self.avg_doclen = avg(self.doclen) 

        # vetor armazenando os tamanhos normalizados
        self.avg_doclen_v = [ doclen/self.avg_doclen for doclen in self.doclen]

        self.tokens = sorted(self.tokens)

        self.n_docs   = len(self.index)
        self.n_tokens = len(self.tokens)

        # Incidence Matrix
        self.im = zeros(self.n_docs*self.n_tokens).reshape(self.n_tokens,self.n_docs)
        # B matrix 
        self.B = zeros(self.n_docs*self.n_tokens).reshape(self.n_tokens,self.n_docs)
        # weigth matrix
        self.wm = zeros(self.n_docs*self.n_tokens).reshape(self.n_tokens,self.n_docs)
        # vector n
        self.n  = zeros(self.n_tokens)

        for i in range(len(self.index)):
            for word in self.index[i]:
                self.im[self.tokens.index(word),i] += 1

        # Contain the number of docs that a token appeared
        for i in range(self.im.shape[0]):
            for num in self.im[i]:
                if( num > 0):
                    self.n[i] += 1

        # Calculating the weigth using the third schema
        for i in range(self.B.shape[0]):
            for j in range(self.B.shape[1]):
                if not( self.im[i,j] == 0):
                    self.B[i,j] = ((self.K1+1.0)*self.im[i,j])/        \
                    (self.K1*((1-self.b) +  self.b*self.avg_doclen_v[j]) \
                    + self.im[i,j])

        return self


    # preprocessing of query
    def preprocess_query(self,query):
        token_list  = super(BM25Model,self).tokenizer(query)
        query_index = super(BM25Model,self).normalizer(token_list)

        # Creating incidence matrix for the query
        im = zeros(self.n_tokens)
        # Creating weigth matrix for the query
        wm = zeros(self.n_docs)

        for word in query_index:
            im[self.tokens.index(word)] += 1

        # Calculating the weigth using the BM25 schema
        for j in xrange(self.n_docs):
            for token in query_index: 
                flag1 = True
                try:
                    i = self.tokens.index(token)
                except:
                    flag1 = False
                if( flag1 ):
                    if ( self.im[i,j] > 0) :
                        wm[j] += self.B[i,j]* \
                        log2(( self.n_docs - self.n[i] + 0.5)/ (self.n[i] + 0.5))

        return(im,wm)

