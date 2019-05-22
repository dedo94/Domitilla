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


class MyLabel(Label):
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
    path_file = open("path.txt", 'r')
    for line in path_file:
        path = line.strip()
    path_file.close()
    gr1 = None

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
        path_file = open("path.txt", 'r')
        for line in path_file:
            path = line.strip()
        path_file.close()
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
        path_file = open("path.txt", 'r')
        for line in path_file:
            path = line.strip()
        path_file.close()
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
        path_file = open("path.txt", 'r')
        for line in path_file:
            path = line.strip()
        path_file.close()
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
        path_file = open("path.txt", 'r')
        for line in path_file:
            path = line.strip()
        path_file.close()
        if self.ids.save_path.text == path or self.ids.save_path.text == "folder":
            pass
        else:
            f = open("path.txt", 'w')
            f.write(self.ids.save_path.text)
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
        if name1.find(".gv") == name1.__len__() - 3:
            a1 = []
            dot_not_struct(name1, "draw1.gv", a1, 1)
        elif name1.find(".txt") == name1.__len__() - 4:
            a2 = []
            struct_gr(name1, "draw1.gv", a2, 1)
        elif name1 == "file1" or name1 == "file 1 missing" or \
                    name1 == "Unsupported file" or name1 == "select Unstructured graph":
            self.ids.gr_1.text = "file1"
            self.ids.gr_1.color = 255, 255, 255, 1
        else:
            self.ids.gr_2.text = "Unsupported file"
            self.ids.gr_2.color = 125, 0, 0, 1

        name2 = self.ids.gr_2.text
        if name2.find(".gv") == name2.__len__() - 3:
            b1 = []
            dot_not_struct(name2, "draw2.gv", b1, 1)
        elif name2.find(".txt") == name2.__len__() - 4:
            b2 = []
            struct_gr(name2, "draw2.gv", b2, 1)
        elif name2 == "file2" or name2 == "file 2 missing" or \
                    name2 == "Unsupported file" or name2 == "select Unstructured graph":
            self.ids.gr_2.text = "file2"
            self.ids.gr_2.color = 255, 255, 255, 1
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
        for line in path_file:
            path = line.strip()
        path_file.close()
        name1 = self.ids.gr_1.text
        a = []
        if name1.find(".gv") == name1.__len__() - 3:
            dot_not_struct(name1, "draw1.gv", a, 0)
            petri2(name1, "petri1", a, path)
        elif name1.find(".txt") == name1.__len__() - 4:
            struct_gr(name1, "draw1.gv", a, 0)
            petri2(name1, "petri1", a, path)
        elif name1 == "file1" or name1 == "file 1 missing" or \
                    name1 == "Unsupported file" or name1 == "select Unstructured graph":
            self.ids.gr_1.text = "file1"
            self.ids.gr_1.color = 255, 255, 255, 1
        else:
            self.ids.gr_1.text = "Unsupported file"
            self.ids.gr_1.color = 125, 0, 0, 1

        name2 = self.ids.gr_2.text
        b = []
        if name2.find(".gv") == name1.__len__() - 3:
            petri2(name2, "draw2", b, path)
        elif name2.find(".txt") == name1.__len__() - 4:
            struct_gr(name2, "draw2.gv", b, 0)
            petri2(name2, "petri2", b, path)
        elif name2 == "file2" or name2 == "file 2 missing" or \
                    name2 == "Unsupported file" or name2 == "select Unstructured graph":
            self.ids.gr_2.text = "file2"
            self.ids.gr_2.color = 255, 255, 255, 1
        else:
            self.ids.gr_1.text = "Unsupported file"
            self.ids.gr_1.color = 125, 0, 0, 1

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

