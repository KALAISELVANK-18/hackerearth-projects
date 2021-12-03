import sys

te = int(sys.stdin.readline())
for h in range(te):
    cc = int(sys.stdin.readline())
    coun = 0
    li1 = [1, 4, 10, 18]
    li2 = [8, 14, 17, 18]

    if cc >= 5:
        dif = cc % 5
        div = cc / 5
        if dif == 0:
            coun += div * 27 + ((div - 1) * 18)
        else:
            difi = cc - dif
            divi = difi / 5
            coun += divi * 27 + ((divi - 1) * 18)
            coun += li1[dif - 1] + li2[dif - 1]
        print(int(coun))
    else:
        print(li1[cc - 1])


