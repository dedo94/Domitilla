from dottogr import *
from function import *


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

    return fus_str


def refusion(gr_st, nome, node_fus, draw):
    name = nome + ".dot"
    totcpid = []
    for i in range(gr_st.__len__()):
        for t in range(node_fus.__len__()):
            if gr_st[i].ist == node_fus[t]:
                for j in range(i, gr_st.__len__()):
                    for r in range(node_fus.__len__()):
                        if gr_st[j].ist == node_fus[r] and gr_st[i].ist != gr_st[j].ist:
                            cpid = [int(gr_st[i].id), int(gr_st[j].id)]
                            totcpid.append(cpid)
    maxid = max_id(gr_st)                                                                                               # max id utilizzato nella prima struttura
    check = []
    opchid = []
    clchid = []
    fus_st = []
    for el in range(totcpid.__len__()):
        pos1 = id_to_pos(gr_st, totcpid[el][0])
        pos2 = id_to_pos(gr_st, totcpid[el][1])
        tmpplop = maxid
        fus_st.append(node(maxid, "|", maxid + 1))
        maxid += 1
        newist = gr_st[pos1].snd + " -> " + gr_st[pos2].recv + " : " + gr_st[pos2].msg
        fus_st.append(node(maxid, newist, maxid + 1))
        maxid += 1
        fus_st.append(node(maxid, "|"))
        tmpplcl = maxid
        maxid += 1

        if totcpid[el][0] not in check:                                                                                 # analizzo primo nodo della coppia, se nuovo
            check.append(totcpid[el][0])                                                                                # lo agungo alla lista "check"
            fus_st.append(node(totcpid[el][0], "+", tmpplop))                                                           # gli creo il nodo + di inizio e lo collego
            opchid.append(totcpid[el][0])                                                                               # aggiungo il suo id alla lista opchid
            fus_st.append(node(maxid, "+", gr_st[id_to_pos(gr_st, totcpid[el][0])].next_node[0]))                       # gli creo il nodo + di fine e lo collego
            clchid.append(maxid)                                                                                        # aggiungo il suo id alla lista clchid
            fus_st[id_to_pos(fus_st, tmpplcl)].next_node.append(maxid)
            maxid += 1
        else:
            fus_st[id_to_pos(fus_st, totcpid[el][0])].next_node.append(tmpplop)                                         # connetto il + di inizio con il | di inizio
            i = check.index(totcpid[el][0])
            fus_st[id_to_pos(fus_st, tmpplcl)].next_node.append(clchid[i])                                              # connetto il | finale con il + di chiusura

        if totcpid[el][1] not in check:                                                                                 # ripeto per il secondo nodo della coppia
            check.append(totcpid[el][1])
            fus_st.append(node(totcpid[el][1], "+", tmpplop))
            opchid.append(totcpid[el][1])
            fus_st.append(node(maxid, "+", gr_st[id_to_pos(gr_st, totcpid[el][1])].next_node[0]))
            clchid.append(maxid)
            fus_st[id_to_pos(fus_st, tmpplcl)].next_node.append(maxid)
            maxid += 1
        else:
            fus_st[id_to_pos(fus_st, totcpid[el][1])].next_node.append(tmpplop)
            i = check.index(totcpid[el][1])
            fus_st[id_to_pos(fus_st, tmpplcl)].next_node.append(clchid[i])

    final_st = []
    for ele in range(gr_st.__len__()):
        if int(gr_st[ele].id) not in check:
            final_st.append(gr_st[ele])

    for elm in range(fus_st.__len__()):
        final_st.append(fus_st[elm])

    if draw:
        draw_graph(final_st, name)
