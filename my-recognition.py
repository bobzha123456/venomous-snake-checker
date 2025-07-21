#!/usr/bin/python3
#ai needed
import jetson_inference
import jetson_utils
#get location of the file 
import argparse

#parser file name and use google net
parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str)
parser.add_argument("googlenet", type=str)

#get image
img = jetson_utils.loadImage(opt.filename)
#get recogination network
net = jetson_inference.imageNet(googlenet)


#get the index of the class
class_idx = net.Classify(img)
#get the name of the class
class_desc = net.GetClassDesc(class_idx)
print("this is a  "+ str(class_desc))

if class_idx in[52, 55, 56, 58, 61, 62]:
    print("this snake is non venomous")
elif class_idx in[53, 57, 59, 60]:   
    print("this snake is mildly venomous")  
elif class_idx in[54, 63, 64, 65, 66, 67, 68]:
    print("this snake is venomous ")
else:
    print("this "+ class_desc +" is so cute!!! ")
# python3 my-recognition.py snake-testing.jpg
