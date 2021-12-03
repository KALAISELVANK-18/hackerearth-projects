lent=int(input())
div=lent/2
ar=input()
#divisibility with 11 of num formed by the first and last(2nd half) numbers of given numbers
arr=ar.split(' ')
num=''
for i in range(lent):
    if i<div:
        num+=arr[i][0]
    else:
        num+=arr[i][-1]
if int(num)%11==0:
    print('OUI')
else:
    print('NON')