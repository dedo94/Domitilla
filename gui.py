import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages')
import PySimpleGUI as sg
from composition import *
from convert import *
from strtogr import *


def execute():
    path = "Browse..."
    pathtxt = open("path.txt", 'r')
    for line in pathtxt:                                                                                                # cerco il path di salvataggio
        path = line.strip()
    pathtxt.close()

    layout = [                                                                                                          # inizio layout grafico
        [sg.Text('Choose the folder to save the files:', size=(35, 1))],
        [sg.InputText(path), sg.FolderBrowse(key='_folder_')],
        [sg.Text('_' * 65)],
        [sg.Text("FIRST GRAPH:", size=(20, 1)), sg.Radio('Unstructured', "R1", default=True, key='_r1_'),
         sg.Radio('Structured', "R1")],
        [sg.Text("Select graph", size=(45, 1)), sg.FileBrowse(key='_gr1_')],
        [sg.Text('_' * 65)],
        [sg.Text("SECOND GRAPH:", size=(20, 1)), sg.Radio('Unstructured', "R2", default=True, key='_r2_'),
         sg.Radio('Structured', "R2")],
        [sg.Text("Select graph", size=(45, 1)), sg.FileBrowse(key='_gr2_')],
        [sg.Text('_' * 65)],
        [sg.Text("Insert fusion node here. Every line MUST contain one node.", size=(60, 1))],
        [sg.Multiline(size=(60, 3), key='_fn_')],
        [sg.Text('_' * 65)],
        [sg.Text("Save name:", size=(15, 1)), sg.InputText("Example", key='_sname_')],
        [sg.Submit("Compose", key='_comp_'), sg.Submit("Fuse", key='_fuse_'),
         sg.Submit("Draw", key='_draw_'), sg.Submit("PetriNet", key='_petri_'), sg.Cancel()]

    ]

    window = sg.Window('DOMITILLA').Layout(layout)
    button, values = window.Read()                                                                                      # fine layout grafico

    if path != values['_folder_'].count("/") > 0:                                                                       # se il path è cambiato lo salvo
        pathtxt = open("path.txt", 'w')
        pathtxt.write(values['_folder_'])
        pathtxt.close()

    if button == "Cancel":
        print("Cancel")

    elif button == "_draw_":
        if values['_gr1_'].count("/") > 0:
            drstr1 = []
            if values['_r1_'] is True:
                dot_not_struct(pathfy(values['_gr1_']), "draw1.gv", drstr1, 1)
            else:
                struct_gr(pathfy(values['_gr1_']), "draw1.gv", drstr1, 1)

        if values['_gr2_'].count("/") > 0:
            drstr2 = []
            if values['_r2_'] is True:
                dot_not_struct(pathfy(values['_gr2_']), "draw2.gv", drstr2, 1)
            else:
                struct_gr(pathfy(values['_gr2_']), "draw2.gv", drstr2, 1)

    elif button == "_petri_":
        if values['_gr1_'].count("/") > 0:
            drstr1 = []
            if values['_r1_'] is True:
                petri2(pathfy(values['_gr1_']), "petri1", drstr1, path)
            else:
                print("Please insert unstructured graph")

        if values['_gr2_'].count("/") > 0:
            drstr2 = []
            if values['_r2_'] is True:
                petri2(pathfy(values['_gr2_']), "petri2", drstr2, path)
            else:
                print("Please insert unstructured graph")

    elif button == "_comp_":
            composition(pathfy(values['_gr1_']), pathfy(values['_gr2_']), values['_sname_'], 1)

    elif button == "_fuse_":
        nf = []
        if values['_gr1_'].count("/") > 0 and values['_gr2_'].count("/") > 0:

            nfx = values['_fn_'].split("\n")
            for el in range(nfx.__len__()):
                if nfx[el].count("->") == 1 and nfx[el].count(":") == 1:
                    if nfx[el].strip() not in nf:
                        nf.append(nfx[el].strip())
            gr = composition(pathfy(values['_gr1_']), pathfy(values['_gr2_']), values['_sname_'], 0)
            refusion(gr, values['_sname_'], nf, 1)

        elif values['_gr1_'].count("/") > 0 and values['_gr2_'].count("/") == 0:                                        # primo grafo

            nfx = values['_fn1_'].split("\n")
            for el in range(nfx.__len__()):
                if nfx[el].count("->") == 1 and nfx[el].count(":") == 1:
                    if nfx[el].strip() not in nf:
                        nf.append(nfx[el].strip())

            st = []
            st = dot_not_struct(pathfy(values['_gr1_']), values['_sname_'], st, 0)
            refusion(st, values['_sname_'], nf, 1)

        elif values['_gr2_'].count("/") > 0 and values['_gr1_'].count("/") == 0:                                        # secondo grafo

            nfx = values['_fn2_'].split("\n")
            for el in range(nfx.__len__()):
                if nfx[el].count("->") == 1 and nfx[el].count(":") == 1:
                    if nfx[el].strip() not in nf:
                        nf.append(nfx[el].strip())

            st = []
            dot_not_struct(pathfy(values['_gr2_']), values['_sname_'], st, 0)
            refusion(st, values['_sname_'], nf, 1)


execute()
