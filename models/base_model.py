# encoding: UTF-8

class BaseModel(object):

    def __init__(self,stopwords = [],separators = [],steammer = None):
        self.stopwords  = stopwords
        self.separators = separators 
        self.steammer   = steammer 

    def steamming(self,word):
        print "Not implemented"
        

    def tokenizer(self,string):
        token_list = []
        last_sep = -1
        next_sep = 0
        while(last_sep < len(string)):
            if( next_sep == len(string)):
                token_list.append(string[last_sep+1:next_sep])
                break
            if( string[next_sep] in self.separators ):
                token_list.append(string[last_sep+1:next_sep])
                last_sep = next_sep
                if next_sep < len(string):
                    next_sep += 1
            else:
                if next_sep < len(string):
                    next_sep += 1
        token_list_cleanned = []
        for word in token_list:
            if( not (word == '') ):
                token_list_cleanned.append(word)
        return token_list_cleanned

    def normalizer(self,token_list):
        token_list_without_stopwords = []
        for word in token_list:
            if(not(word.lower() in self.stopwords) ):
                token_list_without_stopwords.append(word.lower())
        return token_list_without_stopwords

    #-------------------------------------------------------------------------
    #             PROCESS AND PREPROCESS FUNCTIONS
    #-------------------------------------------------------------------------

    # Preprocessing of database
    def preprocess_database(self,database):
        print "Not implemented! "

    # preprocessing of query
    def preprocess_query(self,query):
        print "Not Implemented! "
