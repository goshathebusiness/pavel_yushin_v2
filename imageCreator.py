from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
import random

def randomPicture():
    pictureList=os.listdir('pictures')
    try:
        pictureList.remove('temp.png')
    except:
        pass
    picName=pictureList[random.randint(0,len(pictureList)-1)]
    path=f'pictures/{picName}'
    return path

def imageCreate(text, path):
    img=Image.open(path)
    imgWidth, imgHeight=(img.width, img.height)
    fontSize=round(img.height/10)
    font=ImageFont.truetype('fonts/impactRegular.ttf', size=fontSize)

    textWrapped=textwrap.wrap(text, width=round(imgWidth/(fontSize/2)+5))

    draw=ImageDraw.Draw(img)
    textWidth, textHeight=draw.textsize(text, font)

    if len(text)>=60:
        currentHeight=imgHeight-(imgHeight/2)
    else:
        currentHeight=imgHeight-(imgHeight/4)

    for line in textWrapped:
        textWidth,textHeight=draw.textsize(line, font=font)
        draw.text((((imgWidth-textWidth)/2)-1, currentHeight), text, font=font, fill='#000000')
        draw.text((((imgWidth-textWidth)/2)+1, currentHeight), text, font=font, fill='#000000')
        draw.text(((imgWidth-textWidth)/2, currentHeight-1), text, font=font, fill='#000000')
        draw.text(((imgWidth-textWidth)/2, currentHeight+1), text, font=font, fill='#000000')
        draw.text(((imgWidth-textWidth)/2, currentHeight),line,font=font, fill=('#FFFFFF'))
        
        currentHeight+=textHeight

    img.save('pictures/temp.png')

if __name__=='__main__':
    imageCreate('aye basota', randomPicture())