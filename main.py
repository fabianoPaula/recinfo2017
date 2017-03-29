#!/usr/bin/env python 
# encoding:UTF-8

from modelo_booleano import *

def main():
    M= [u"O peã e o caval são pec de xadrez. O caval é o melhor do jog.",
        u"A jog envolv a torr, o peã e o rei.",
        u"O peã lac o boi",
        u"Caval de rodei!",
        u"Polic o jog no xadrez."]; #conjunto de documentos

    stopwords=[u"a",u"o",u"e",u"é",u"de",u"do",u"no",u"são"]; #lista de stopwords
    q=u"xadrez peã caval torr"; #consulta
    separadores=[u" ",u",",u".",u"!",u"?"]; #separadores para tokenizacao

    (matriz_incidencia,matriz_pesos,tokens,n) = preprocess_database(M,stopwords,separadores)

    for i in range(len(tokens)):
        sys.stdout.write(str(matriz_incidencia[i]))
        print tokens[i]

    for i in range(len(tokens)):
        sys.stdout.write(str(matriz_pesos[i]))
        print tokens[i]

    for i in range(len(tokens)):
        sys.stdout.write("["+str(n[i])+"]")
        print tokens[i]

    print "\n\n\n\n"


    (matriz_incidencia_q,matriz_pesos_q,tokens_q) = preprocess_query(n,matriz_incidencia,tokens,q,stopwords,separadores)

    for i in range(len(tokens_q)):
        sys.stdout.write(str(matriz_incidencia_q[i]))
        print tokens[i]
    print "\n\n"
    for i in range(len(tokens_q)):
        sys.stdout.write(str(matriz_pesos_q[i]))
        print tokens[i]

    #print process(matriz_incidencia,tokens,q)
    #print process(matriz_incidencia,tokens,u"xadrez peã")


if __name__ == "__main__": main()
