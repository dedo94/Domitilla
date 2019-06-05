import kivy
import platform
import shlex
import subprocess

from strtogr import *
from convert import *
from composition import *

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserIconView, FileChooserListView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from functools import partial

kivy.require('1.10.1')


class MyLabel(Label):
    pass


class MyNavBar(GridLayout):
    pass


class MyHelp(AnchorLayout):
    pass


class MyFolderChooser(BoxLayout):
    pass


class MyFileChooser(BoxLayout):
    pass


class UnStBtn(BoxLayout):
    pass


class MyTxt(TextInput):
    pass


class SaveName(BoxLayout):
    pass


class MyBtnBar(BoxLayout):
    pass


class MyLayout(BoxLayout):
    print(kivy.__version__)

    def pathfy(self):
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
        # per Linux
        if platform.system() == "Linux":
            path = paths[1]
        return path

    def clear(self):
        self.ids.gr_1.text = "file1"
        self.ids.gr_1.color = 51, 51, 51, 1
        self.ids.gr_2.text = "file2"
        self.ids.gr_2.color = 51, 51, 51, 1
        self.ids.gr_1.save_path = "folder"
        self.ids.gr_2.save_path = 51, 51, 51, 1
        self.ids.fuse_area.text = "Insert each pair of nodes in a different row.\nExample:\nA -> H : m ; K -> B : m"
        self.ids.save_name.text = "prova"

    def load(self, path, selection):
        # print path
        # print selection
        pass

    def load_from_filechooser(self, filechooser, option):
        try:
            self.load(filechooser.path, filechooser.selection)
            self.ids.save_path.text = filechooser.selection[0]
        except:
            pass

    def save_path(self, obj):
        path = self.pathfy()
        layout = BoxLayout(orientation='vertical')
        filechooser = FileChooserIconView(path=path, dirselect=True)
        btn = Button(size_hint_y=None, text="OK")
        btn.bind(on_press=partial(self.load_from_filechooser, filechooser))
        layout.add_widget(filechooser)
        layout.add_widget(btn)
        popup = Popup(title="save folder", content=layout, size_hint=(0.9, 0.9))
        popup.open()
        btn.bind(on_release=popup.dismiss)

    def load_from_filechooser2(self, filechooser, option):
        try:
            self.load(filechooser.path, filechooser.selection)
            self.ids.gr_1.text = filechooser.selection[0]
        except:
            pass

    def gr_1(self, obj):
        self.overwrite_path()
        path = self.pathfy()
        layout = BoxLayout(orientation='vertical')
        filechooser = FileChooserIconView(path=path, dirselect=False)
        btn = Button(size_hint_y=None, text="OK")
        btn.bind(on_press=partial(self.load_from_filechooser2, filechooser))
        layout.add_widget(filechooser)
        layout.add_widget(btn)
        popup = Popup(title="first graph", content=layout, size_hint=(0.9, 0.9))
        popup.open()
        btn.bind(on_release=popup.dismiss)

    def load_from_filechooser3(self, filechooser, option):
        try:
            self.load(filechooser.path, filechooser.selection)
            self.ids.gr_2.text = filechooser.selection[0]
        except:
            pass

    def gr_2(self, obj):
        self.overwrite_path()
        path = self.pathfy()
        layout = BoxLayout(orientation='vertical')
        filechooser = FileChooserIconView(path=path, dirselect=False)
        btn = Button(size_hint_y=None, text="OK")
        btn.bind(on_press=partial(self.load_from_filechooser3, filechooser))
        layout.add_widget(filechooser)
        layout.add_widget(btn)
        popup = Popup(title="second graph", content=layout, size_hint=(0.9, 0.9))
        popup.open()
        btn.bind(on_release=popup.dismiss)

    def overwrite_path(self):
        path = self.pathfy()
        paths = []
        if self.ids.save_path.text == path or self.ids.save_path.text == "folder":
            pass
        else:
            # per Windows
            if platform.system() == "Windows":
                pass
            # per macOs
            if platform.system() == "Darwin":
                paths.append(self.ids.save_path.text)
                paths.append("home/")
            # per Linux
            if platform.system() == "Linux":
                paths.append("/Users")
                paths.append(self.ids.save_path.text)
            f = open("path.txt", 'w')
            for pth in range(paths.__len__()):
                f.write(paths[pth] + "\n")
            f.close()
        self.ids.save_path.text = "folder"

    def compose(self):
        name1 = self.ids.gr_1.text
        name2 = self.ids.gr_2.text
        if name1.find(".gv") == name1.__len__() - 3 and name2.find(".gv") == name2.__len__() - 3:
            composition(name1, name2, self.ids.save_name.text, 1)

        else:
            if name1 == "file1" or name1 == "file 1 missing" or \
                    name1 == "Unsupported file" or name1 == "select Unstructured graph":
                self.ids.gr_1.text = "file 1 missing"
                self.ids.gr_1.color = 125, 0, 0, 1
            elif name1.find(".gv") < name1.__len__() - 3:
                self.ids.gr_1.text = "Unsupported file"
                self.ids.gr_1.color = 125, 0, 0, 1
            if name2 == "file2" or name2 == "file 2 missing" or \
                    name2 == "Unsupported file" or name2 == "select Unstructured graph":
                self.ids.gr_2.text = "file 2 missing"
                self.ids.gr_2.color = 125, 0, 0, 1
            elif name2.find(".gv") < name1.__len__() - 3:
                self.ids.gr_2.text = "Unsupported file"
                self.ids.gr_2.color = 125, 0, 0, 1

        self.overwrite_path()

    def draw(self):
        name1 = self.ids.gr_1.text
        draw1 = name1.split("/")
        draw1 = draw1[-1].split(".")
        if name1.find(".gv") == name1.__len__() - 3:
            a1 = []
            dot_not_struct(name1, draw1[0] + ".gv", a1, 1)
        elif name1.find(".txt") == name1.__len__() - 4:
            a2 = []
            struct_gr(name1, draw1[0] + ".gv", a2, 1)
        elif name1 == "file1" or name1 == "file 1 missing" or \
                    name1 == "Unsupported file" or name1 == "select Unstructured graph":
            self.ids.gr_1.text = "file1"
            self.ids.gr_1.color = 51, 51, 51, 1
        else:
            self.ids.gr_2.text = "Unsupported file"
            self.ids.gr_2.color = 125, 0, 0, 1

        name2 = self.ids.gr_2.text
        draw2 = name2.split("/")
        draw2 = draw2[-1].split(".")
        if name2.find(".gv") == name2.__len__() - 3:
            b1 = []
            dot_not_struct(name2, draw2[0] + ".gv", b1, 1)
        elif name2.find(".txt") == name2.__len__() - 4:
            b2 = []
            struct_gr(name2, draw2[0] + ".gv", b2, 1)
        elif name2 == "file2" or name2 == "file 2 missing" or \
                    name2 == "Unsupported file" or name2 == "select Unstructured graph":
            self.ids.gr_2.text = "file2"
            self.ids.gr_2.color = 51, 51, 51, 1
        else:
            self.ids.gr_2.text = "Unsupported file"
            self.ids.gr_2.color = 125, 0, 0, 1

        self.overwrite_path()

    def fuse(self):
        name1 = self.ids.gr_1.text
        name2 = self.ids.gr_2.text
        node_str = self.ids.fuse_area.text
        nf = []                                                                                                         # lista con le coppie di label da fondere
        nfline = node_str.split("\n")
        for el in range(nfline.__len__()):
            if nfline[el].count(";"):
                couple = nfline[el].split(";")
                a = couple[0].strip()                                                                                   # primo label
                b = couple[1].strip()                                                                                   # secondo label
                if a.count("->") == b.count("->") == 1 and a.count(":") == b.count(":") == 1:
                    cpl = [a, b]                                                                                        # coppia dei label
                    nf.append(cpl)                                                                                      # la aggiungo alla lista
        if name1.find(".gv") == name1.__len__() - 3 and name2.find(".gv") == name2.__len__() - 3:
            comp = composition(name1, name2, self.ids.save_name.text, 0)
            refusion(comp, self.ids.save_name.text, nf, 1)
        else:
            if name1 == "file1":
                self.ids.gr_1.text = "select Unstructured graph"
                self.ids.gr_1.color = 125, 0, 0, 1
            elif name1.find(".gv") < 0:
                self.ids.gr_1.text = "Unsupported file"
                self.ids.gr_1.color = 125, 0, 0, 1
            if name2 == "file2":
                self.ids.gr_2.text = "select Unstructured graph"
                self.ids.gr_2.color = 125, 0, 0, 1
            elif name2.find(".gv") < 0:
                self.ids.gr_2.text = "Unsupported file"
                self.ids.gr_2.color = 125, 0, 0, 1

        self.overwrite_path()

    def petri(self):
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
        # per Linux
        if platform.system() == "Linux":
            path = paths[1]

        name1 = self.ids.gr_1.text
        namea = name1.split("/")
        namea = namea[-1].split(".")
        namea = namea[0]
        a = []
        if name1.find(".gv") == name1.__len__() - 3:
            dot_not_struct(name1, namea + ".gv", a, 0)
            print(type(a[0].next_node[0]))

            for el in range(a.__len__()):
                print(a[el].id)
                print(a[el].ist)
                print(a[el].next_node)

            petri2(name1, namea, a, path)
        elif name1.find(".txt") == name1.__len__() - 4:
            struct_gr(name1, namea, a, 0)
            petri2(name1, namea, a, path)
        elif name1 == "file1" or name1 == "file 1 missing" or \
                name1 == "Unsupported file" or name1 == "select Unstructured graph":
            self.ids.gr_1.text = "file1"
            self.ids.gr_1.color = 51, 51, 51, 1
        else:
            self.ids.gr_1.text = "Unsupported file"
            self.ids.gr_1.color = 125, 0, 0, 1

        print()

        name2 = self.ids.gr_2.text
        nameb = name2.split("/")
        nameb = nameb[-1].split(".")
        nameb = nameb[0]
        b = []
        if name2.find(".gv") == name2.__len__() - 3:
            petri2(name2, nameb, b, path)
        elif name2.find(".txt") == name2.__len__() - 4:
            struct_gr(name2, nameb, b, 0)
            print(type(b[0].next_node[0]))
            for el in range(b.__len__()):
                print(b[el].id)
                print(b[el].ist)
                print(b[el].next_node)

            petri2(name2, nameb, b, path)
        elif name2 == "file2" or name2 == "file 2 missing" or \
                name2 == "Unsupported file" or name2 == "select Unstructured graph":
            self.ids.gr_2.text = "file2"
            self.ids.gr_2.color = 51, 51, 51, 1
        else:
            self.ids.gr_2.text = "Unsupported file"
            self.ids.gr_2.color = 125, 0, 0, 1

        self.overwrite_path()

    def help(self):
        file = "guide.pdf"
        # per windows
        if platform.system() == "Windows":
            os.system("start " + file)
        # per macOs
        if platform.system() == "Darwin":
            os.system("open " + shlex.quote(file))
        # per Linux
        if platform.system() == "Linux":
            path = os.getcwd()
            path = path + "/" + file
            subprocess.call(("xdg-open", path))


class Domitilla(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    Domitilla().run()

