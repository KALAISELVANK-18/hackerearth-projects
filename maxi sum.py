te = int(input())
for i in range(te):

    u = input()
    a = u.split(' ')
    z = input()
    q = z.split(' ')
    ar = []
    for h in q:
        ar.append(int(h))
    lo = 0
    ex = int(a[1])
    ne = []
    while len(ar) != 0:

        t = ar.count(max(ar))
        gh = t * max(ar)
        ne.append(gh)
        for s in range(t):
            a = ar.index(max(ar))
            del (ar[a])

    for i in range(ex):
        if len(ne) != 0:
            if max(ne) > 0:
                lo += max(ne)
            d = ne.index(max(ne))
            del (ne[d])
        else:
            break

    print(lo)