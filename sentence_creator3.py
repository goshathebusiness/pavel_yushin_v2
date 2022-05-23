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

first_word_base=data[random.randint(0,len(data)-1)]
first_word=first_word_base[0]
next_word=first_word_base[1]
sentence=sentence+first_word

#while len(sentence.split())<sentence_max_lenght:
for j in range(0,sentence_max_lenght):
    print(buffer)
    for k in buffer:
        k=''
    for i in data:
        if next_word==i[0]:
            buffer.append(i[1])
            buffer_next.append
    word=buffer[random.randint(0,len(buffer)-1)]
    sentence=sentence+' '+word

print(sentence)
