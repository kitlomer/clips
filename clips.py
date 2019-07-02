import numpy as np
import librosa
import os
# from scipy import signal
#import operator
#last = operator.itemgetter(-1)
lens=[]
sr = 44100
totallen=34*60+59 #total counts of second
# k=0.4

while sum(lens)<totallen:
    # len=abs(np.random.normal(7,4))
    len=np.random.uniform(1,9)
    lens.append(len)
	
if sum(lens)>totallen:
    lens[-1]=lens[-1]-sum(lens)+totallen

y,sr=librosa.load('04 能臣之路NRcutBG.wav',sr)

lensum=np.cumsum(lens)
samplelensum=np.round(lensum*sr)
ends = samplelensum
start = samplelensum[0:-1]+1
starts= np.insert(start,0,0)

for i,(start0,end0) in enumerate(zip(starts,ends)):
    ylil=y[int(start0):int(end0)]
    filename = os.path.join('CLIPS', '04-'+ str(i) + '.wav')
   # ylil0 = signal.lfilter([1], [1, -k], ylil)
   # z = librosa.zero_crossings(ylil0)
   # zc = np.nonzero(z)
   # zclast=zc[0][-1]
   # zcfirst = zc[0][1]
   # ylil1=ylil0[zcfirst:zclast]
   # ylil2=signal.lfilter([1,-k],[1],ylil1)
    librosa.output.write_wav(filename, ylil, sr)




##############zero crossing###

#
# import numpy as np
# import librosa
# import os
# lens=[]
# sr = 22050
# totallen=13*60+9
# y,sr=librosa.load('C:\\Users\\A\\Downloads\\120605obama\\120615_AddresstotheNation.wav',sr)
# z = librosa.zero_crossings(y)
# ends=np.nonzero(z)
#
#
########################resample

# import librosa
# y,sr=librosa.load('D:\\silent_bullet_01_f000014.wav',16000)
# y_48k = librosa.resample(y, 16000, 48000)
# filename='D:\\silent_bullet_01_f000014_48k.wav'
# librosa.output.write_wav(filename, y_48k, 48000)

