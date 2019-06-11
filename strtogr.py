from myfunc import *


def struct_gr(path, nome_grafo, struct, draw):
    nome_grf = nome_grafo.split(".")
    file = open(path, 'r')
    gr_node = struct                                                                                                    # array con la struttura dei nodi
    id = 0                                                                                                              # id dei nodi
    set_istruction = 0                                                                                                  # indica se si tratta di un semplice set istruzioni
    case = []                                                                                                           # array dei casi
    gr_node.append(node(id, "start", str(id + 1)))                                                                           # creo il nodo start
    id += 1
    cho_start = []                                                                                                      # id inizio choice
    cho_end = []                                                                                                        # id fine choice
    rec_start = []                                                                                                      # id inizio recursion
    rec_end = []                                                                                                        # id fine recursion1
    par_start = []                                                                                                      # id inizio parallelo
    par_end = []                                                                                                        # id fine parallelo

    for line in file:                                                                                                   # analizzo riga per riga il file
        spl_ist = str(line).split(";")                                                                                  # separo le "istruzioni"

        for el in spl_ist:                                                                                              # analizzo ogni "istruzione"

            if el.count("|{") > 0 and el.strip() == "|{":                                                               # inizio di un parallelo
                case.append("p")                                                                                        # aggiungo caso parallelo
                gr_node.append(node(id, "|", str(id + 1)))                                                                   # creo nodo [|]
                par_start.append(id)                                                                                    # traccio l'id del nodo di inizio del parallelo
                id += 1

            elif el.count("+{") > 0 and el.strip() == "+{":                                                             # inizio di una choice
                case.append("c")                                                                                        # aggiungo caso choice
                cho_start.append(id)                                                                                    # traccio l'id del nodo di inizio della choice
                gr_node.append(node(id, "+", str(id + 2)) )                                                                  # creo il nodo <+> iniziale
                id += 1
                cho_end.append(id)                                                                                      # traccio l'id del nodo di fine della choice
                gr_node.append(node(id, "+"))                                                                           # creo il nodo <+> finale
                id += 1

            elif el.count("*{") > 0 and el.strip() == "*{":                                                             # inizio di una ricorsione
                case.append("r")                                                                                        # aggiungo caso ricorsione
                rec_start.append(id)                                                                                    # traccio l'id del nodo di inizio di ricorsione
                gr_node.append(node(id, "+", str(id + 2)))                                                                   # creo il nodo <+> iniziale
                id += 1
                rec_end.append(id)                                                                                      # traccio l'id del nodo di fine della recursion
                gr_node.append(node(id, "+", str(id - 1)))                                                                   # creo il nodo <+> finale
                id += 1

            elif el.count("+") > 0 and el.strip() == "+":                                                               # nuovo ramo choice
                gr_node[cho_start[-1]].next_node.append(str(id))                                                             # aggiungo un arco uscente dall'inizio della choice

            elif el.count("|") > 0 and el.strip() == "|":                                                               # nuovo ramo parallelo
                if par_start.__len__() != par_end.__len__():                                                            # non ho ancora inserito il nodo di chiusura del parallelo
                    gr_node.append(node(id, "|"))                                                                       # creo nodo [|] finale
                    par_end.append(id)                                                                                  # traccio l'id del nodo di fine del parallelo
                    id += 1

                else:                                                                                                   # altrimenti
                    gr_node[id - 1].next_node[0] = str(par_end[-1])                                                          # modifico l'arco uscente del nodo precedente

                gr_node[par_start[-1]].next_node.append(str(id))                                                             # aggiungo un arco uscente dall'inizio del parallelo

            elif el.count("}") > 0:                                                                                     # treminazione di qualcosa
                if case.__len__() > 0:
                    tmp_case = case[-1]                                                                                 # analizzo l'ultimo caso

                    if tmp_case == "p":                                                                                 # termine di un parallelo
                        gr_node[id - 1].next_node[0] = str(par_end[-1])                                                  # modifico l'arco uscente del nodo precedente
                        gr_node[par_end[-1]].next_node.append(str(id))                                                      # faccio puntare la fine del parallelo al prossimo nodo
                        par_end.pop()                                                                                   # elimino l'ultimo elemento di par_end
                        par_start.pop()                                                                                 # elimino l'ultimo elemento di par_start
                        case.pop()

                    else:                                                                                               # termine di un choice o recursion

                        if el.count("} @") > 0:                                                                         # treminazione indirizzata
                            tmp_el = el.split("@")                                                                      # cerco come indirizzare l'arco uscente dal nodo
                            tmp_el = tmp_el[1].strip()                                                                  # ottengo l'informazione che mi serve
                            gr_node[-1].next_node.pop(-1)
                            if tmp_el == "(o)":                                                                         # break
                                gr_node.append(node(id, "end"))                                                         # creo il nodo (o)
                                id += 1

                            if tmp_el.count("->") == tmp_el.count(":") == 1:                                            # termina in un altro nodo
                                if case[-1] == "r":                                                                     # siamo nel caso di ricorsione
                                    gr_node[rec_end[-1]].next_node.append(str(id))
                                    gr_node[-1].next_node.append(str(rec_end[-1]))

                        elif el.count("}") > 0 and el.strip() == "}" and case[-1] == "c":
                            gr_node[id - 1].next_node[0] = str(cho_end[-1])
                else:
                    gr_node.append(node(id, "end"))                                                                     # siamo alla fine di un grafo

                if set_istruction:                                                                                      # se siamo alla fine di un set di istruzioni
                    set_istruction = 0                                                                                  # cambio la variabile

                elif el.count("}") > 0 and el.strip() == "}" and case.__len__() > 0:                                    # trovata la fine di un set di istruzioni o di choice, ricorsione o parallelo
                    if set_istruction:                                                                                  # se siamo alla fine di una istruzione
                        set_istruction = 0                                                                              # cambio la variabile e non faccio niente

                    else:                                                                                               # altrimenti
                        tmp_case = case[-1]  # analizzo l'ultimo caso
                        if tmp_case == "r":                                                                             # termine di una recursion
                            case.pop()                                                                                  # elimino l'ultimo caso
                            rec_start.pop()                                                                             # elimino gli ultimi id
                            rec_end.pop()
                        if tmp_case == "c":                                                                             # termine di una choice
                            case.pop()                                                                                  # elimino l'ultimo caso
                            cho_start.pop()                                                                             # elimino gli ultimi id
                            tmp_end = cho_end.pop()
                            gr_node[tmp_end].next_node.append(str(id))

                        elif tmp_case == "p":                                                                           # termine di un parallelo
                            gr_node[id - 1].next_node[0] = str(par_end[-1])                                                  # modifico l'arco uscente del nodo precedente
                            case.pop()                                                                                  # elimino l'ultimo caso

            elif el.count("->") == el.count(":") == 1:                                                                  # istruzione
                el = el.strip()

                if el.count("{") > 0:                                                                                   # se trovo l'inizio di un set istruzioni
                    el = el.replace("{", "")                                                                            # rimuovo eventuali parentesi iniziali
                    el = el.strip()                                                                                     # e anche gli spazi vuoti
                    set_istruction = 1                                                                                  # setto la variabile delle istruzioni a vero

                gr_node.append(node(id, str(el), id + 1))                                                               # aggiungo nodo con istruzione
                id += 1
    gr_node.append(node(id, "end"))

    file.close()

    if draw:
        draw_graph(gr_node, nome_grafo)
    return gr_node


