#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 13:44:32 2019

@author: colesmith
"""


from PIL import Image

from random import randint as random

filename = 'Arrow.png'
refImage = Image.open(filename).convert('RGB')
refImage.show()  
#pixel = refImage.load()
noise = refImage.getdata()

width, length = refImage.size #https://python-forum.io/Thread-random-change-of-color-pixel-with-PIL
print(width, length)

white = (255,255,255)
black = (0,0,0)

noiseref = Image.new('RGB', (width, length))#https://python-forum.io/Thread-random-change-of-color-pixel-with-PIL

pix = noiseref.load()#https://stackoverflow.com/questions/138250/how-to-read-the-rgb-value-of-a-given-pixel-in-python

for z in noise:
        pix[random(0,221),random(0,84)] = white
        pix[random(0,221),random(0,84)] = black
                
noiseref.save('noiseref.png')
#noiseref.show()  
 
newImageL = Image. new('RGB', (width, length))
newImageR = Image. new('RGB', (width, length))

offset = 10

for x in range(width):
    for y in range(length): 
        
        if refImage.getpixel((x,y)) == white: 
            if (x - offset ) % width != (x-offset):
                    continue   
            temppix = noiseref.getpixel((x,y))
            newImageL.putpixel(((x - offset)% width,y % length),temppix)
            
            if refImage.getpixel((x,y)) == white:
                
                    temppix = noiseref.getpixel((x,y))
                    
                    newImageL.putpixel((x,y),temppix)
      
        else: 
            #newImageL[y][x+1]= noiseref[y][x]
            temppix = noiseref.getpixel((x,y))
            #newImageL.putpixel((x+1,y),temppix)
            newImageL.putpixel((x,y),temppix)
            

newImageL.save('newImageL.png')#https://stackoverflow.com/questions/138250/how-to-read-the-rgb-value-of-a-given-pixel-in-python
newImageL.show()

for x2 in range(width):
    for y2 in range(length): 
        '''
        if refImage.getpixel((x2,y2)) == white: 
            #newImageL[y][x] = noiseref[y][x]
            temppix2 = noiseref.getpixel((x2,y2))
            newImageR.putpixel((x2+3,y2),temppix2)
            if refImage.getpixel((x2,y2)) == white: 
            #newImageL[y][x] = noiseref[y][x]
                temppix2 = noiseref.getpixel((x2,y2))
                newImageR.putpixel((x2,y2),temppix2)
        else: 
        '''
        
            #newImageL[y][x+1]= noiseref[y][x]
        temppix2 = noiseref.getpixel((x2,y2))
            #newImageL.putpixel((x+1,y),temppix)
        newImageR.putpixel((x2,y2),temppix2)
            
        
newImageR.save('newImageR.png')
newImageR.show()