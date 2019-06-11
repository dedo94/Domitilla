import platform

from graphviz import Digraph


def draw_graph(struct, name):
    g_name = name.split(".")
    g = Digraph(name, filename=name)                                                                               # inizializzo il disegno del grafo
    print(name)
    print(g_name[0])
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

    path_file = open("path.txt", 'r')
    paths = []
    for line in path_file:
        paths.append(line.strip())
    path_file.close()
    # per Windows
    if platform.system() == "Windows":
        pass
    # per macOs
    if platform.system() == "Darwin":
        path = paths[0]
        print("diohane")
    # per Linux
    if platform.system() == "Linux":
        path = paths[1]
    g.view(g_name[0], path, False)                                                                                      # disegno il grafo


