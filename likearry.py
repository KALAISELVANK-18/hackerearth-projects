te = int(input())
for i in range(te):
    coun = 0
    n = int(input())
    z = input()
    li = z.split(' ')
    li1 = []
    for z in range(n):
        li1.append(int(li[z]))
    maxi = max(li1)
    chli=list(range(1,maxi+1))
    print(chli)
    print(li1)
    for a in range(maxi):
        if chli[0] in li1:
            if li1.count(chli[0]) ==chli[0]:
                coun += 0
            if li1.count(chli[0]) < chli[0]:
                co = chli[0] - li1.count(chli[0])
                if chli[0] > co:
                    coun += co
                elif co > chli[0]:
                    coun += chli[0]
                else:
                    coun += co

            if li.count(chli[0]) > chli[0]:
                co = li.count(chli[0]) -chli[0]
                if chli[0] > co:
                    coun += co
                elif co > chli[0]:
                    coun += chli[0]
                else:
                    coun += chli[0]
            del(chli[0])
        else:
            pass
    print(coun)
