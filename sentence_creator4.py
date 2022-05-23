import random

def count_lines(filename, chunk_size=1<<13):
    with open(filename, errors='ignore') as file:
        return sum(chunk.count('\n')
                   for chunk in iter(lambda: file.read(chunk_size), ''))

f1=open("D:/bot lib/text/chains_cooked.txt", mode="r", encoding="utf-8")
lines=count_lines("D:/bot lib/text/chains_cooked.txt")
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
buffer=['None']
buffer_final=['None']
buffer_sum=['None']
chance_sum=0

first_word_base=data[random.randint(0,len(data)-1)]
first_word=first_word_base[1]
next_word=first_word_base[2]
sentence=sentence+first_word

while len(sentence.split())<sentence_max_lenght:
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
