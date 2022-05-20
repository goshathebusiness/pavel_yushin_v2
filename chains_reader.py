

data=[]

def count_lines(filename, chunk_size=1<<13):
    with open(filename) as file:
        return sum(chunk.count('\n')
                   for chunk in iter(lambda: file.read(chunk_size), ''))

f1=open("D:/bot lib/text/chains.txt", mode="r", encoding="utf-8")
lines1=count_lines("D:/bot lib/text/chains.txt")
for i in range(0,lines1):
    chain_raw=f1.readline()
    chain_raw=chain_raw.replace('\n','')
    j=chain_raw.split()
    data.append(j)

f2=open("D:/bot lib/text/cooked.txt", mode="r", encoding="utf-8")
lines2=count_lines("D:/bot lib/text/cooked.txt")
unique_words=[]
for i in range(1,lines2):
    string_raw=f2.readline()
    num=int(string_raw[:string_raw.find(':')])
    string=str(string_raw[string_raw.find(':')+1:])
    string=string.replace('\n','')
    unique_words.append(string)
unique_words=set(unique_words)

for i in unique_words:
    