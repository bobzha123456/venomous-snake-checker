#!/usr/bin/python3

import jetson_inference
import jetson_utils

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str, help="filename of the image to process")
parser.add_argument("--network", type=str, default="googlenet", help="model to use, can be:  googlenet, resnet-18, ect. (see --help for others)")
opt = parser.parse_args()
img = jetson_utils.loadImage(opt.filename)
net = jetson_inference.imageNet(opt.network)
class_idx, confidence = net.Classify(img)

class_desc = net.GetClassDesc(class_idx)
print("this is a  "+ str(class_desc))# +" (class #"+ str(class_idx),")")

if class_idx in[52, 55, 56, 58, 61, 62]:
    print("this snake is non venomous")
elif class_idx in[53, 57, 59, 60]:   
    print("this snake is mildly venomous")  
elif class_idx in[54, 63, 64, 65, 66, 67, 68]:
    print("this snake is venomous ")
else:
    print("this "+ class_desc +" is so cute!!! ")
# python3 my-recognition.py polar_bear.jpg