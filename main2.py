#!/usr/bin/env python 
# encoding:UTF-8

from models.vector_model import VectorModel
import sys 

def main():
    M= [u"O peã e o caval são pec de xadrez. O caval é o melhor do jog.",
        u"A jog envolv a torr, o peã e o rei.",
        u"O peã lac o boi",
        u"Caval de rodei!",
        u"Polic o jog no xadrez."]; #conjunto de documentos

    stopwords=[u"a",u"o",u"e",u"é",u"de",u"do",u"no",u"são"]; #lista de stopwords
    q=u"xadrez peã caval torr"; #consulta
    separadores=[u" ",u",",u".",u"!",u"?"]; #separadores para tokenizacao

    model = VectorModel(stopwords,separadores,None)

    model.preprocess_database(M)

    for i in range(len(model.tokens)):
        sys.stdout.write(str(model.im[i]))
        print model.tokens[i]

    print "\n\n"

    for i in range(len(model.tokens)):
        sys.stdout.write(str(model.wm[i]))
        print model.tokens[i]

    print "\n\n"

    for i in range(len(model.tokens)):
        sys.stdout.write("["+str(model.n[i])+"]")
        print model.tokens[i]

    print "\n\n"

    (im_q,wm_q,wvd) = model.preprocess_query(q)

    for i in range(model.n_docs):
        sys.stdout.write(str(i+1) + " - ")
        print wvd[i]

    print "\n\n" 

    #print process(matriz_incidencia,tokens,q)
    #print process(matriz_incidencia,tokens,u"xadrez peã")

if __name__ == "__main__": main()
