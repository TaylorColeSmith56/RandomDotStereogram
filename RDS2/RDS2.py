#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 10:09:30 2019

@author: colesmith
"""

from PIL import Image

from random import randint as random

   
filename = 'Arrow2.png'
refImage = Image.open(filename).convert('RGB')
refImage.show()
#pixel = refImage.load()
noise = refImage.getdata()

width, length = refImage.size 
print( width, length)

white = (255,255,255)
black = (0,0,0)

noiseref = Image.new('RGB', (width, length))

pix = noiseref.load()

for z in noise:
        pix[random(0,224),random(0,91)] = white
        pix[random(0,224),random(0,91)] = black
        
noiseref.save('noiseref2.png')
#noiseref.show() 

newImageL = Image. new('RGB', (width, length))
newImageR = Image. new('RGB', (width, length))

offset = 10

for x in range(width):#columns
    for y in range(length): # rows
      
             if refImage.getpixel((x,y)) == white: 
                 if (x - offset ) % width != (x-offset):
                    continue
                 temppix = noiseref.getpixel(( x,y))
                 newImageL.putpixel(((x - offset)% width,y % length),temppix)
     
                 if refImage.getpixel((x,y)) == white:
                
                    temppix = noiseref.getpixel((x,y))
                
                    newImageL.putpixel((x,y),temppix)
                            
             else: 
                    
                    temppix = noiseref.getpixel((x,y))
                   
                    newImageL.putpixel(( x,y),temppix)
                   
newImageL.save('newImageL2.png')
newImageL.show()

for x2 in range(width):
    for y2 in range(length): 
        '''       
        if refImage.getpixel((x2,y2)) == white:
            
            if (x2 + offset ) % width != (x2+offset):
                    continue
            #newImageL[y][x] = noiseref[y][x]
            temppix2 = noiseref.getpixel((x2 ,y2 ))
            newImageR.putpixel(((x2+offset)% width ,y2 ),temppix2)
            
            if refImage.getpixel((x2 ,y2 )) == white:
                temppix2 = noiseref.getpixel((x2,y2 ))
                newImageR.putpixel((x2 ,y2 ),temppix2)
    
        else: 
        '''
            #newImageL[y][x+1]= noiseref[y][x]
        temppix2 = noiseref.getpixel((x2 ,y2 ))
            #newImageL.putpixel((x+1,y),temppix)
        newImageR.putpixel((x2 ,y2 ),temppix2)
        
newImageR.save('newImageR2.png')         
newImageR.show()   
