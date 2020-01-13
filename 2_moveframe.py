import os
import pickle

def move_frames(kintype):

    train_ls = '/home/wei/Documents/DATA/kinship/Nemo/label/train_list/{}.pkl'.format(kintype)
    sour_pth = '/home/wei/Documents/DATA/kinship/Nemo/frames'
    tar_pth = '/home/wei/Documents/DATA/kinship/Nemo/kins/frames/{}'.format(kintype)
    with open(train_ls, 'rb') as fp:
        nemo_ls = pickle.load(fp)

    # print(nemo_ls)

    def mk_dir(dir):
        if os.path.exists(dir):
            return
        else:
            os.makedirs(dir)


    def tran_nm(names):
        fm_fd = 'f_'+names.split('-')[0][1:]
        mem_fd = 'm_'+names.split('-')[1]
        trans_nm = fm_fd+'/'+mem_fd
        return trans_nm
    truels = []
    for i in nemo_ls:
        if i[1]==0:
            continue
        truels.append(i)

    for i in truels:
        m1 = i[2]
        m1_pth = os.path.join(tar_pth,m1)
        mk_dir(m1_pth)
        m2 = i[3]
        m2_pth = os.path.join(tar_pth,m2)
        mk_dir(m2_pth)
        m1_sour = tran_nm(m1)
        m2_sour = tran_nm(m2)
        m1_sor = os.path.join(sour_pth,m1_sour)
        m2_sor = os.path.join(sour_pth,m2_sour)
        comm1 = 'cp {}/*.jpg {}'.format(m1_sor,m1_pth)
        comm2 = 'cp {}/*.jpg {}'.format(m2_sor,m2_pth)
        os.system(comm1)
        os.system(comm2)

    print('finish')


move_frames('S-S')


