from dottogr import *
from function import *

# permette di realizzae una composizione tra due grafi

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
    lastg2 = None                                                                                                       # id ultimo nodo secondo grafo

    for el in range(new_g1.__len__()):
        if new_g1[el].ist == "end":
            lastg1 = new_g1[el].id
        else:
            fus_str.append(new_g1[el])
    fus_str[1].next_node.append(new_g1[0].id)                                                                           # connetto il parallelo

    for el in range(new_g2.__len__()):
        if new_g2[el].ist == "end":
            lastg2 = new_g2[el].id
        else:
            fus_str.append(new_g2[el])
    fus_str[1].next_node.append(new_g2[0].id)                                                                           # connetto il parallelo

    id_max = max_id(fus_str)                                                                                            # per poi richiudere il tutto

    for el in range(fus_str.__len__()):
        for ele in range(fus_str[el].next_node.__len__()):
            if fus_str[el].next_node[ele] == lastg1:
                fus_str[el].next_node.remove(lastg1)
                fus_str[el].next_node.append(id_max)
            if fus_str[el].next_node[ele] == lastg2:
                fus_str[el].next_node.remove(lastg2)
                fus_str[el].next_node.append(id_max)

    fus_str.append(node(id_max, "|", id_max + 1))
    fus_str.append(node(id_max + 1, "end"))

    if draw:
        draw_graph(fus_str, name)

    return fus_str


# permette di realizzare la fusione di nodi all'interno di un grafo non strutturato gr_st

def refusion(gr_st, nome, node_fus, draw):
    name = nome + ".gv"                                                                                                 # modifico la lista di nodi di fusione
    nf_pos = []                                                                                                         # traformando i label in pos
    for el in range(node_fus.__len__()):                                                                                # ciclo le coppie di fusione
        for g1 in range(gr_st.__len__()):                                                                               # ciclo la struttura
            if gr_st[g1].ist == node_fus[el][0]:                                                                        # quando trovo il primo nodo
                for g2 in range(gr_st.__len__()):                                                                       # riciclo la struttura
                    if gr_st[g2].ist == node_fus[el][1]:                                                                # finche trovo dei match
                        pos_cp = [g1, g2]                                                                               # creo le coppie posizione
                        nf_pos.append(pos_cp)                                                                           # e le aggiungo alla lista
    maxid = max_id(gr_st)                                                                                               # max id utilizzato nella prima struttura
    check = []
    opchid = []                                                                                                         # open choice id
    clchid = []                                                                                                         # close choice io
    fus_st = []                                                                                                         # struttura spiders
    for el in range(nf_pos.__len__()):
        pos1 = nf_pos[el][0]
        pos2 = nf_pos[el][1]
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
            if gr_st[nf_pos[el][0]].id not in check:                                                                    # analizzo primo nodo della coppia, se nuovo
                check.append(gr_st[nf_pos[el][0]].id)                                                                   # lo agungo alla lista "check"
                fus_st.append(node(gr_st[nf_pos[el][0]].id, "+", tmpplop))                                              # gli creo il nodo + di inizio e lo collego
                opchid.append(gr_st[nf_pos[el][0]].id)                                                                  # aggiungo il suo id alla lista opchid
                fus_st.append(node(maxid, "+", gr_st[nf_pos[el][0]].next_node[0]))                                      # gli creo il nodo + di fine e lo collego
                clchid.append(maxid)                                                                                    # aggiungo il suo id alla lista clchid
                fus_st[id_to_pos(fus_st, tmpplcl)].next_node.append(maxid)
                maxid += 1
            else:
                fus_st[id_to_pos(fus_st, gr_st[nf_pos[el][0]].id)].next_node.append(tmpplop)                            # connetto il + di inizio con il | di inizio
                i = check.index(gr_st[nf_pos[el][0]].id)
                fus_st[id_to_pos(fus_st, tmpplcl)].next_node.append(clchid[i])                                          # connetto il | finale con il + di chiusura

            if nf_pos[el][1] not in check:                                                                              # ripeto per il secondo nodo della coppia
                check.append(gr_st[nf_pos[el][1]].id)
                fus_st.append(node(gr_st[nf_pos[el][1]].id, "+", tmpplop))
                opchid.append(gr_st[nf_pos[el][1]].id)
                fus_st.append(node(maxid, "+", gr_st[nf_pos[el][1]].next_node[0]))
                clchid.append(maxid)
                fus_st[id_to_pos(fus_st, tmpplcl)].next_node.append(maxid)
                maxid += 1
            else:
                fus_st[id_to_pos(fus_st, gr_st[nf_pos[el][1]].id)].next_node.append(tmpplop)
                i = check.index(gr_st[nf_pos[el][1]].id)
                fus_st[id_to_pos(fus_st, tmpplcl)].next_node.append(clchid[i])
    final_st = []
    for ele in range(gr_st.__len__()):
        if gr_st[ele].id not in check:
            final_st.append(gr_st[ele])

    for elm in range(fus_st.__len__()):
        final_st.append(fus_st[elm])

    if draw:
        draw_graph(final_st, name)
    else:
        return final_st
