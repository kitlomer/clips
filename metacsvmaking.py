import os 


# dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = os.getcwd()
csvfile0 = os.path.join(dir_path,'text','meta03')
txtfile = os.path.join(dir_path,'text','03_new')
wav_path = os.path.join(dir_path,'CLIPS','03')
files = os.listdir(wav_path)
# files.sort(key=lambda x: int(os.path.splitext(x)[0]))
filemid = []

for x in files:
    filemid.append(int(x[3:-4]))
filemid.sort()
files = []

for i in filemid:
    eachname = '03-'+str(i)+'.wav'
    files.append(eachname)
	
    
# nfiles=[x[:-4] for x in files]
nfiles=[x for x in files]

with open(txtfile,'r',encoding='utf8') as input:
    with open(csvfile0, 'a') as output:
        for i,(line,nfile) in enumerate(zip(input,nfiles)):
            output.write(nfile)
            output.write("|")
            output.write(line)
			
        #for i, nfile in enumerate(nfiles):
         #   output.write(nfile)
          #  output.write("|\n")





