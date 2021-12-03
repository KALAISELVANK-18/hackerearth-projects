ent=int(input())
dic={'0':6,'1':2,'2':5,'3':5,'4':4,'5': 5,'6': 6,'7':3,'8':7,'9':6}
for i in range(0,ent):
    number=input()
    num=0
    for s in range(0,len(number)):
        num+=dic[number[s]]
    s=int(num/2)
    if num%2==0:
        print('1'*(s))
    else:
        print('7'+'1'*int((num-3)/2))
