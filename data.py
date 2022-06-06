import random

def chain_3():
    f1=open("text/data_raw.txt", mode="r", encoding="utf-8")
    data=f1.read()
    data=data.split()
    chain=[]
    buffer=[]
    for i in range(0,len(data)):
        try:
            buffer.append(data[i-1])
        except:
            buffer.append('$none')
        buffer.append(data[i])
        try:
            buffer.append(data[i+1])
        except:
            buffer.append('$none')
        chain.append(buffer)
        buffer=[]
    return chain

def chain_5():
    f1=open("text/data_raw.txt", mode="r", encoding="utf-8")
    data=f1.read()
    data=data.split()
    chain=[]
    buffer=[]
    for i in range(0,len(data)):
        try:
            buffer.append(data[i-2])
        except:
            buffer.append('$none')
        try:
            buffer.append(data[i-1])
        except:
            buffer.append('$none')
        buffer.append(data[i])
        try:
            buffer.append(data[i+1])
        except:
            buffer.append('$none')
        try:
            buffer.append(data[i+2])
        except:
            buffer.append('$none')
        chain.append(buffer)
        buffer=[]
    return chain


chain3=chain_3()
chain5=chain_5()

sentence=''
sentence_max_lenght=10
sentence_lenght=10 #random.randint(1,sentence_max_lenght)
buffer=[]
num=0

base=chain5[random.randint(0,len(chain5))]
first_word=base[2]
next_word=base[3]
next_next_word=base[4]

while len(sentence.split())<sentence_lenght:
    #buffer=[]
    del buffer[:]
    coin=random.randint(0,1)
    if coin==0:
        for i in chain3:
            if i[1]==next_word:
                buffer.append(i)
            else:
                pass
    else:
        for i in chain5:
            if i[2]==next_word:
                if i[3]==next_next_word:
                    buffer.append(i)
    if coin==0:
        num=random.randint(0,len(buffer))-1
        word=buffer[num][1]
        next_word=buffer[num][2]
    else:
        num=random.randint(0,len(buffer))-1
        word=buffer[num][2]
        next_word=buffer[num][3]
        next_next_word=buffer[num][4]
    print(buffer)
    #print(word)
    sentence=sentence+word+' '

print(sentence)
