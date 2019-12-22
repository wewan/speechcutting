# get time stamp from TextGrid file

import textgrid
import os

vi = '/home/wei/Documents/CODE/speechcutting/English.mp4'
cut_p = '/home/wei/Documents/CODE/speechcutting/cut'
t = textgrid.TextGrid()
t.read('out/eng.TextGrid')
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