

data=[]

def count_lines(filename, chunk_size=1<<13):
    with open(filename) as file:
        return sum(chunk.count('\n')
                   for chunk in iter(lambda: file.read(chunk_size), ''))

f1=open("D:/bot lib/text/chains_raw.txt", mode="r", encoding="utf-8")
lines1=count_lines("D:/bot lib/text/chains_raw.txt")
for i in range(0,lines1):
    chain_raw=f1.readline()
    chain_raw=chain_raw.replace('\n','')
    data.append(chain_raw)
f1.close()

f2=open("D:/bot lib/text/chains_cooked.txt", mode="w", encoding="utf-8")
for i in data:
    count=data.count(i)
    f2.write(str(count))
    f2.write('$')
    f2.write(i)
    f2.write('\n')
f2.close()