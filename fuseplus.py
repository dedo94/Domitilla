from dottogr import *
from function import *
from composition import *


cmp = []                                                                                                                # struttura
dot_not_struct("example/prove/composition.gv", "composition.gv", cmp, 0)
n1 = "K"
n2 = "H"
max_id = max_id(cmp)
complex_fus = []                                                                                                        # struttura della fusione
id_pair = []                                                                                                            # id delle coppie
pos_pair = []                                                                                                           # posizione delle coppie nella struttura originale
lab = []                                                                                                                # label
pos_list = []
for el in range(cmp.__len__()):
    if 0 < cmp[el].ist.find("->") < cmp[el].ist.find(":"):
        label1 = cmp[el].ist.split("->")
        sender1 = label1[0].strip()
        label1 = label1[1].split(":")
        # recv1 = label1[0].strip()
        msg1 = label1[1].strip()

        if sender1 == n1:
            for ele in range(cmp.__len__()):
                if 0 < cmp[ele].ist.find("->") < cmp[ele].ist.find(":"):
                    label2 = cmp[ele].ist.split("->")
                    # sender2 = label2[0].strip()
                    label2 = label2[1].split(":")
                    recv2 = label2[0].strip()
                    msg2 = label2[1].strip()
                    if recv2 == n2 and msg1 == msg2:
                        id_pair.append([cmp[el].id, cmp[ele].id])
                        pos_pair.append([el, ele])
                        pos_list.append(el)
                        pos_list.append(ele)
                        lab.append(str(sender1 + " -> " + recv2 + " : " + msg2))

        elif sender1 == n2:
            for ele in range(cmp.__len__()):
                if 0 < cmp[ele].ist.find("->") < cmp[ele].ist.find(":"):
                    label2 = cmp[ele].ist.split("->")
                    # sender2 = label2[0].strip()
                    label2 = label2[1].split(":")
                    recv2 = label2[0].strip()
                    msg2 = label2[1].strip()
                    if recv2 == n1 and msg1 == msg2:
                        id_pair.append([cmp[el].id, cmp[ele].id])
                        pos_pair.append([el, ele])
                        pos_list.append(el)
                        pos_list.append(ele)
                        lab.append(str(sender1 + " -> " + recv2 + " : " + msg2))
print("label:")
print(lab)
print("id_pair:")
print(id_pair)
print("pos_pair:")
print(pos_pair)
print("pos_list:")
print(pos_list)
spider = []
mod_list = []
spider_pos = []
for el in range(pos_pair.__len__()):
    spider.append(node(max_id, lab[el]))
    spider_pos.append(spider.__len__() - 1)
    print(spider.__len__())
    tmp = max_id
    max_id += 1
    if pos_pair[el][0] not in mod_list:
        spider.append(node(cmp[pos_pair[el][0]].id, "+", tmp))
        spider.append(node(max_id, "+", cmp[pos_pair[el][0]].next_node[0]))
        spider[spider_pos[-1]].next_node.append(max_id)
        max_id += 1
    else:
        # cercare nodo e aggiungere tmp ai suoi next_node
        pass
    if pos_pair[el][1] not in mod_list:
        spider.append(node(cmp[pos_pair[el][1]].id, "+", tmp))
        spider.append(node(max_id, "+", cmp[pos_pair[el][1]].next_node[0]))
        spider[spider_pos[-1]].next_node.append(max_id)
        max_id += 1
    else:
        # cercare nodo e aggiungere tmp ai suoi next_node
        pass
draw_graph(spider, "spider")
draw_graph(cmp, "cmp")

tot = []
for el in range(cmp.__len__()):
    if int(cmp[el].id) not in pos_list:
        tot.append(cmp[el])
for el in range(spider.__len__()):
    tot.append(spider[el])
draw_graph(tot, "tot.gv")

