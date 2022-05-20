import random

def count_lines(filename, chunk_size=1<<13):
    with open(filename) as file:
        return sum(chunk.count('\n')
                   for chunk in iter(lambda: file.read(chunk_size), ''))

f1=open("D:/bot lib/text/cooked.txt", mode="r", encoding="utf-8")
lines=count_lines("D:/bot lib/text/cooked.txt")
data=[]
for i in range(1,lines):
    string_raw=f1.readline()
    num=int(string_raw[:string_raw.find(':')])
    string=str(string_raw[string_raw.find(':')+1:])
    string=string.replace('\n','')
    string_final=(string+' ')*num
    string_mega_final=string_final.split()
    if type(string_mega_final)!=str:
        data=data+string_mega_final
    else:
        data.append(string_final)

sentence=''
max_sentence_lenght=20
sentence_lenght=random.randint(1,max_sentence_lenght)
for i in range(0,sentence_lenght):
    word=data[random.randint(0,len(data))]
    sentence=sentence+word+' '

print(sentence)
