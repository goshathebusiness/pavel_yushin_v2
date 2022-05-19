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
        await ctx.send(f'Нет нужных полномочий')
    picturelist=os.listdir('D:/pictures')
    picname=picturelist[random.randint(0,len(picturelist))]
    author=ctx.message.author
    picpath='D:/pictures/'+picname
    await ctx.send(f'{author.mention}, название этого файла {picname}', file=discord.File(picpath))

@bot.event
async def on_message(ctx):
    if ctx.message.contai


bot.run(settings['token'])