
nongrata={',':'','.':'','—':'','!':'','?':'','<':'','>':'','«':'','»':'','(':'',')':'','[':'',']':'','{':'','}':'','…':'',' ':''}
#nongrata='-,.—!?<>«»'


def a1():
    result=[]
    f1=open("D:/bot lib/text/data_raw.txt", mode="r", encoding="utf-8")
    raw=f1.read()
    f1.close()
    main=raw.split()
    for i in main:
        for j, k in nongrata.items():
            i=i.replace(j,k)
            i=i.lower()
        result.append(i)
    f2=open("D:/bot lib/text/data_cooked.txt", mode="w", encoding="utf-8")
    result.sort()
    result_set=set(result)
    for i in result_set:
        count=result.count(i)
        f2.write(str(count))
        f2.write(':')
        f2.write(str(i))
        f2.write('\n')
    f2.close()



a1()
