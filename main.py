import discord
from discord.ext import commands
from config import settings
import random
import os

bot=commands.Bot(command_prefix=settings['prefix'])

@bot.event
async def on_ready():
    print("ready")

@bot.command()
async def randomint(ctx):
    await ctx.message.delete()
    author=ctx.message.author
    random_integer=random.randint(0,100)
    await ctx.send(f'{author.mention}, {random_integer}!')

@bot.command()
async def randompicture(ctx):
    try:
        await ctx.message.delete()
    except:
        await ctx.send('Нет нужных полномочий')
    picturelist=os.listdir('D:/pictures')
    picname=picturelist[random.randint(0,len(picturelist))]
    author=ctx.message.author
    picpath='D:/pictures/'+picname
    await ctx.send(f'{author.mention}, название этого файла {picname}', file=discord.File(picpath))

picture_format=['.png','.jpg','jpeg','bmp']

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    ch=message.channel
    if (message.author.bot):
        pass
    else:
        for picture in message.attachments:
            for i in picture_format:
                if i in picture.filename:
                    await picture.save(f"D:/bot lib/pictures/{picture.filename}")
                else:
                    pass
        message.content
        output=open("D:/bot lib/text/raw.txt", mode="a", encoding="utf-8")
        output.writelines(message.content+"\n")
        output.close
        

bot.run(settings['token'])

#        await msg.send('Файл обнаружен')
#        for picture in msg.attachments:
#            await picture.save("D:\bot lib")
#            print('saved', picture)
#            await msg.send('Файл скачан')