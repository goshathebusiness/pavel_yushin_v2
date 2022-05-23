nongrata={',':'','.':'','—':'','!':'','?':'','<':'','>':'','«':'','»':'','(':'',')':'','[':'',']':'','{':'','}':'','…':'',' ':''}
nongrata_lite={'—':'','<':'','>':'','«':'','»':'','(':'',')':'','[':'',']':'','{':'','}':'','…':'...',' ':'','"':''}
result=[]
chains=[]

f1=open("D:/bot lib/text/data_raw.txt", mode="r", encoding="utf-8")
raw=f1.read()
f1.close()
main=raw.split()
for i in main:
    for j, k in nongrata_lite.items():
        i=i.replace(j,k)
        i=i.lower()
        pass
    main.pop(0)
    main.append(i)
f2=open("D:/bot lib/text/chains_raw.txt", mode="w", encoding="utf-8")
for i in range(0,len(main)):
    f2.write(main[i]+' ')
    try:
        f2.write(main[i+1]+'\n')
    except:
        f2.write(main[0])
f2.close()