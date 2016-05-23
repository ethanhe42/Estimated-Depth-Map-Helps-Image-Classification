import cPickle as pickle
import numpy as np
import os
from scipy.misc import imread
from PIL import Image
import csv
import sys


def load_CIFAR_batch(filename):
  """ load single batch of cifar """
  with open(filename, 'rb') as f:
    datadict = pickle.load(f)
    X = datadict['data']
    Y = datadict['labels']
    #X = X.reshape(10000, 3, 32, 32).transpose(0,2,3,1).astype("float")
    Y = np.array(Y)
    return X, Y

def save_CIFAR10(ROOT):
  """ load all of cifar """
  xs = []
  ys = []
  for b in range(1,6):
    f = os.path.join(ROOT, 'data_batch_%d' % (b, ))
    X, Y = load_CIFAR_batch(f)
    xs.append(X)
    ys.append(Y)    
  X, Y = load_CIFAR_batch(os.path.join(ROOT, 'test_batch'))
  xs.append(X)
  ys.append(Y)
  Xtr = np.concatenate(xs)
  Ytr = np.concatenate(ys)
  print Xtr.shape
  del X, Y
  fo=csv.writer(open('label.csv','w'))
  for i in xrange(Xtr.shape[0]):
    if i % 1000 ==0:
      print i
    img=Xtr[i]
    img = img.reshape((3, 32, 32))
    img = np.swapaxes(img, 0, 2)
    img = np.swapaxes(img, 0, 1)
    #print img.shape
    im=Image.fromarray(img)
    im.save('images/'+str(i)+'.jpg')
    row=[i,Ytr[i]]
    fo.writerow(row)

def main():
    save_CIFAR10('/home/eli/work/data/cifar10/cifar-10-batches-py')

if __name__=="__main__":
    main()
