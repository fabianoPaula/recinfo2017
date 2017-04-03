# encoding: UTF-8

from numpy import zeros

from base_model import BaseModel

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

    #-------------------------------------------------------------------------
    #             PROCESS AND PREPROCESS FUNCTIONS
    #-------------------------------------------------------------------------

    # preprocessing of the database
    def preprocess_database(self,database):
        self.index = []
        for doc in database:
            token_list = super(BooleanModel,self).tokenizer(doc)
            self.index.append(super(BooleanModel,self).normalizer(token_list))

        self.tokens = []
        for doc_index in self.index:
            for word in doc_index:
                if not(word in tokens):
                    self.tokens.append(word)

        self.n_docs   = len(self.index)
        self.n_tokens = len(self.tokens)

        # Incidence Matrix
        self.im = zeros(self.n_docs*self.n_tokens).reshape(self.n_tokens,self.n_docs)

        for i in range(len(self.index)):
            for word in index[i]:
                im[self.tokens.index(word),i] += 1


    # function that process a query
    def process(self,query):
        listand = query.split(' ')
        response_list = []

        if(len(listand) > 1):
            response_list = list_and(self.im[self.tokens.index(listand[0])],self.im[self.tokens.index(listand[1])])
            for i in range(2,len(listand)):
                response_list = list_and(response_list,self.im[self.tokens.index(listand[i])])
        else:
            response_list = self.im[self.tokens.index(listand[0])]

        result = []
        for i in range(len(response_list)):
            if(response_list[i] == 1):
                    result.append(i+1)
        return result 

