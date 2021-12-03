te = int(input())
for i in range(te):
    cou = 0
    n = int(input())
    z = input()
    li = z.split(' ')
    li1 = []
    for z in range(n):
        li1.append(int(li[z]))
    maxi = max(li1)
    for a in range(1, maxi + 1):
        if li1.count(a) == a:
            cou += 0
        if li1.count(a) < a:
            co = a - li1.count(a)
            cou+=min(co,li1.count(a))
        if li.count(str(a)) > a:
            co =  li1.count(a)-a
            cou += min(co, li1.count(a))
    print(cou)
