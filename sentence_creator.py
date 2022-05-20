import random

def count_lines(filename, chunk_size=1<<13):
    with open(filename) as file:
        return sum(chunk.count('\n')
                   for chunk in iter(lambda: file.read(chunk_size), ''))

f1=open("D:/bot lib/text/chains_cooked.txt", mode="r", encoding="utf-8")
lines=count_lines("D:/bot lib/text/chains_cooked.txt")
data=[]
for i in range(1,lines):
    string_raw=f1.readline()
    string=str(string_raw[string_raw.find(':')+1:])
    string=string.replace('\n','')
    string_final=(string+' ')
    string_mega_final=string_final.split()
    data.append(string_final)
        
sentence=''
sentence_lenght=10

first_word_base=data[random.randint(0,len(data))]
first_word=first_word_base[first_word_base.find('$')+1:]
sentence=sentence+first_word

first_word_splitted=first_word.split()
try:
    next_word=first_word_splitted[1]
except:
    next_word=first_word_splitted[0]
while len(sentence.split())<sentence_lenght: #ДОБАВИТЬ СИСТЕМУ РАНДОМА НЕКСТ СЛОВА, ТОГДА РАЗМЕР ЕБАНУТЫЙ ДОЛЖЕН ПОФИКСИТСЯ
#for n in range(0,sentence_lenght):
    for i in data:
        i=i[i.find('$')+1:]
        i_splitted=i.split()
        if i_splitted[0]==next_word:
            sentence=sentence+i_splitted[0]+' '
            try:
                next_word=i_splitted[1]
            except:
                next_word=i_splitted[0]
        else:
            pass
print(sentence)
print(len(sentence.split()))