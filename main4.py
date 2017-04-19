#!/usr/bin/env python 
# encoding:UTF-8

from models.bm25_model import BM25Model
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

    model = BM25Model(stopwords,separadores,None,1.0,0.75)

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

    (im_q,wm_q) = model.preprocess_query(q)

    index  = [(i,b) for i,b in enumerate(wm_q) ]
    index_sorted = sorted(index, key=lambda tup: tup[1], reverse=True)

    for elem in index_sorted:
        sys.stdout.write(str(int(elem[0])+1) + " - ")
        print elem[1]

    print "\n\n" 

    #print process(matriz_incidencia,tokens,q)
    #print process(matriz_incidencia,tokens,u"xadrez peã")

if __name__ == "__main__": main()
