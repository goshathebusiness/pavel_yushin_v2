from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
import random

def randomPicture(serverId):
    pictureList=os.listdir(f'data/{serverId}/pictures')
    try:
        pictureList.remove('temp.png')
    except:
        pass
    picName=pictureList[random.randint(0,len(pictureList)-1)]
    basewidth = 600
    img = Image.open(f'data/{serverId}/pictures/{picName}')
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save(f'data/{serverId}/pictures/temp.png')
    return f'data/{serverId}/pictures/temp.png'

def imageCreate(text, path, serverId):
    img=Image.open(path)
    imgWidth, imgHeight=(img.width, img.height)
    fontSize=round(img.height/10)
    font=ImageFont.truetype('fonts/impact.ttf', size=fontSize)

    textWrapped=textwrap.wrap(text, width=round(imgWidth/(fontSize/2)-1))

    draw=ImageDraw.Draw(img)
    textWidth, textHeight=draw.textsize(text, font)

    if len(text)>=60:
        currentHeight=imgHeight-(imgHeight/2)
    else:
        currentHeight=imgHeight-(imgHeight/4)

    for line in textWrapped:
        textWidth,textHeight=draw.textsize(line, font=font)
        draw.text((((imgWidth-textWidth)/2)-1, currentHeight-1),line, font=font, fill=('#000000'))
        draw.text((((imgWidth-textWidth)/2)+1, currentHeight-1),line, font=font, fill=('#000000'))
        draw.text((((imgWidth-textWidth)/2)-1, currentHeight-1),line, font=font, fill=('#000000'))
        draw.text((((imgWidth-textWidth)/2)+1, currentHeight+1),line, font=font, fill=('#000000'))
        draw.text(((imgWidth-textWidth)/2, currentHeight),line,font=font, fill=('#FFFFFF'))
        
        currentHeight+=textHeight

    img.save(f'data/{serverId}/pictures/temp.png')

def randomImageCreate(text,serverId):
    imageCreate(text, randomPicture(serverId), serverId)

if __name__=='__main__':
    imageCreate('aye basota фафафафа афаф уу у фее', randomPicture())