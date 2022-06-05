import random

def createSentence():
    chains=[]

    class Chain():
        def __init__(self, word='', nextWord='', nextNextWord='', num=1) -> None:
            self.word=word
            self.nextWord=nextWord
            self.nextNextWord=nextNextWord
            if num==None:
                self.num=1
            else:
                self.num=num
            chains.append(self)
        
        def info(self):
            print(f'Цепь: {self.word} {self.nextWord} {self.nextNextWord}. Встречается в тексте {self.num} раз')

    with open("text/data_raw.txt", mode="r", encoding="utf-8") as file:
        data=file.read()
    data=data.split()
    dataNew=[]

    for i in range(0,len(data)-1):
        try:
            arr=data[i]+' '+data[i+1]+' '+data[i+2]
            dataNew.append(arr)
        except:
            try:
                arr=data[i]+' '+data[i+1]+' '+data[random.randint(0,len(data)-1)]
                dataNew.append(arr)
            except:
                arr=data[i]+' '+data[random.randint(0,len(data)-1)]+' '+data[random.randint(0,len(data)-1)]
                dataNew.append(arr)

    dataNewSet=set(dataNew)
    for i in dataNewSet:
        iSplitted=i.split()
        try:
            Chain(word=iSplitted[0], nextWord=iSplitted[1], nextNextWord=iSplitted[2],num=dataNew.count(i))
        except:
            try:
                Chain(word=iSplitted[0], nextWord=iSplitted[1], nextNextWord=None, num=dataNew.count(i))
            except:
                Chain(word=iSplitted[0], nextWord=None, nextNextWord=None, num=dataNew.count(i))

    buffer=[]
    bufferSecond=[]
    sentenceMaxLenghtWanted=32
    sentenceLenght=random.randint(1,sentenceMaxLenghtWanted)
    chainSingle=chains[random.randint(0,len(chains)-1)]
    while chainSingle.word=='-' or chainSingle.word=='.' or chainSingle.word== ',' or chainSingle.word=='+' or chainSingle.word=='/' or chainSingle.word=='*' or chainSingle.word=='?':
        chainSingle=chains[random.randint(0,len(chains)-1)]
    sentence=chainSingle.word
    nextWord=chainSingle.nextWord
    nextNextWord=chainSingle.nextNextWord

    while len(sentence.split())<sentenceLenght:
        del buffer[:]
        del bufferSecond[:]
        for i in chains:
            if i.word==nextWord and i.nextWord==nextNextWord:
                for k in range(0,2):
                    buffer.append(i)
            elif i.word==nextWord:
                buffer.append(i)
        if len(buffer)==0:
            buffer.append(chains[random.randint(0,len(chains)-1)])

        for i in buffer:
            for j in range(0,i.num):
                bufferSecond.append(Chain(word=i.word, nextWord=i.nextWord, nextNextWord=i.nextNextWord, num=None))
            choiced=bufferSecond[random.randint(0,len(bufferSecond)-1)]
            word=choiced.word
            nextWord=choiced.nextWord
            nextNextWord=choiced.nextNextWord
        sentence+=' '+word

    if sentence[0].islower()==True:
        sentenceFirstChar=sentence[0]
        sentence=sentence[1:]
        sentence=sentenceFirstChar.upper()+sentence

    if sentence[-1]=='!' or sentence[-1]=='?' or sentence[-1]==';' or sentence[-1]==':' or sentence[-1]==')' or sentence[-1]=='(' or sentence[-1]=='$':
        pass
    elif sentence[-1]!='.':
        sentence+='.'
    elif sentence[-1]==',':
        sentence=sentence[:-1]
        sentence+='.'
    return sentence

if __name__=='__main__':
    createSentence()