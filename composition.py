from dottogr import *
from strtogr import *


def composition(gr1, gr2, name, draw):
    name = name + ".dot"
    str_g1 = []                                                                                                         # struttura primo grafo
    dot_not_struct(gr1, "og1", str_g1, 0)                                                                               # la riempo
    str_g2 = []                                                                                                         # struttura secondo grafo
    dot_not_struct(gr2, "og2", str_g2, 0)                                                                               # la riempo

    fus_str = []                                                                                                        # struttura del grafo fuso
    new_g1 = reassign_id(str_g1, 1)                                                                                     # riassegno gli id del primo grafo
    max = max_id(new_g1)                                                                                                # max id utilizzato nella prima struttura
    new_g2 = reassign_id(str_g2, max)                                                                                   # riassegno gli id del secondo grafo
    fus_str.append(node(0, "start", 1))                                                                                 # creo il nuovo start
    fus_str.append(node(1, "|"))                                                                                        # nodo[|]
    lastg1 = None                                                                                                       # id ultimo nodo primo grafo
    for elm in range(new_g1.__len__()):                                                                                 # copio la struttura del primo grafo in quella di fusione
        fus_str.append(new_g1[elm])
        if new_g1[elm].next_node.__len__() == 0:
            lastg1 = new_g1[elm].id
    fus_str[1].next_node.append(new_g1[0].id)                                                                           # connetto il parallelo

    lastg2 = None                                                                                                       # id ultimo nodo secondo grafo
    for elm in range(new_g2.__len__()):                                                                                 # copio la struttura del secondo grafo in quella di fusione
        fus_str.append(new_g2[elm])
        if new_g2[elm].next_node.__len__() == 0:
            lastg2 = new_g2[elm].id
    fus_str[1].next_node.append(new_g2[0].id)                                                                           # connetto il parallelo

    lastg1 = find_pos(fus_str, lastg1)                                                                                  # cerco la posizione nella struttura
    lastg2 = find_pos(fus_str, lastg2)                                                                                  # dei due nodi finali

    id_max = max_id(fus_str)                                                                                            # per poi richiudere il tutto
    fus_str[lastg1].next_node.append(id_max)
    fus_str[lastg2].next_node.append(id_max)
    fus_str.append(node(id_max, "|", id_max + 1))
    fus_str.append(node(id_max + 1, "end"))

    if draw:
        draw_graph(fus_str, name)
    else:
        return fus_str


def fusion2(g1, g2, nome, node_fusion, draw):
    fus_str = composition(g1, g2, nome, 0)
    nd1 = node_fusion[0]
    nd2 = node_fusion[1]
    maxid = max_id(fus_str)                                                                                             # max id utilizzato nella prima struttura
    fus_list = []
    for i in range(nd1.__len__()):                                                                                      # per ogni primo nodo
        x1 = ist_to_pos(fus_str, nd1[i])
        for n in range(nd2.__len__()):                                                                                  # ciclo i secondi nodi
            for e in range(fus_str.__len__()):
                if nd2[n] == fus_str[e].ist:                                                                            # quelli che hanno lo stesso messaggio
                    x2 = fus_str[e].id
                    a = [x1, x2]                                                                                        # verranno inseriti in una lista a coppie
                    fus_list.append(a)

    spider = []                                                                                                         # array contenente la futura struttura di fusione
    ap = maxid + 1                                                                                                      # aperti paralleli
    it = ap + fus_list.__len__()                                                                                        # istruzioni
    cp = it + fus_list.__len__()                                                                                        # chiusi paralleli
    cc = cp + fus_list.__len__()                                                                                        # chiusi choice
    modnode = []                                                                                                        # traccia i nodi usati in apertura
    modnode2 = []                                                                                                       # traccia i nodi usati in chiusura

    for i in range(fus_list.__len__()):                                                                                 # ciclo tutte le coppie di fusione
        an = fus_list[i][0]                                                                                             # primo nodo
        bn = fus_list[i][1]                                                                                             # secondo nodo

        if an not in modnode:                                                                                           # se an non è ancora stato anlaizzato in apertura
            modnode.append(an)                                                                                          # lo aggungo alla lista
            spider.append(node(fus_str[find_pos(fus_str, an)].id, "+", ap))                                             # lo aggungo alla lista
        else:
            spider[find_pos(spider, an)].next_node.append(ap)                                                           # altrimenti gli aggiungo successori

        if bn not in modnode:                                                                                           # uguale ad an
            modnode.append(bn)
            spider.append(node(fus_str[find_pos(fus_str, bn)].id, "+", ap))
        else:
            spider[find_pos(spider, bn)].next_node.append(ap)

        spider.append(node(ap, "|", it))                                                                                # creo il nodo di apertura parallelo
        ap += 1
        new_ist = fus_str[find_pos(fus_str, an)].snd + " -> " + fus_str[find_pos(fus_str, bn)].recv\
                  + " : " + fus_str[find_pos(fus_str, bn)].msg
        spider.append(node(it, new_ist, cp))                                                                            # creo il nodo di istruzione
        it += 1
        spider.append(node(cp, "|"))                                                                                    # creo il nodo di chiusura parallelo
        cp += 1
        tmp = spider.__len__()

        if an not in modnode2:                                                                                          # se an non è ancora stato anlaizzato in chiusura
            modnode2.append(an)                                                                                         # lo aggungo alla lista
            spider[tmp - 1].next_node.append(cc)                                                                        # connetto il precedente nodo
            spider.append(node(cc, "+", fus_str[find_pos(fus_str, bn)].next_node[0]))                                   # lo aggungo alla lista
            cc += 1
        else:
            spider[tmp - 1].next_node.append(fus_str[find_pos(fus_str, bn)].next_node[0])                               # altrimenti gli aggiungo successori

        if bn not in modnode2:                                                                                          # uguale ad an
            modnode2.append(bn)
            spider[tmp - 1].next_node.append(cc)
            spider.append(node(cc, "+", fus_str[find_pos(fus_str, an)].next_node[0]))
            cc += 1
        else:
            spider[tmp - 1].next_node.append(fus_str[find_pos(fus_str, an)].next_node[0])

    final = []                                                                                                          # struttura finale
    for nod in range(fus_str.__len__()):                                                                                # ci copio tutti i nodi tranne quelli che ho fuso
        if fus_str[nod].ist not in nd1 and fus_str[nod].ist not in nd2:
            final.append(fus_str[nod])

    for nod in range(spider.__len__()):                                                                                 # aggiungo anche spider
        final.append(spider[nod])

    if draw:
        draw_graph(final, nome + ".dot")
