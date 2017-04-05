# encoding: UTF-8

from numpy import log2,zeros,dot
from numpy import linalg as LA


from base_model import BaseModel

class VectorModel(BaseModel):

    #-------------------------------------------------------------------------
    #             PROCESS AND PREPROCESS FUNCTIONS
    #-------------------------------------------------------------------------

    # Preprocessing of database
    def preprocess_database(self,database):
        self.index = []
        for doc in database:
            token_list = super(VectorModel,self).tokenizer(doc)
            self.index.append(super(VectorModel,self).normalizer(token_list))

        # this list is a position token dicionary 
        # of lines in the incidence matrix 
        self.tokens = []
        for doc_index in self.index:
            for word in doc_index:
                if not(word in self.tokens):
                    self.tokens.append(word)

        self.tokens = sorted(self.tokens)

        self.n_docs   = len(self.index)
        self.n_tokens = len(self.tokens)

        # Incidence Matrix
        self.im = zeros(self.n_docs*self.n_tokens).reshape(self.n_tokens,self.n_docs)
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
        for i in range(self.im.shape[0]):
            for j in range(self.im.shape[1]):
                if not( self.im[i,j] == 0):
                    self.wm[i,j] = (1 + log2(self.im[i,j]))*log2(self.n_docs/self.n[i])

        return self


    # preprocessing of query
    def preprocess_query(self,query):
        token_list  = super(VectorModel,self).tokenizer(query)
        query_index = super(VectorModel,self).normalizer(token_list)

        # Creating incidence matrix for the query
        im = zeros(self.n_tokens)
        # Creating weigth matrix for the query
        wm = zeros(self.n_tokens)

        for word in query_index:
            im[self.tokens.index(word)] += 1

        # Calculating the weigth using the third schema
        for j in range(self.n_tokens):
            if not( im[j] == 0):
                wm[j] = (1 + log2(im[j]))*log2(self.n_docs/self.n[j])

        # Creating the weigth for documents with query 
        wvd = zeros(self.n_docs)

        # matrix documents x tokens
        mdt = self.wm.T

        for j in range(self.n_docs):
            wvd[j] = mdt[j].dot(wm) / (LA.norm(mdt[j])*LA.norm(wm))
        

        return(im,wm,wvd)

