import os
from config.conf import LOG_PATH

path=LOG_PATH
files=os.listdir(path)
for i ,f in enumerate(files):
    if f.find(".lock")>=0 :
        print(i)
        os.remove(path+f)