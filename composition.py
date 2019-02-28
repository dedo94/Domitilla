from dottogr import *
from function import *


def composition(gr1, gr2, name, draw):
    name = name + ".gv"
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
    name = nome + ".gv"
    nf_id = []                                                                                                          # modifico la lista di nodi di fusione
    for el in range(node_fus.__len__()):                                                                                # traformando i label in id
        node1 = node_fus[el][0]
        node2 = node_fus[el][1]
        new_cp = [ist_to_id(gr_st, node1), ist_to_id(gr_st, node2)]
        nf_id.append(new_cp)

    maxid = max_id(gr_st)                                                                                               # max id utilizzato nella prima struttura
    check = []
    opchid = []                                                                                                         # open choice id
    clchid = []                                                                                                         # close choice io
    fus_st = []                                                                                                         # struttura spiders
    for el in range(nf_id.__len__()):
        pos1 = search_node(gr_st, nf_id[el][0])                                                                         # posizione nella struttura del primo id
        pos2 = search_node(gr_st, nf_id[el][1])                                                                         # posizione nella struttura del secondo id
        if gr_st[pos1].msg == gr_st[pos2].msg:                                                                          # controllo abbiano lo stesso messaggio
            tmpplop = maxid                                                                                             # temporary parallel open
            fus_st.append(node(maxid, "|", maxid + 1))
            maxid += 1
            newist = gr_st[pos1].snd + " -> " + gr_st[pos2].recv + " : " + gr_st[pos2].msg
            fus_st.append(node(maxid, newist, maxid + 1))
            maxid += 1
            fus_st.append(node(maxid, "|"))
            tmpplcl = maxid                                                                                             #temporary parallel close
            maxid += 1
            if nf_id[el][0] not in check:                                                                               # analizzo primo nodo della coppia, se nuovo
                check.append(nf_id[el][0])                                                                              # lo agungo alla lista "check"
                fus_st.append(node(nf_id[el][0], "+", tmpplop))                                                         # gli creo il nodo + di inizio e lo collego
                opchid.append(nf_id[el][0])                                                                             # aggiungo il suo id alla lista opchid
                fus_st.append(node(maxid, "+", gr_st[id_to_pos(gr_st, nf_id[el][0])].next_node[0]))                     # gli creo il nodo + di fine e lo collego
                clchid.append(maxid)                                                                                    # aggiungo il suo id alla lista clchid
                fus_st[id_to_pos(fus_st, tmpplcl)].next_node.append(maxid)
                maxid += 1
            else:
                fus_st[id_to_pos(fus_st, nf_id[el][0])].next_node.append(tmpplop)                                       # connetto il + di inizio con il | di inizio
                i = check.index(nf_id[el][0])
                fus_st[id_to_pos(fus_st, tmpplcl)].next_node.append(clchid[i])                                          # connetto il | finale con il + di chiusura

            if nf_id[el][1] not in check:                                                                               # ripeto per il secondo nodo della coppia
                check.append(nf_id[el][1])
                fus_st.append(node(nf_id[el][1], "+", tmpplop))
                opchid.append(nf_id[el][1])
                fus_st.append(node(maxid, "+", gr_st[id_to_pos(gr_st, nf_id[el][1])].next_node[0]))
                clchid.append(maxid)
                fus_st[id_to_pos(fus_st, tmpplcl)].next_node.append(maxid)
                maxid += 1
            else:
                fus_st[id_to_pos(fus_st, nf_id[el][1])].next_node.append(tmpplop)
                i = check.index(nf_id[el][1])
                fus_st[id_to_pos(fus_st, tmpplcl)].next_node.append(clchid[i])
    final_st = []
    for ele in range(gr_st.__len__()):
        if gr_st[ele].id not in check:
            final_st.append(gr_st[ele])

    for elm in range(fus_st.__len__()):
        final_st.append(fus_st[elm])

    if draw:
        draw_graph(final_st, name)
