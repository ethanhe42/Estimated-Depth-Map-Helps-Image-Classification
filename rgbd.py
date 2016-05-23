from scipy import misc
import numpy as np

def rgbd(depth,rgb):
    """
    return 32x32x4 array
    """
    d=misc.imread(depth)
    c=misc.imread(rgb)
    r=c[:,:,0]
    g=c[:,:,1]
    b=c[:,:,2]
    img=np.zeros([r.shape[0],r.shape[1],4])
    img[:,:,0]=r
    img[:,:,1]=g
    img[:,:,2]=b
    img[:,:,3]=d
    return img

if __name__=='__main__':
    print rgbd('predict_depth_gray.png','predict_depth_rgb.png').shape
    
