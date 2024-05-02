# Estimated Depth Map Helps Image Classification

[GitHub - yihui-he/Estimated-Depth-Map-Helps-Image-Classification: Depth estimation with neural network, and learning on RGBD images](https://github.com/yihui-he/Estimated-Depth-Map-Helps-Image-Classification)

[Estimated Depth Map Helps Image Classification](https://arxiv.org/abs/1709.07077)

![Untitled](https://github.com/ethanhe42/Estimated-Depth-Map-Helps-Image-Classification/assets/10027339/a1ec2282-ad31-4013-b78b-361c46fa3837)


![Untitled 1](https://github.com/ethanhe42/Estimated-Depth-Map-Helps-Image-Classification/assets/10027339/13900f3b-0a69-4100-8c78-2b5345b2f3dd)


if you find our work helpful in your research, please consider citing:

```
@article{estimated2017he,
  title={Estimated Depth Map Helps Image Classification},
  author={He, Yihui},
  journal={arXiv preprint arXiv:1709.07077},
  year={2017}
}
```

### how to test

1. you can run tryhere.ipynb to test performance on RGBD and RGB images.
2. you can do depth estimation in train/ folder

### Approach

1. train a mapping map RGB to depth
2. convert cifar10 to images
3. convert RGBD to cifar10 format
4. train neural network on RGBD dataset

### download

[dcnf-fcsp](https://bitbucket.org/fayao/dcnf-fcsp)[RGBD CIFAR-10](https://github.com/yihui-he/Estimated-Depth-Map-Helps-Image-Classification/releases/tag/depth-cifar-10)

### External Links

[all dataset descriptions](http://www0.cs.ucl.ac.uk/staff/M.Firman/RGBDdatasets/)[a good one](http://redwood-data.org/3dscan/index.html)
