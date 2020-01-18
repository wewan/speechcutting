# import textgrid
# import os
#
#
#
# Rootpth = '/home/wei/Documents/DATA'
# dirpth = os.path.join(Rootpth,'seg')
# if not os.path.exists(dirpth):
#     os.makedirs(dirpth)
#
# #
# # vi = '/home/wei/Documents/CODE/speechcutting/English.mp4'
# # cut_p = '/home/wei/Documents/CODE/speechcutting/cut'
#
# grid = Rootpth +'/f01-1-1_D0.TextGrid'
# vipth = Rootpth + '/1_D0.mp4'
#
# t = textgrid.TextGrid()
# t.read(grid)
# phonem_tier = t[2]
# count = 0
# maxT = phonem_tier.maxTime
#
# for i in phonem_tier:
#     phone = i.mark
#     if phone !='':
#         count +=1
#         t_star = i.minTime
#         t_stop = i.maxTime
#         if count > 1:
#             t_star -=0.0
#             if t_stop !=maxT:
#                 t_stop +=0.0
#         comm = 'ffmpeg  -nostats -loglevel 0 -i  {} -ss {} -to {} {}/{}_{}.mp4'.format(vipth,t_star,t_stop,dirpth,count,phone)
#         os.system(comm)


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