# Genera un file contenete un grafo in formato petri net esegiubile all'interno del tool TINA
from function import *


nomi = ["ch1", "ch2", "pl1", "fus_str_err"]
r = 3


def petri_net(path, nome_grafo, gr_str, save):
    to_struct(path, gr_str)                                                                                             # genero a struttura
    namefile = nome_grafo
    ord_vis = []                                                                                                        # array per l'ordine di visita (id)
    order3(gr_str, ord_vis, 0, 0)                                                                                       # genero l'ordine di visita
    writetxt = []                                                                                                       # array che contiene le stringhe per scrivere .ndr
    p_count = 0                                                                                                         # contatore piazze
    t_count = 0                                                                                                         # contatore transizioni
    token = 1                                                                                                           # token
    t_list = []
    p_list = []
    y_coord = 50
    for d in range(ord_vis.__len__()):
        x_coord = 50
        nodo_now = ord_vis[d]                                                                                           # nodo da analizzare
        r_n_n = search_node(gr_str, nodo_now)                                                                           # dove nodo_now si trova in gr_str
        cost = check_situation(gr_str, nodo_now)
        if what_im(gr_str, nodo_now) == "start":                                                                        # se è start
            p_list.append(p_count)
            string = "p " + str(x_coord) + " " + str(y_coord) + ".0 p" + str(p_list[-1]) + " " + str(token) + " " + cost     # riempo la stringa con una paizza
            y_coord += 50
            p_count += 1
            token *= 0
            writetxt.append(string)                                                                                     # e la salvo nell'array

        elif what_im(gr_str, nodo_now) == "istruction":                                                                 # se è un istruzione
            t_list.append(t_count)
            string = "t " + str(x_coord) + " " + str(y_coord) + " t" + str(t_list[-1]) + \
                     " c 0 w n {" + str(gr_str[r_n_n].label) + "} e"                                                    # riempo la stringa con una transizione
            y_coord += 50
            x_coord += 100
            t_count += 1
            writetxt.append(string)

            string = "e p" + str(p_list.pop(0)) + " t" + str(t_list[0]) + " 1 n"                                        # riempo la stringa con un arco
            writetxt.append(string)                                                                                     # e la salvo nell'array

            p_list.append(p_count)
            string = "p " + str(x_coord) + " " + str(y_coord) + " p" + str(p_list[-1]) + " " + str(token) + " " + cost          # riempo la stringa con una paizza
            y_coord += 50
            x_coord += 100
            p_count += 1
            token *= 0
            writetxt.append(string)                                                                                     # e la salvo nell'array

            string = "e t" + str(t_list.pop(0)) + " p" + str(p_list[-1]) + " 1 n"                                       # riempo la stringa con un arco
            writetxt.append(string)                                                                                     # e la salvo nell'array

        elif what_im(gr_str, nodo_now) == "open choice":                                                                # se l'inizio di un choice
            tmp_p = str(p_list.pop(0))
            y_coord += 50
            x_coord += 100
            for el in range(gr_str[r_n_n].next_node.__len__()):
                t_list.append(t_count)
                string = "t " + str(x_coord) + " " + str(y_coord) + " t" + str(t_list[-1]) + " 0 w n"                   # riempo la stringa con una transizione
                t_count += 1
                y_coord += 50
                x_coord += 100
                writetxt.append(string)                                                                                 # e la salvo nell'array

                string = "e p" + tmp_p + " t" + str(t_list[0]) + " 1 n"                                                 # riempo la stringa con un arco
                writetxt.append(string)                                                                                 # e la salvo nell'array

                p_list.append(p_count)
                string = "p " + str(x_coord) + " " + str(y_coord) + " p" + str(p_list[-1]) + " " + str(token) + " " + cost      # riempo la stringa con una paizza
                y_coord += 50
                x_coord += 100
                p_count += 1
                token *= 0
                writetxt.append(string)                                                                                 # e la salvo nell'array

                string = "e t" + str(t_list.pop(0)) + " p" + str(p_list[-1]) + " 1 n"                                   # riempo la stringa con un arco
                writetxt.append(string)                                                                                 # e la salvo nell'array

        elif what_im(gr_str, nodo_now) == "open parallel":                                                              # se l'inizio di un parallelo
            t_list.append(t_count)
            string = "t " + str(x_coord) + " " + str(y_coord) + " t" + str(t_list[-1]) + " 0 w n"                       # riempo la stringa con una transizione
            t_count += 1
            y_coord += 50
            x_coord += 100
            writetxt.append(string)                                                                                     # e la salvo nell'array
            tmp_t = str(t_list.pop(0))

            string = "e p" + str(p_list.pop(0)) + " t" + tmp_t + " 1 n"                                                 # riempo la stringa con un arco
            writetxt.append(string)                                                                                     # e la salvo nell'array

            for el in range(gr_str[r_n_n].next_node.__len__()):
                p_list.append(p_count)
                string = "p " + str(x_coord) + " " + str(y_coord) + " p" + str(p_list[-1]) + " " + str(token) + " " + cost      # riempo la stringa con una paizza
                y_coord += 50
                x_coord += 100
                p_count += 1
                token *= 0
                writetxt.append(string)                                                                                 # e la salvo nell'array

                string = "e t" + tmp_t + " p" + str(p_list[-1]) + " 1 n"                                                # riempo la stringa con un arco
                writetxt.append(string)                                                                                 # e la salvo nell'array

        elif what_im(gr_str, nodo_now) == "close choice":                                                               # se la fine di un choice o di un parallelo

            p_list.append(p_count)
            string = "p " + str(x_coord) + " " + str(y_coord) + " p" + str(p_list[-1]) + " " + str(token) + " " + cost  # riempo la stringa con una paizza
            y_coord += 50
            x_coord += 100
            p_count += 1
            token *= 0
            writetxt.append(string)                                                                                     # e la salvo nell'array

            list_prec = pred(gr_str, nodo_now)
            for elem in range(list_prec.__len__()):
                t_list.append(t_count)
                string = "t " + str(x_coord) + " " + str(y_coord) + " t" + str(t_list[-1]) + " 0 w n"                   # riempo la stringa con una transizione
                y_coord += 50
                x_coord += 100
                t_count += 1
                writetxt.append(string)                                                                                 # e la salvo nell'array

                string = "e p" + str(p_list.pop(0)) + " t" + str(t_list[0]) + " 1 n"                                    # riempo la stringa con un arco
                writetxt.append(string)                                                                                 # e la salvo nell'array

                string = "e t" + str(t_list.pop(0)) + " p" + str(p_list[-1]) + " 1 n"                                   # riempo la stringa con un arco
                writetxt.append(string)                                                                                 # e la salvo nell'array

        elif what_im(gr_str, nodo_now) == "close parallel":                                                             # se la fine di un choice o di un parallelo
            t_list.append(t_count)
            string = "t " + str(x_coord) + " " + str(y_coord) + " t" + str(t_list[-1]) + " 0 w n"                       # riempo la stringa con una transizione
            t_count += 1
            y_coord += 50
            x_coord += 100
            writetxt.append(string)                                                                                     # e la salvo nell'array

            list_prec = pred(gr_str, nodo_now)
            for elem in range(list_prec.__len__()):
                string = "e p" + str(p_list.pop(0)) + " t" + str(t_list[0]) + " 1 n"                                    # riempo la stringa con un arco
                writetxt.append(string)                                                                                 # e la salvo nell'array

            p_list.append(p_count)
            string = "p " + str(x_coord) + " " + str(y_coord) + " p" + str(p_list[-1]) + " " + str(token) + " " + cost          # riempo la stringa con una paizza
            y_coord += 50
            x_coord += 100
            p_count += 1
            token *= 0
            writetxt.append(string)                                                                                     # e la salvo nell'array

            string = "e t" + str(t_list.pop(0)) + " p" + str(p_list[-1]) + " 1 n"                                       # riempo la stringa con un arco
            writetxt.append(string)                                                                                     # e la salvo nell'array

    string = "h " + namefile                                                                                            # riempo la stringa con il nome del file
    writetxt.append(string)                                                                                             # e la salvo nell'array
    new_ndr = open(save + "/" +  namefile + ".ndr", "w")                                                                # creo un nuovo file
    for elem in range(writetxt.__len__()):                                                                              # scrivo gli elementi dell'array
        new_ndr.write(writetxt[elem] + "\n")
    new_ndr.close()                                                                                                     # chiudo il file
