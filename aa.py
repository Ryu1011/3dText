from PIL import Image, ImageDraw, ImageFont
from time import sleep
import matplotlib.pyplot as plt
import numpy as np
import textwrap
import time
import copy
import cv2


def make_image(message):


    lines = textwrap.wrap(message, width=5)

    font = ImageFont.truetype("ONEMObILE.ttf", size=200)
    font_color = 'rgb(0, 0, 0)' 
    bg_color = 'rgb(255, 255, 255)'

    width, height = font.getsize(lines[0])
    height *= len(lines)
    image =Image.new('RGB', (width+20, height+20), color = bg_color)
    draw = ImageDraw.Draw(image)
    
    x_text = 10
    y_text = 10
    for line in lines:
        width, height = font.getsize(line)
        draw.text((x_text, y_text), line, font=font, fill=font_color, stroke_width=1)
        y_text += height
    image.save('aa.png')


    asdf=["글씨","입체화","작업중",".",".","."]
    for i in asdf:
        time.sleep(0.3)
        print(i)


    image_gray = cv2.imread('aa.png', cv2.IMREAD_GRAYSCALE)
    img_c = cv2.Canny(image_gray, 0, 360)
    height, width = image_gray.shape
    plt.imshow(img_c)
    plt.show()


    img_c2 = copy.deepcopy(img_c)
    for i in range(0, width):
        m=0
        n=0
        for j in range(0,height):
            if img_c2[j,i]==255:
                if img_c2[j-1,i]==0: n=j
                if img_c2[j+1,i]==0:
                    if (m%2==0) and ((j-n)<2):
                        img_c[n:j+1,i]=0
                    m+=1
        cv2.imshow('가로줄 제거', img_c)
        cv2.waitKey(1)  
    for i in range(0, height):
        m=0
        n=0
        for j in range(0,width):
            if img_c2[i,j]==255:
                if img_c2[i,j-1]==0: n=j
                if img_c2[i,j+1]==0:
                    if (m%2==0) and ((j-n)<2):
                        img_c[i,n:j+1]=0
                    m+=1
        cv2.imshow('세로줄 제거', img_c)
        cv2.waitKey(1)


    k = cv2.getStructuringElement(cv2.MORPH_RECT, (1,3))
    opening = cv2.morphologyEx(img_c, cv2.MORPH_OPEN, k)
    k2 = cv2.getStructuringElement(cv2.MORPH_RECT, (3,1))
    opening2 = cv2.morphologyEx(img_c, cv2.MORPH_OPEN, k2)
    img_c =cv2.add(opening, opening2)
    

    for i in range(0, width):
        for j in range(0, height):
            if img_c[j,i]==255:
                if img_c[j+1,i]==0 and img_c[j,i+1]==0:
                    img_c[j,i]=0  
          
                    cv2.imshow('', img_c)
                    cv2.waitKey(1)
    
    
    k = cv2.getStructuringElement(cv2.MORPH_RECT, (4,4))
    rst = cv2.dilate(img_c, k)
    cv2.imshow('', rst)
    cv2.waitKey(0)

make_image("노형률")