# file contentente tutte le funzioni di supporto
import random


class Node:                                                                                                             # mi permette di schematizzare un.dot
    def __init__(self, id, label, *nxt_node):
        self.id = id
        self.label = label
        self.next_node = []
        for b in nxt_node:
            self.next_node.append(b)


def rv():                                                                                                               # genera un valore casuale tra 50 e 500
    x = random.randint(50, 500)
    x = str(x)
    x = x + str(".0")
    return x


def search_node(gr_st, id):                                                                                             # data una struttura e un id restituisce
    for el in range(gr_st.__len__()):                                                                                   # la posizione del nodo cercato
        if gr_st[el].id == str(id):
            return el


def st_print_all(struct):                                                                                               # mi permette di stampare tutta la struttura
    for elem in range(struct.__len__()):
        # print(str(elem) + ".")
        print("\n")
        print("id: " + str(struct[elem].id))
        print("label: " + str(struct[elem].label))
        print("next: " + str(struct[elem].next_node))


def st_print_node(struct, n):                                                                                           # mi permette di stampare la struttura di un nodo dato
        i = search_node(struct, n)
        print("id: " + str(struct[i].id))
        print("label: " + str(struct[i].label))
        print("next: " + str(struct[i].next_node))


def to_struct(graph, gr_node):                                                                                          # mi riempe la struttura
    file = open(graph, "r")
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

            gr_node.append(Node(at, label))
    file.close()
    return gr_node


def what_im(gr_st, node):                                                                                               # mi permette di capire cos'è il nodo
    node = search_node(gr_st, node)
    if node >= gr_st.__len__():
        return None
    else:
        ist = gr_st[node].label  # istruzioni dei next node
        n_next = gr_st[node].next_node.__len__()
        if ist == "+":
            if n_next > 1:
                im = "open choice"
            else:
                im = "close choice"
        elif ist == "|":
            if n_next > 1:
                im = "open parallel"
            else:
                im = "close parallel"
        elif ist == "start":
            im = "start"
        elif ist == "end":
            im = "end"
        else:
            im = "istruction"
        return im


def what_next(gr_st, node):                                                                                             # mi permette di capire cos'è il prossimo nodo
    w = search_node(gr_st, node)
    nextn = gr_st[w].next_node
    rest = []
    for el in range(nextn.__len__()):
        res = what_im(gr_st, int(gr_st[w].next_node[el]))
        rest.append(res)
    return rest


def info(gr_str):                                                                                                       # stampo alcuno informazioni
    for i in range(gr_str.__len__()):
        print("-*struct*-")
        st_print_node(gr_str, i)
        print("-*whaaat IM*-")
        print(what_im(gr_str, i))
        print("-*whaaat NEXT*-")
        print(what_next(gr_str, i))


def pred(gr_st, n):                                                                                                     # trova i predecessori
    predec = []
    for el in range(gr_st.__len__()):
        succe = gr_st[el].next_node
        if str(n) in succe:
            predec.append(gr_st[el].id)
    return predec


def order3(gr_st, arr, n, i):
    if 0 not in arr:
        arr.append(0)
    l_next = gr_st[n].next_node
    if l_next.__len__() > 0:
        for x in range(l_next.__len__()):
            if int(l_next[x]) not in arr:
                arr.append(int(l_next[x]))
    if i < arr.__len__():
        k = search_node(gr_st, arr[i])
        order3(gr_st, arr, k, i + 1)


def check_situation(gr_st, node):                                                                                       # in base alla situazione mi ritorna un valore differente
    # now = what_im(gr_st, node)
    later = what_next(gr_st, node)
    last_cost = "n"
    if later.__len__() > 0:
        if later[0] == "end":
            last_cost = "e"
    return last_cost