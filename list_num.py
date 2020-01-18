import os

pth = '/home/wei/Documents/DATA/kinship/Nemo/kins/frames'

kin_ls = sorted(os.listdir(pth))
kin_num_dic = {}



def clean_ls(ls):
    ls_ = []
    for ims in ls:
        if ims.endswith('.jpg'):
            ls_.append(ims)
    return ls_

small_name = 500
small_ls = []
for ki in kin_ls:
    kin_pth = os.path.join(pth,ki)
    k_nms = sorted(os.listdir(kin_pth))
    ls = []
    for nm in k_nms:
        mem_pth = os.path.join(kin_pth,nm)
        imgs = os.listdir(mem_pth)
        num = len(clean_ls(imgs))
        if num<=small_name:
            small_name = num
            small_ls = (ki,nm,num)

        ls.append((nm, num))
    kin_num_dic[ki] = ls

print(kin_num_dic)
print(small_ls)