import sys
te=int(sys.stdin.readline())
for j in range(te):
    gh=int(sys.stdin.readline())
    jk=list(map(int,sys.stdin.readline().split(' ')))
    jk.sort()
    fg=int(gh/2)
    fi=jk[0:fg]
    se=jk[fg:]
    cc=se[0]-fi[-1]+1
    print(cc)