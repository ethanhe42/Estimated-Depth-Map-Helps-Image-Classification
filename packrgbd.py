from rgbd import rgbd
import os
import numpy as np
import cPickle as pickle
from cifar2im import load_CIFAR_batch
def packrgbd(rgbPath,dPath):
    ext='.jpg'
    datadict=dict()
    data=[]
    labels=np.loadtxt('label.csv',delimiter=',')
    labels=labels.T[1].astype(int)
    l=[]
    percent=0
    for i in range(60000):
        percent+=1
        if percent%1000==0:
            print 'done',percent
        dfile=os.path.join(dPath,str(i)+ext)
        rgbfile=os.path.join(rgbPath,str(i)+ext)
        try:
            img=rgbd(dfile,rgbfile)
        except:
            continue

        l.append(labels[i])
       #r=im[:,:,0].flatten()
       #g=im[:,:,1].flatten()
       #b=im[:,:,2].flatten()
       #d=im[:,:,3].flatten()
        data.append(img.flatten())
    datadict['data']=np.array(data)
    datadict['labels']=np.array(l)
    with open('data_batch','wb') as f:
        pickle.dump(datadict,f)


if __name__=="__main__":
    packrgbd('images','fayao-dcnf-fcsp-f66628a4a991/results/images')
    exit()
    for i in load_CIFAR_batch('data_batch'):
        print i.shape
