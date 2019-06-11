import os
import platform
import sys
from os.path import relpath
sys.path.append('/usr/local/bin/dot')
sys.path.append('/usr/bin/dot')
from graphviz import Digraph


# struttura dati

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


# definisce il path

def pathfy(filepath):
    prgpath = os.path.dirname(os.path.abspath(__file__))
    pathz = relpath(filepath, prgpath)
    return pathz


# data una struttura dati ed un id, restituisce la sua posizione

def id_to_pos(str_gr, id_node):                                                                                         # data un struttura e un id
    for x in range(str_gr.__len__()):                                                                                   # restituisce la posizione del
        if str_gr[x].id == id_node:                                                                                     # nodo al suoi interno
            return x                                                                                                    # se presente


# data una struttura dati ed una istruzione, restituisce la posizione

def ist_to_pos(str_gr, ist):                                                                                            # data un struttura e un istruzione
    for x in range(str_gr.__len__()):                                                                                   # restituisce la posizione del
        if str_gr[x].ist == ist:                                                                                        # nodo al suoi interno
            return x                                                                                                    # se presente


# data una struttura dati ed una istruzione, restituisce il suo id

def ist_to_id(str_gr, ist):                                                                                             # data un struttura e un istruzione
    for x in range(str_gr.__len__()):                                                                                   # restituisce l'id  del
        if str_gr[x].ist == ist:                                                                                        # nodo associato
            return str_gr[x].id


# data una istruzione ed un numero di partenza, riassegna tutti gli id a partire dal numero dato

def reassign_id(str_gr, start_id):
    new_str_gr = []
    for el in range(str_gr.__len__()):
        if str_gr[el].ist != "start":                                                       # se diversi da start e end
            new_str_gr.append(node(int(str_gr[el].id) + start_id, str_gr[el].ist))
            for ele in range(str_gr[el].next_node.__len__()):
                new_str_gr[-1].next_node.append(int(str_gr[el].next_node[ele]) + start_id)
    return new_str_gr


# data una struttura e una istruzione, restituisce il predecessore

def prec_node(graph, node_ist):                                                                                         # funzione che restituice i nodi che precedono quello dato
    graph_gr = graph
    pred = []
    id_nodo = -1
    for z in range(graph_gr.__len__()):
        if node_ist == graph_gr[z].ist:
            id_nodo = graph_gr[z].id
    if id_nodo == -1:
        print("Can't find node in that graph")
    else:
        for x in range(graph_gr.__len__()):
            for y in range(graph_gr[x].next_node.__len__()):
                if graph_gr[x].next_node[y] == id_nodo:
                    pred.append(graph_gr[x].id)
        return pred


# restituisce l'id massimo contenuto in una struttura

def max_id(str_gr):
    max = 0
    for x in range(str_gr.__len__()):
        if int(str_gr[x].id) > max:
            max = int(str_gr[x].id)
    max += 1
    return max


# stampa una struttura

def print_str(struct_gr, space):
    for k in range(struct_gr.__len__()):
        if space == 1:
            print("---")
        print(struct_gr[k].id)
        print(struct_gr[k].ist)
        print(struct_gr[k].next_node)


# data una struttura ed un id restituisce la posizione

def find_pos(gr, id):
    for el in range(gr.__len__()):
        if int(gr[el].id) == int(id):
            return el
