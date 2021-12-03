import sys
#find least and highest factor of the given powers
te=int(sys.stdin.readline())
for h in range(te):
    fi=sys.stdin.readline()
    dc=list(map(int,sys.stdin.readline().split(' ')))
    dv=list(map(int,sys.stdin.readline().split(' ')))
    dc.sort()
    dv.sort(reverse=True)
    maxi=1
    mini=1
    for vu in range(len(dc)):
        maxi=((maxi%1000000007) * ((((dc[vu]+1)%1000000007)*((dv[vu]+1)%1000000007))%1000000007)%1000000007)%1000000007
        '''deep=((dc[vu]%1000000007)+((dv[vu])+1)%1000000007)%1000000007'''
        mini=(((mini%1000000007)*(dc[vu]+dv[vu]+1)%1000000007)%1000000007)
    print(mini, maxi)