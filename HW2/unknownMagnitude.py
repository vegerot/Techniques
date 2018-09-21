#!/usr/bin/env python3
import numpy as np
import re
import itertools

def sublist(lst1, lst2):
    for i in lst2:
        if np.array_equal(lst1,i):
            return True
    return False

def getBorder(img,center,dist):
    around=np.empty([0,2])
    for i in itertools.product(range(-1*dist,dist+1),repeat=2):
        if np.sum(np.power(i,2))>=np.power(dist,2):
            around=np.vstack((around,np.array([i[0]+center[0],i[1]+center[1]])))
    return around.astype(int)

def printColoredArray(img, around): 
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if sublist([i,j], list(around.astype(int))): 
                print("\u001b[31m"+'{0: <3}'.format(str(img[i,j]))+"\u001b[0m", end=" ")
            else:
                output='{0: <3}'.format(str(img[i,j]))
                print(output, end=" ")
            (str(img[i,j]))
        print()
    print("\n")

def getBackground(img, around):
    background=np.array([])
    for i in around.astype(int):
        background=np.append(background,img[i[0],i[1]])
    backgroundAvg=np.mean(background)
    return backgroundAvg


def main():
    imgNums="34 16 26 33 37 22 25 25 29 19 28 25 22 20 44 34 22 26 14 30 30 20 19 17 31 70 98 66 37 25 35 36 39 39 23 20 34 99 229 107 38 28 46 102 159 93 37 22 33 67 103 67 36 32 69 240 393 248 69 30 22 33 34 29 36 24 65 241 363 244 68 24 28 22 17 16 32 24 46 85 157 84 42 22 18 25 27 26 17 18 30 29 35 24 30 27 32 23 16 29 25 24 30 28 20 35 22 23 28 28 28 24 26 26 17 19 30 35 30 26"

    img=np.array([int(num) for num in imgNums.split()])
    img=np.reshape(img,(10,12))
    dist=2
    center=np.concatenate(np.where(img==229))
    around=getBorder(img,center,dist)
    printColoredArray(img,around)
    print("\u001b[37mAverage Background 1 is\u001b[93m", getBackground(img,around),"\u001b[0m")
    print("\n")

    dist2=2
    center2=np.concatenate(np.where(img==393))
    around2=getBorder(img,center2,dist2)
    printColoredArray(img,around2)
    print("\u001b[37mAverage Background 2 is\u001b[93m", getBackground(img,around2),"\u001b[0m")
if __name__=="__main__":
    main()
