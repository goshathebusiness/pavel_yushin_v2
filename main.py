import discord
from discord.ext import commands
import config
import random
import os
import sentenceCreator
import imageCreator
import filter
import formats

bot=commands.Bot(command_prefix=config.settings['prefix']) #command_prefix переменная

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
    pictureList=os.listdir('D:/pictures')
    picName=pictureList[random.randint(0,len(pictureList))]
    author=ctx.message.author
    picPath='D:/pictures/'+picName
    await ctx.send(f'{author.mention}, название этого файла {picName}', file=discord.File(picPath))
    print(f'File {picName} sended')



@bot.event
async def on_message(message):
    await bot.process_commands(message)
    serverId=message.guild.id
    ch=message.channel
    if (message.author.bot) or (message.content in filter.commandFilter):
        print('Filtered message')
        pass
    else:
        for i in filter.commandFilter:
            if i in message.content:
                break
        path=f'data/{serverId}/pictures'
        if os.path.exists(path):
            pass
        else:
            os.makedirs(path)
        for picture in message.attachments:
            for i in formats.pictureFormat:
                if i in picture.filename:
                    await picture.save(f"data/{serverId}/pictures/{picture.filename}")
                    print('Picture saved')
                else:
                    pass
        message.content
        with open(f"data/{serverId}/data.txt", mode="a", encoding="utf-8") as output:
            output.writelines(message.content+"\n")
            print('Text saved')

@bot.command()
async def generate(ctx):
    serverId=ctx.guild.id
    try:
        imageCreator.randomImageCreate(sentenceCreator.sentenceCreate(16, serverId), serverId)
        await ctx.send(file=discord.File(f'data/{serverId}/pictures/temp.png'))
    except:
        print('Not enough data')

@bot.command()
async def generateStr(ctx):
    serverId=ctx.guild.id
    try:
        await ctx.send(f'{sentenceCreator.sentenceCreate(32, serverId)}')
    except:
        print('Not enough data')

bot.run(config.settings['token'])