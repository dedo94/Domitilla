from draw import *
from myfunc import *


# permette di riempire la struttura dati partendo da un grafo non strutturato

def dot_not_struct(path, nome_grafo, struct, draw):

    file = open(path, "r")
    gr_node = struct                                                                                                    # array con la struttura dei nodi
    nome_grf = nome_grafo.split(".")
    for line in file:

        if line.count("->") == 1 and line.count("label") == 0:                                                          # archi
            line = line.split("->")
            at = line[0].strip()                                                                                        # nodo attuale
            dest = line[1].strip()                                                                                      # nodo destinazione
            for el in range(gr_node.__len__()):
                if gr_node[el].id == at:
                    gr_node[el].next_node.append(dest)

        elif line.count('label="'):
            at = line.split("[")
            at = at[0].strip()                                                                                          # nuovo nodo
            cut = line.find("label=") + 7
            label = line[cut:]
            cut2 = label.find('"')
            label = label[:cut2]                                                                                        # label estratto

            if label.__len__() == 0 and line.find("shape=doublecircle") > 0:
                label = "end"

            if label.__len__() == 0 and line.find("shape=circle") > 0:
                label = "start"

            gr_node.append(node(at, label))

    file.close()

    if draw:
        draw_graph(gr_node, nome_grafo)
    return gr_node
