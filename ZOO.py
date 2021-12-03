aa=input()
count1=0
count2=0

for i in range(len(aa)):
    if aa[i]=='z':
        count1+=1
    if aa[i]=='o':
        count2+=1
if count2==count1*2:
    print('Yes')
else:
    print('No')
