lent=int(input())
ar=input()
#find the mod of the num formed by last numbers of the given numbers with 10
arr=ar.split(' ')
arr1=''
for i in range(0,lent):
    arr1+=arr[i][-1]
if int(arr1)%10==0:
    print('Yes')
else:
    print('No')    