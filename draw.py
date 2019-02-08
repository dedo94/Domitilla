from graphviz import Digraph


def draw_graph(struct, name):
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

    path = open("path.txt", 'r')
    for line in path:
        line = line.strip()
    g.view(name, line, False)                                                                                           # disegno il grafo
