# encoding: UTF-8

class BaseMetric(object):
    
    def __init__(self, D = [], R = [], R1 = [], R2 = [] ):
        self.Rank1 = R1
        self.Rank2 = R2

        self.R1 = {}
        self.R2 = {}

        self.R  = R

        self.R1["relevant_list"] = []
        self.R2["relevant_list"] = []
        
        # Calculating the revocation
        num_R1 = .0
        num_R2 = .0
        
        for doc in R1:
            if doc in R:
                num_R1 += 1.0
            self.R1["relevant_list"].append(num_R1)

        for doc in R2:
            if doc in R:
                num_R2 += 1.0
            self.R2["relevant_list"].append(num_R2)

        self.R1["precision"] = num_R1/len(R1) 
        self.R2["precision"] = num_R2/len(R2) 

        self.R1["revocation"] = num_R1/len(R) 
        self.R2["revocation"] = num_R2/len(R) 

        self.R1["f1_measure"] = self.f1_measure(self.R1["revocation"],self.R1["precision"],1.0)  
        self.R2["f1_measure"] = self.f1_measure(self.R2["revocation"],self.R2["precision"],1.0)  

        self.R1["precision_list"] = [] 
        self.R2["precision_list"] = [] 

        self.R1["revocation_list"] = [] 
        self.R2["revocation_list"] = [] 

        for i,doc in enumerate(R1):
            self.R1["revocation_list"].append(self.R1["relevant_list"][i]/len(self.R))
            self.R1["precision_list"].append(self.R1["relevant_list"][i]/i)


        for i,doc in enumerate(R2):
            self.R2["revocation_list"].append(self.R2["relevant_list"][i]/len(self.R))
            self.R2["precision_list"].append(self.R2["relevant_list"][i]/i)




    def f1_measure(self,revocation,precision,beta):
        aux = (1.0 + beta**2)*revocation*precision/  \
                (beta**2 *precision) + revocation
        return aux
        

         

        
        

        
        
