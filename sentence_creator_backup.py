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
    string_raw=str(string_raw[string_raw.find('$')+1:])
    string=(string_raw+' ')
    string=string.split()
    data.append(string)

sentence=''
sentence_max_lenght=10
buffer=['None']
buffer_final=['None']

first_word_base=data[random.randint(0,len(data)-1)]
first_word=first_word_base[0]
next_word=first_word_base[1]
sentence=sentence+first_word

while len(sentence.split())<sentence_max_lenght:
    del buffer[:]
    del buffer_final[:]
    for i in data:
        try:
            if next_word==i[0]:
                buffer.append(i)
        except:
            i=data[random.randint(0,len(data)-1)]
    buffer_final=buffer[random.randint(0,len(buffer)-1)]
    word=buffer_final[0]
    next_word=buffer_final[1]
    sentence=sentence+' '+word

print(sentence)
