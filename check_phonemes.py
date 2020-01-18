import csv
import os
import matplotlib.pyplot as plt

phones = ['AA0', 'AA1', 'AA2', 'AE0', 'AE1', 'AE2', 'AH0', 'AH1', 'AH2', 'AO0', 'AO1', 'AO2',
           'AW0', 'AW1', 'AW2', 'AY0', 'AY1', 'AY2', 'EH0', 'EH1', 'EH2', 'ER0', 'ER1', 'ER2',
           'EY0', 'EY1', 'EY2', 'IH0', 'IH1', 'IH2', 'IY0', 'IY1', 'IY2', 'OW0', 'OW1', 'OW2',
           'OY0', 'OY1', 'OY2', 'UH0', 'UH1', 'UH2', 'UW0', 'UW1', 'UW2',
           'B', 'CH', 'D', 'DH', 'F', 'G', 'HH', 'JH', 'K', 'L', 'M', 'N', 'NG', 'P', 'R',
           'S', 'SH', 'T', 'TH', 'V', 'W', 'Y', 'Z', 'ZH']



phone_cout_dict = {}
for p in phones:
    phone_cout_dict[p]=0


def count_phone(dicts,cuts):

    for p in dicts:
        if p in cuts:
            dicts[p] = dicts[p]+1



root_pth = '/home/wei/Documents/DATA/kinship/speech/label'
eng_pth = '/home/wei/Documents/DATA/kinship/speech/eng/cuts'
dutch_pth = '/home/wei/Documents/DATA/kinship/speech/dutch-eng/cuts'

mem_ls = []
with open('/home/wei/Documents/DATA/kinship/Nemo/label/kin_simple.csv') as ff:
    reader = csv.reader(ff, delimiter=',')
    for it in reader:
        mem_ls.append(it[0])

print(mem_ls)
en_l = sorted(os.listdir(eng_pth))
du_l = sorted(os.listdir(dutch_pth))
for mem in mem_ls:
    two_ls = []
    cuts_phones = []
    for e in en_l:
        if e.startswith(mem):
            two_ls.append(e)
    for fd in two_ls:
        mpth = os.path.join(eng_pth,fd)
        cuts_ls = os.listdir(mpth)
        cuts_phones = cuts_phones+ [m.split('_')[-1].split('.')[0] for m in cuts_ls]

    count_phone(phone_cout_dict, cuts_phones)

    two_ls = []
    cuts_phones = []
    for e in du_l:
        if e.startswith(mem):
            two_ls.append(e)
    for fd in two_ls:
        mpth = os.path.join(eng_pth, fd)
        try:
            cuts_ls = os.listdir(mpth)
        except:
            continue
        cuts_phones = cuts_phones + [m.split('_')[-1].split('.')[0] for m in cuts_ls]

    count_phone(phone_cout_dict, cuts_phones)



print(phone_cout_dict)

hist_nm = ['all']
hist_nu = [253]
for i in phone_cout_dict:
    hist_nm.append(i)
    hist_nu.append(phone_cout_dict[i])




plt.figure()
plt.bar(range(len(hist_nm)),hist_nu,tick_label= hist_nm)
plt.show()