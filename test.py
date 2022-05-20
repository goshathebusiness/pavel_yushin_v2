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
