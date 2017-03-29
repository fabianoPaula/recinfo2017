# encoding: UTF-8

from numpy import log2,zeros

from base_model import BaseModel

class WeigthedModel(BaseModel):

    #-------------------------------------------------------------------------
    #             PROCESS AND PREPROCESS FUNCTIONS
    #-------------------------------------------------------------------------

    # Preprocessing of database
    def preprocess_database(self,database):
        self.index = []
        for doc in database:
            token_list = super(BooleanModel,self).tokenizador(doc)
            self.index.append(super(BooleanModel,self).normalizar(token_list))

        # this list is a position token dicionary 
        # of lines in the incidence matrix 
        self.tokens = []
        for doc_index in self.index:
            for word in doc_index:
                if not(word in tokens):
                    self.tokens.append(word)

        self.n_docs   = len(self.index)
        self.n_tokens = len(self.tokens)

        # Incidence Matrix
        self.im = zeros(self.n_docs*self.n_tokens).reshape(self.n_tokens,self.n_docs)
        # weigth matrix
        self.wm = zeros(self.n_docs*self.n_tokens).reshape(self.n_tokens,self.n_docs)
        # vector n
        self.n = np.zeros(self.n_tokens)

        for i in range(len(self.index)):
            for word in index[i]:
                im[self.tokens.index(word),i] += 1

        # Contain the number of docs that a token appeared
        for i in range(self.im.shape[0]):
            for num in self.im[i]:
                if( num > 0):
                    self.n[i] += 1

        # Calculating the weigth using the third schema
        for i in range(self.im.shape[0]):
            for j in range(self.im.shape[1]):
                if not( self.im[i,j] == 0):
                    self.wm[i,j] = (1 + log2(self.wm[i,j]))* \
                                    log2(self.n_docs/self.n[i])

        return self


    # preprocessing of query
    def preprocess_query(query):
        token_list = super(BooleanModel,self).tokenizador(query)
        query_index = super(BooleanModel,self).normalizar(token_list)

        # this list is a position token dicionary 
        # of lines in the incidence matrix 
        tokens = []
        for word in query_index:
            if not(word in tokens):
                tokens.append(word)

        n_tokens = len(tokens)

        # Creating incidence matrix for the query
        im = zeros(n_tokens)
        # Creating weigth matrix for the query
        wp = zeros(n_tokens)

        for word in query_index:
            im[tokens.index(word)] += 1

        # Calculating the weigth using the third schema
        for j in range(im.shape[0]):
            if not( im[j] == 0):
                wm[j] = (1 + log2(im[j]))*log2(self.n_docs/n[self.tokens.index(tokens[j])])

        return(im,wm)

