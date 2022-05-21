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
    string=str(string_raw[string_raw.find(':')+1:])
    string=string.replace('\n','')
    string_final=(string+' ')
    string_mega_final=string_final.split()
    data.append(string_final)
        
sentence=''
pre_sentence=[]
max_sentence_lenght=20
sentence_lenght=random.randint(1,max_sentence_lenght)
sentence_splitted=[]

first_word_base=data[random.randint(0,len(data))]
first_word=first_word_base[first_word_base.find('$')+1:]
sentence=sentence+first_word
next_word=['']
count=0
first_word_splitted=first_word.split()
try:
    next_word[0]=first_word_splitted[1]
except:
    next_word[0]=first_word_splitted[0]

while len(sentence_splitted)<sentence_lenght: #ДОБАВИТЬ СИСТЕМУ РАНДОМА НЕКСТ СЛОВА, ТОГДА РАЗМЕР ЕБАНУТЫЙ ДОЛЖЕН ПОФИКСИТСЯ
#for n in range(0,5):
    pre_sentence.clear()
    for i in data:
        
        i_str=i[i.find('$')+1:]
        i_splitted=i_str.split()
        i_num=i[:i.find('$')]
        #print(i_splitted)
        if i_splitted[1]==next_word[0]:
            print(i_splitted,next_word)
            print(i_splitted[0]==next_word[0])
            pre_sentence.append(i_splitted[0])
            try:
                next_word[0]=i_splitted[1]
            except:
                next_word[0]=i_splitted[0] #сделать рандомайзер при повторе
        else:
            pass
    count=count+int(i_num)
    print(pre_sentence)
    sentence=sentence+pre_sentence[random.randint(0,len(pre_sentence))-1]+' '
    sentence_splitted=sentence.split()
print(sentence)
print(count,'adfafd')
print(len(sentence_splitted))
#print(pre_sentence)
print(len(pre_sentence))