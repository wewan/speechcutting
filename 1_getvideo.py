import os
import csv

# get csv
en_vid_ls = []
root_pth = '/media/wei/ww-5T/Kinship/family'


def get_fam_pth(fam_n):
    fam_fld = 'f_'+fam_n.split('-')[0][1:]
    mem_fld = 'm_'+fam_n.split('-')[1]
    fld =  os.path.join(fam_fld,mem_fld)
    return fld

def get_exact_info(fld):
    fls = os.listdir(fld)
    for fl in fls:
        if fl.startswith('1'):
            ds_one = fl
        if fl.startswith('3'):
            ds_two = fl
    dso_pth = os.path.join(fld,ds_one)
    dst_pth = os.path.join(fld,ds_two)
    return dso_pth,dst_pth

with open('/media/wei/ww-5T/Kinship/label/family_kin.csv') as ff:
    reader = csv.reader(ff, delimiter=',')
    for it in reader:
        # check language
        if it[4]=='en':
            fami_pth = get_fam_pth(it[0])
            fami_pth = os.path.join(root_pth,fami_pth)
            ptho,ptht = get_exact_info(fami_pth)
            en_vid_ls.append(ptho)
            en_vid_ls.append(ptht)


print(en_vid_ls)


###############

root_aud = '/media/wei/ww-5T/Kinship/speech/aud/'
ViList = en_vid_ls
AuList = []
def get_au_nm(pth):
    fn = pth.split('/')[6].replace('_','')
    mn = pth.split('/')[7][-1]
    an = pth.split('/')[8].replace('mp4','wav')
    au_n = fn+'-'+mn+'-'+an
    return au_n

def get_aud_pth(vid_ls):

    for num,pth in enumerate(vid_ls):
        au_n = get_au_nm(pth)
        aupth = os.path.join(root_aud,'au{}'.format(num+1))
        aupth = os.path.join(aupth,au_n)
        AuList.append(aupth)

    return AuList


AuList = get_aud_pth(ViList)

############################ get audio
#
# for vi,au in zip(ViList,AuList):
#     aupth = au[:-14]
#     if not os.path.exists(aupth):
#         os.makedirs(aupth)
#     os.system('ffmpeg -i %s -ar 16000 %s' % (vi, au))


############################ get text

# import io
# import os
#
# # Imports the Google Cloud client library
# from google.cloud import speech
# from google.cloud.speech import enums
# from google.cloud.speech import types
# from google.oauth2 import service_account
#
# credentials = service_account.Credentials.from_service_account_file(
# '/home/wei/google/credentials/56952e1412ca.json')
#
# # Instantiates a client
# client = speech.SpeechClient(credentials=credentials)
#
#
# ## define write txt
#
# def write_txt(au_pth,txt):
#     txt_pth = au_pth.replace('.wav','.txt')
#     with open(txt_pth,'w') as tt:
#         tt.write(txt)
#
#
# for aud_nam in AuList:
#
#     # Loads the audio into memory
#     with io.open(aud_nam, 'rb') as audio_file:
#         content = audio_file.read()
#         audio = types.RecognitionAudio(content=content)
#
#     config = types.RecognitionConfig(
#         encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=16000,
#         audio_channel_count=2,
#         language_code='en-US'          # en-GB en-US nl-NL
#
#     )
#
#     # Detects speech in the audio file
#     response = client.recognize(config, audio)
#
#     con = ''
#     for result in response.results:
#
#         trans = result.alternatives[0].transcript
#         con = con+trans
#     write_txt(aud_nam,con)
#     print('Transcript: {}'.format(con))


###################################### get textgrid

# comm = '/home/wei/Documents/CODE/speechcutting/create_textgrid.praat'
# comm = 'sh texgrid.sh'
# os.system(comm)


###################################### get align

# comm = 'sh malign.sh'
# os.system(comm)

###################################### gether

import textgrid
import os



cut_pth = '/media/wei/ww-5T/Kinship/speech/cuts/'
grid_pth = '/media/wei/ww-5T/Kinship/speech/out/'
for vi,au in zip(ViList,AuList):
    #
    # vi = '/home/wei/Documents/CODE/speechcutting/English.mp4'
    # cut_p = '/home/wei/Documents/CODE/speechcutting/cut'
    cut_p = cut_pth + au.split('/')[-1][:-4]
    if not os.path.exists(cut_p):
        os.makedirs(cut_p)
    grid = grid_pth+ au.split('/')[-1][:-4]+'.TextGrid'

    t = textgrid.TextGrid()
    t.read(grid)
    phonem_tier = t[1]
    count = 0
    maxT = phonem_tier.maxTime

    for i in phonem_tier:
        phone = i.mark
        if phone !='':
            count +=1
            t_star = i.minTime
            t_stop = i.maxTime
            if count > 1:
                t_star -=0.1
                if t_stop !=maxT:
                    t_stop +=0.1
            comm = 'ffmpeg  -nostats -loglevel 0 -i  {} -ss {} -to {} {}/{}_{}.mp4'.format(vi,t_star,t_stop,cut_p,count,phone)
            os.system(comm)

print(6)