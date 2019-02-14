from graphviz import Digraph
import os
from os.path import relpath


class node:
    def __init__(self, id, istruction, *nxt_node):
        self.id = id
        self.ist = istruction
        self.next_node = []
        for i in nxt_node:
            self.next_node.append(i)
        if str(istruction).count("->") == str(istruction).count(":") == 1:                                              # se contiene le informazioni nel formato richiesto le separo
            strz = str(istruction).split("->")                                                                          # analizzo istruction e la divido in
            self.snd = strz[0].strip()                                                                                  # mittente
            strz = strz[1].split(":")
            self.recv = strz[0].strip()                                                                                 # destinatario
            self.msg = strz[1].strip()                                                                                  # messaggio
        else:
            self.snd = self.recv = self.msg = "null"


def pathfy(filepath):
    prgpath = os.path.dirname(os.path.abspath(__file__))
    pathz = relpath(filepath, prgpath)
    return pathz


def draw_graph(struct, name):
    pathsave = open("path.txt", 'r')
    for line in pathsave:
        pathsave = str(line)
    g = Digraph(name, filename=name)                                                                                   # inizializzo il disegno del grafo

    for x in range(struct.__len__()):                                                                                   # rileggo la struttura e do i comandi per disegnare il grafo
        id_node = struct[x].id
        ist_node = struct[x].ist
        next_node_id = struct[x].next_node

        if ist_node == "start":
            g.node(str(id_node), label="", shape="circle")

        elif ist_node == "end":
            g.node(str(id_node), label="", shape="doublecircle")

        elif ist_node == "+":
            g.node(str(id_node), label="+", shape="diamond")

        elif ist_node == "|":
            g.node(str(id_node), label="|", shape="square")

        else:
            g.node(str(id_node), label=str(ist_node), shape="rect")

        if next_node_id != "null":

            for y in next_node_id:
                g.edge(str(id_node), str(y))
    g.view(name, pathsave, False)                                                                                       # disegno il grafo


def id_to_pos(str_gr, id_node):                                                                                         # data un struttura e un id
    for x in range(str_gr.__len__()):                                                                                   # restituisce la posizione del
        if str_gr[x].id == id_node:                                                                                     # nodo al suoi interno
            return x                                                                                                    # se presente


def ist_to_pos(str_gr, ist):                                                                                            # data un struttura e un istruzione
    for x in range(str_gr.__len__()):                                                                                   # restituisce la posizione del
        if str_gr[x].ist == ist:                                                                                        # nodo al suoi interno
            return x                                                                                                    # se presente


def ist_to_id(str_gr, ist):                                                                                             # data un struttura e un istruzione
    for x in range(str_gr.__len__()):                                                                                   # restituisce l'id  del
        if str_gr[x].ist == ist:                                                                                        # nodo associato
            return str_gr[x].id


def reassign_id(str_gr, start_id):
    new_str_gr = []

    for x in range(str_gr.__len__()):                                                                                   # ciclo tutti i nodi
        if str_gr[x].ist != "start" and str_gr[x].ist != "end":                                                         # se diversi da start e end
            new_str_gr.append(str_gr[x])                                                                                # copio il nodo nella nuova struttura
            new_str_gr[-1].id = int(new_str_gr[-1].id) + start_id                                                       # modifico il suo id
            if str_gr[x].next_node.__len__() > 0:                                                                       # se ho dei next node
                for y in range(str_gr[x].next_node.__len__()):                                                          # li ciclo
                    new_str_gr[-1].next_node[y] = int(new_str_gr[-1].next_node[y]) + start_id                           # e li modifico

        if str_gr[x].ist == "end":                                                                                      # se trovo il nodo di end
            new_str_gr[-1].next_node.clear()                                                                            # modifico il nodo precedente

    return new_str_gr


def prec_node(graph, node_ist):                                                                                         # funzione che restituice i nodi che precedono quello dato
    graph_gr = graph
    pred = []
    id_nodo = -1
    for z in range(graph_gr.__len__()):
        if node_ist == graph_gr[z].ist:
            id_nodo = graph_gr[z].id
    if id_nodo == -1:
        return print("Can't find node in that graph")
    else:
        for x in range(graph_gr.__len__()):
            for y in range(graph_gr[x].next_node.__len__()):
                if graph_gr[x].next_node[y] == id_nodo:
                    pred.append(graph_gr[x].id)
        return pred


def max_id(str_gr):
    max = 0
    for x in range(str_gr.__len__()):
        if int(str_gr[x].id) > max:
            max = int(str_gr[x].id)
    max += 1
    return max


def print_str(struct_gr, space):
    for k in range(struct_gr.__len__()):
        if space == 1:
            print("---")
        print(struct_gr[k].id)
        print(struct_gr[k].ist)
        print(struct_gr[k].next_node)


def find_pos(gr, id):
    for el in range(gr.__len__()):
        if gr[el].id == id:
            return el


'''
A -> H : m 
K -> B : m

'''