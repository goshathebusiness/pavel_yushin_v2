import re

nongrata=['-',',','.','—','!','?','<','>','«','»','(',')','[',']','{','}']
#nongrata='-,.—!?<>«»'

print(re.search('.','aye...,<<?'))
a=re.sub(".","a","aye...,<<?")
print(a)

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text
 
text2 = 'aye...,<<?'
i = {'hel':'HEL'}
j = {'-':'', '.':'-', 'o':'0'}
text2 = replace_all(text2, j)
text2 = replace_all(text2, j)
print(text2)


sentence=''

max_sentence_lenght=10
sentence_lenght=random.randint(1,max_sentence_lenght)
first_word_base=data[random.randint(0,len(data))]
first_word_second_part=first_word_base[first_word_base.find(' ')+1:]
first_word=first_word_base[first_word_base.find('$')+1:first_word_base.find(' ')]
sentence=sentence+first_word
sentence_splitted=sentence.split()
for i in range(0,max_sentence_lenght):
    for i in data:
        first_part_word=i[i.find('$')+1:i.find(' '):]
        second_part_word=i[i.find(' ')+1:]
        if first_word_second_part in first_part_word:
            sentence=sentence+first_part_word
        elif first_part_word!=first_word_second_part:
            sentence=sentence+second_part_word
        else:
            pass



print(sentence)