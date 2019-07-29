from dottogr import *
from function import *


def multi(str, pt1, pt2):
    new = []
    ist_list = []
    qty_list = []
    for el in range(str.__len__()):

        if 0 < str[el].ist.find("->") < str[el].ist.find(":"):
            if str[el].ist.find(pt1) >-1 and str[el].ist.find(pt2) > -1:
                if str[el].ist not in ist_list:
                    ist_list.append(str[el].ist)
                    qty_list.append(1)
                else:
                    qty_list[ist_list.index(str[el].ist)] += 1

    maxid = max_id(str)
    mu_id = []
    demu_id = []
    for el in range(ist_list.__len__()):
        new.append(node(maxid, "MULTIPLEXER"))
        mu_id.append(maxid)
        maxid += 1
        new.append(node(maxid, "DEMULTIPLEXER"))
        demu_id.append(maxid)

    for el in range(str.__len__()):
        if str[el].ist not in ist_list:                                                                                 # non è l'istruzione del multi
            if str[el].next_node.__len__() > 0:
                for ele in range(str[el].next_node.__len__()):
                    idz = search_node(str, str[el].next_node[ele])
                    new_next = []
                    if str[idz].ist in ist_list:                                                                        # ma un suo next_node si
                        what_multi = ist_list.index(str[idz].ist)
                        new_next.append(mu_id[what_multi])
                        new[search_node(new, mu_id[what_multi])].next_node.append(str[el].next_node[ele])
                    else:                                                                                               # e neanche il suo next_node
                        new_next.append(str[el].next_node[ele])

                    new.append(node(str[el].id, str[el].ist))
                    for n in range(new_next.__len__()):
                        new[-1].next_node.append(new_next[n])
            else:
                new.append(node(str[el].id, str[el].ist))
                for n in range(str[el].next_node.__len__()):
                    new[-1].next_node.append(str[el].next_node[n])

        elif str[el].ist in ist_list:                                                                                   # è l'istruzione che va nel multi
            what_multi = ist_list.index(str[el].ist)
            out = str[el].next_node
            new.append(node(str[el].id, str[el].ist, demu_id[what_multi - 1]))
            for ele in range(out.__len__()):
                new[search_node(new, demu_id[what_multi])].next_node.append(out[ele])

    draw_graph(new, "new-prova")
    return new
