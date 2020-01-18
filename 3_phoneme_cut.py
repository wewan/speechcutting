import textgrid
import os



Rootpth = '/home/wei/Documents/DATA'
dirpth = os.path.join(Rootpth,'seg')
if not os.path.exists(dirpth):
    os.makedirs(dirpth)


grid = Rootpth +'/f01-1-1_D0.TextGrid'
vipth = Rootpth + '/1_D0.mp4'

t = textgrid.TextGrid()
t.read(grid)
phonem_tier = t[2]
count = 0
maxT = phonem_tier.maxTime

for i in phonem_tier:
    phone = i.mark
    if phone !='':
        count +=1
        t_star = i.minTime
        t_stop = i.maxTime
        if count > 1:
            t_star -=0.0
            if t_stop !=maxT:
                t_stop +=0.0
        comm = 'ffmpeg  -nostats -loglevel 0 -i  {} -ss {} -to {} {}/{}_{}.mp4'.format(vipth,t_star,t_stop,dirpth,count,phone)
        os.system(comm)


