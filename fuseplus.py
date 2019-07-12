from dottogr import *
from function import *
from composition import *


cmp = []                                                                                                                # struttura
dot_not_struct("example/prove/composition.gv", "composition.gv", cmp, 0)
n1 = "K"
n2 = "H"
fus_pair = []                                                                                                           # lista di coppie da fondere


for el in range(cmp.__len__()):
    if 0 < cmp[el].ist.find("->") < cmp[el].ist.find(":"):
        label1 = cmp[el].ist.split("->")
        sender1 = label1[0].strip()
        # label1 = label1[1].split(":")
        # recv1 = label1[0].strip()
        label1 = label1[1].split(":")
        msg1 = label1[1].strip()
        f_p = []                                                                                                        # fuse pair, coppia che andrà fusa
        if sender1 == n1:
            # print(cmp[el].ist)
            f_p.append(cmp[el].ist)
            for ele in range(cmp.__len__()):
                if 0 < cmp[ele].ist.find("->") < cmp[ele].ist.find(":"):
                    label2 = cmp[ele].ist.split("->")
                    # sender2 = label2[0].strip()
                    label2 = label2[1].split(":")
                    recv2 = label2[0].strip()
                    msg2 = label2[1].strip()
                    if recv2 == n2 and msg1 == msg2:
                        # print(cmp[ele].ist)
                        f_p.append(cmp[ele].ist)
        elif sender1 == n2:
            # print(cmp[el].ist)
            f_p.append(cmp[el].ist)
            for ele in range(cmp.__len__()):
                if 0 < cmp[ele].ist.find("->") < cmp[ele].ist.find(":"):
                    label2 = cmp[ele].ist.split("->")
                    # sender2 = label2[0].strip()
                    label2 = label2[1].split(":")
                    recv2 = label2[0].strip()
                    msg2 = label2[1].strip()
                    if recv2 == n1 and msg1 == msg2:
                        # print(cmp[ele].ist)
                        f_p.append(cmp[ele].ist)
        if f_p not in fus_pair:
            if f_p.__len__() > 0:
                fus_pair.append(f_p)
print("coppie:")
print(fus_pair)
new = []
refusion(cmp, "ciao", fus_pair, 1)
