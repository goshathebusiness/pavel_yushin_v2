import discord
from discord.ext import commands
from config import settings
import random
import os

bot=commands.Bot(command_prefix=settings['prefix'])

async def count_lines(filename, chunk_size=1<<13):
    with open(filename, errors='ignore') as file:
        return sum(chunk.count('\n')
                for chunk in iter(lambda: file.read(chunk_size), ''))

async def create_chains():
    nongrata={',':'','.':'','—':'','!':'','?':'','<':'','>':'','«':'','»':'','(':'',')':'','[':'',']':'','{':'','}':'','…':'',' ':''}
    nongrata_lite={'—':'','<':'','>':'','«':'','»':'','(':'',')':'','[':'',']':'','{':'','}':'','…':'...',' ':'','"':''}
    f1=open("D:/bot lib/text/data_raw.txt", mode="r", encoding="utf-8")
    raw=f1.read()
    f1.close()
    main=raw.split()
    for i in main:
        for j, k in nongrata_lite.items():
            i=i.replace(j,k)
            i=i.lower()
            pass
        main.pop(0)
        main.append(i)
    f2=open("D:/bot lib/text/chains_raw.txt", mode="w", encoding="utf-8")
    for i in range(0,len(main)):
        f2.write(main[i]+' ')
        try:
            f2.write(main[i+1]+'\n')
        except:
            f2.write(main[0])
    f2.close()

async def read_chains():
    data=[]
    f1=open("D:/bot lib/text/chains_raw.txt", mode="r", encoding="utf-8")
    lines1=await count_lines("D:/bot lib/text/chains_raw.txt")
    for i in range(0,lines1):
        chain_raw=f1.readline()
        chain_raw=chain_raw.replace('\n','')
        data.append(chain_raw)
    f1.close()

    f2=open("D:/bot lib/text/chains_cooked.txt", mode="w", encoding="utf-8")
    for i in data:
        count=data.count(i)
        f2.write(str(count))
        f2.write('$')
        f2.write(i)
        f2.write('\n')
    f2.close()

async def sentence_creator():
    f1=open("D:/bot lib/text/chains_cooked.txt", mode="r", encoding="utf-8")
    lines=await count_lines("D:/bot lib/text/chains_cooked.txt")
    data=[]
    for i in range(1,lines):
        string_raw=f1.readline()
        string_raw=string_raw.replace('\n','')
        string_raw=string_raw.replace('$',' ')
        string=(string_raw+' ')
        string=string.split()
        data.append(string)
    sentence=''
    sentence_max_lenght=10
    sentence_lenght=random.randint(1,sentence_max_lenght)
    buffer=['None']
    buffer_final=['None']
    buffer_sum=['None']
    first_word_base=data[random.randint(0,len(data)-1)]
    first_word=first_word_base[1]
    next_word=first_word_base[2]
    sentence=sentence+first_word
    while len(sentence.split())<sentence_lenght:
        del buffer[:]
        del buffer_final[:]
        del buffer_sum[:]
        for i in data:
            try:
                if next_word==i[1]:
                    buffer.append(i)
            except:
                i=data[random.randint(0,len(data)-1)]
        for i in buffer:
            buffer_sum.append(i*int(i[0]))
        buffer_final=buffer_sum[random.randint(0,len(buffer)-1)]
        word=buffer_final[1]
        next_word=buffer_final[2]
        sentence=sentence+' '+word
    print(sentence)
    return sentence

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
        output=open("D:/bot lib/text/data_raw.txt", mode="a", encoding="utf-8")
        output.writelines(message.content+"\n")
        output.close

@bot.command()
async def sentence(ctx):
    await create_chains()
    await read_chains()
    text=await sentence_creator()
    await ctx.send(text)

bot.run(settings['token'])

#        await msg.send('Файл обнаружен')
#        for picture in msg.attachments:
#            await picture.save("D:\bot lib")
#            print('saved', picture)
#            await msg.send('Файл скачан')