import math
#find hexadecimal within the given range and add up after that find gcd and then find total of gcd of the range
te=int(input())
dic={'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
for i in range(te):
    fi=input()
    rang=fi.split()

    total=0
    for b in range(int(rang[0]),int(rang[1])+1):
        z=hex(b)

        s=str(z)
        ne=s[2:]
        print(ne)
        add=0
        for t in ne:
            if t in('a','b','c','d','e','f'):
                add+=dic[t]
            else:
                add+=int(t)
        gc=math.gcd(b,add)
        if gc>1:
            total+=1
    print(total)