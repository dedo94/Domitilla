# Genera un file contenete un grafo in formato petri net esegiubile all'interno del tool TINA
from function import *


def petri2(path, nome_grafo, gr_str, save):
    to_struct(path, gr_str)                                                                                             # genero la struttura
    namefile = nome_grafo
    petri_st = []
    writetxt = []                                                                                                       # array che contiene le stringhe per scrivere .ndr
    p_c = 0
    t_c = 0
    for t in range(gr_str.__len__()):                                                                                   # creo prima la struttura semivuota
        petri_st.append(Petri2(gr_str[t].id, what_im(gr_str, gr_str[t].id), [], [], [], gr_str[t].ist))

    for el in range(gr_str.__len__()):                                                                                  # la vado poi ad arricchire

        if what_im(gr_str, gr_str[el].id) == "start":
            petri_st[el].pla.append(p_c)
            pos = petripos(petri_st, gr_str[el].next_node[0])
            petri_st[pos].p_in.append(p_c)
            p_c += 1

        elif what_im(gr_str, gr_str[el].id) == "istruction" or what_im(gr_str, gr_str[el].id) == "transition choice":
            petri_st[el].tr.append(t_c)
            t_c += 1
            petri_st[el].pla.append(p_c)
            pos = petripos(petri_st, gr_str[el].next_node[0])
            petri_st[pos].p_in.append(p_c)
            p_c += 1

        elif what_im(gr_str, gr_str[el].id) == "open choice":

            for n in range(gr_str[el].next_node.__len__()):
                petri_st[el].tr.append(t_c)
                t_c += 1
                petri_st[el].pla.append(p_c)
                pos = petripos(petri_st, gr_str[el].next_node[n])
                petri_st[pos].p_in.append(p_c)
                p_c += 1

        elif what_im(gr_str, gr_str[el].id) == "close choice":
            petri_st[el].tr.append(t_c)
            t_c += 1
            petri_st[el].tr.append(t_c)
            t_c += 1
            petri_st[el].pla.append(p_c)
            pos = petripos(petri_st, gr_str[el].next_node[0])
            petri_st[pos].p_in.append(p_c)
            p_c += 1

        elif what_im(gr_str, gr_str[el].id) == "open parallel":
            petri_st[el].tr.append(t_c)
            t_c += 1

            for n in range(gr_str[el].next_node.__len__()):
                petri_st[el].pla.append(p_c)
                pos = petripos(petri_st, gr_str[el].next_node[n])
                petri_st[pos].p_in.append(p_c)
                p_c += 1

        elif what_im(gr_str, gr_str[el].id) == "close parallel":
            petri_st[el].tr.append(t_c)
            t_c += 1
            petri_st[el].pla.append(p_c)
            pos = petripos(petri_st, gr_str[el].next_node[0])
            petri_st[pos].p_in.append(p_c)
            p_c += 1

    y_c = 100

    for x in range(petri_st.__len__()):                                                                                 # terminata la struttura procedo al disegno
        x_c = 100

        if petri_st[x].im == "start":
            write = "p " + str(x_c) + ".0 " + str(y_c) + ".0 p" + str(petri_st[x].pla[0]) + " 1 n"
            y_c += 50
            writetxt.append(write)

        elif petri_st[x].im == "open parallel":
            write = "t " + str(x_c) + ".0 " + str(y_c) + ".0 t" + str(petri_st[x].tr[0]) + " 0 w n"
            y_c += 50
            writetxt.append(write)
            write = "e p" + str(petri_st[x].p_in[0]) + " t" + str(petri_st[x].tr[0]) + " 1 n"
            writetxt.append(write)

            for i in range(petri_st[x].pla.__len__()):
                write = "p " + str(x_c) + ".0 " + str(y_c) + ".0 p" + str(petri_st[x].pla[i]) + " 0 n"
                writetxt.append(write)
                write = "e t" + str(petri_st[x].tr[0]) + " p" + str(petri_st[x].pla[i]) + " 1 n"
                writetxt.append(write)
                x_c += 200
            y_c += 50

        elif petri_st[x].im == "istruction":
            write = "t " + str(x_c) + ".0 " + str(y_c) + ".0 t" + str(petri_st[x].tr[0]) + \
                    " c 0 w n {" + str(petri_st[x].ist) + "} e"
            y_c += 50
            writetxt.append(write)
            write = "e p" + str(petri_st[x].p_in[0]) + " t" + str(petri_st[x].tr[0]) + " 1 n"
            writetxt.append(write)
            write = "p " + str(x_c) + ".0 " + str(y_c) + ".0 p" + str(petri_st[x].pla[0]) + " 0 n"
            writetxt.append(write)
            y_c += 50
            write = "e t" + str(petri_st[x].tr[0]) + " p" + str(petri_st[x].pla[0]) + " 1 n"
            writetxt.append(write)

        elif petri_st[x].im == "open choice":

            for el in range(petri_st[x].tr.__len__()):
                write = "t " + str(x_c) + ".0 " + str(y_c) + ".0 t" + str(petri_st[x].tr[el]) + " 0 w n"
                y_c += 50
                writetxt.append(write)
                write = "e p" + str(petri_st[x].p_in[0]) + " t" + str(petri_st[x].tr[el]) + " 1 n"
                writetxt.append(write)
                write = "p " + str(x_c) + ".0 " + str(y_c) + ".0 p" + str(petri_st[x].pla[el]) + " 0 n"
                y_c += 50
                writetxt.append(write)
                write = "e t" + str(petri_st[x].tr[el]) + " p" + str(petri_st[x].pla[el]) + " 1 n"
                writetxt.append(write)
                x_c += 200

        elif petri_st[x].im == "transition choice":
            write = "t " + str(x_c) + ".0 " + str(y_c) + ".0 t" + str(petri_st[x].tr[0]) + " 0 w n"
            y_c += 50
            writetxt.append(write)
            write = "e p" + str(petri_st[x].p_in[0]) + " t" + str(petri_st[x].tr[0]) + " 1 n"
            writetxt.append(write)
            write = "p " + str(x_c) + ".0 " + str(y_c) + ".0 p" + str(petri_st[x].pla[0]) + " 0 n"
            writetxt.append(write)
            y_c += 50
            write = "e t" + str(petri_st[x].tr[0]) + " p" + str(petri_st[x].pla[0]) + " 1 n"
            writetxt.append(write)

        elif petri_st[x].im == "close choice":
            write = "p " + str(x_c) + ".0 " + str(y_c) + ".0 p" + str(petri_st[x].pla[0]) + " 0 n"
            writetxt.append(write)
            y_c += 50

            for el in range(petri_st[x].tr.__len__()):
                write = "t " + str(x_c) + ".0 " + str(y_c) + ".0 t" + str(petri_st[x].tr[el]) + " 0 w n"
                y_c += 50
                writetxt.append(write)
                write = "e p" + str(petri_st[x].p_in[el]) + " t" + str(petri_st[x].tr[el]) + " 1 n"
                writetxt.append(write)
                write = "e t" + str(petri_st[x].tr[el]) + " p" + str(petri_st[x].pla[0]) + " 1 n"
                writetxt.append(write)

        elif petri_st[x].im == "close parallel":
            write = "t " + str(x_c) + ".0 " + str(y_c) + ".0 t" + str(petri_st[x].tr[0]) + " 0 w n"
            y_c += 50
            writetxt.append(write)
            write = "p " + str(x_c) + ".0 " + str(y_c) + ".0 p" + str(petri_st[x].pla[0]) + " 0 n"
            writetxt.append(write)
            y_c += 50
            write = "e t" + str(petri_st[x].tr[0]) + " p" + str(petri_st[x].pla[0]) + " 1 n"
            writetxt.append(write)

            for el in range(petri_st[x].p_in.__len__()):
                write = "e p" + str(petri_st[x].p_in[el]) + " t" + str(petri_st[x].tr[0]) + " 1 n"
                writetxt.append(write)

    write = "h " + namefile
    writetxt.append(write)
    new_ndr = open(save + "/" + namefile + ".ndr", "w")

    for elem in range(writetxt.__len__()):
        if writetxt[elem][0] != "e":
            new_ndr.write(writetxt[elem] + "\n")
    for elem in range(writetxt.__len__()):
        if writetxt[elem][0] == "e":
            new_ndr.write(writetxt[elem] + "\n")

    new_ndr.close()

