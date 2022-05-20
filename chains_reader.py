

data=[]

def count_lines(filename, chunk_size=1<<13):
    with open(filename) as file:
        return sum(chunk.count('\n')
                   for chunk in iter(lambda: file.read(chunk_size), ''))

f1=open("D:/bot lib/text/chains.txt", mode="r", encoding="utf-8")
lines=count_lines("D:/bot lib/text/chains.txt")
for i in range(0,lines):
    chain_raw=f1.readline()
    chain_raw=chain_raw.replace('\n','')
    chain_raw.split()
    data.append(chain_raw)
print(data)