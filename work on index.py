q = int(input())
#sum of index must be less than the lenth of the list hence find the max sum of the list satisfing the condition
li = input()
lis1 = li.split(' ')
lis = []
maxi = []
for i in range(0, q):
    lis.append(lis1[i])
for i in range(1, q + 1):
    sum = 0
    su = 0
    loop = 0
    indli = []
    s = 0
    for z in range(1, q + 1):

        if loop + (s + 1) <= len(lis):
            su += 1
            loop += z


        if loop > len(lis):
            break
        s = z

    for a in range(0, loop):
        sum += int(lis[a])

    maxi.append(sum)
    del (lis[0])
print((maxi))