# Depth from Single Monocular Images 

This is the prediction/test code for the paper: 

`Learning Depth from Single Monocular Images Using Deep Convolutional Neural Fields`

Available at: [http://arxiv.org/abs/1502.07411](http://arxiv.org/abs/1502.07411).

This code is tested on Ubuntu 14.04, and requires Matlab 2014a or later versions.



# Install

Two toolboxes are required for using this code. For convenience, they are included in the folder: 

`./libs` and pre-compiled in Linux. These toolboxes are as follows:

1. MatConvNet is required for the CNN training, which can be downloaded at: http://www.vlfeat.org/matconvnet/

2. VLFeat is required for generating superpixels, which is available at http://www.vlfeat.org/.
This code is tested using the VLFeat 0.9.18 version.



# Run 

1. Users need to compile MatConvNet before running our code. 
Please refer to: http://www.vlfeat.org/matconvnet/

2. We provide a demo file in folder `./demo/`: 
 
     `demo_DCNF_FCSP_depths_prediction.m`

This is a demo for predicting depths of given images using our trained model. 

3. We provide two trained models (trained using the Make3D and NYUD2 datasets respectively) in the folder `./model_trained`. 




# Contact

authors: Fayao Liu, Chunhua Shen, Guosheng Lin, Ian Reid (University of Adelaide, Australia)

email: firstname.lastname@adelaide.edu.au

03/2015
