n = input()
fi = input()
se = input()
fi1 = fi.split(' ')
se1 = se.split(' ')


def split(list):
    array = []
    if len(list) == int(n):

        for i in range(0, len(list)):
            array.append(int(list[i]))
    return array


arr1 = split(fi1)
ar1=[]
for i in range(len(arr1)):
    ar1.append(arr1[i])
arr2 = split(se1)


dum=0





if arr1.count(arr1[0])==len(arr1):
    print(0)
    dum+=1
aa=min(arr1)
iii=arr1.index(min(arr1))

zoo=0
def repeat(call):
    if True:
        try:
            no_ways = 0
            global zoo
            for i in range(len(arr1)):
                while arr1[i]!=call:
                    if arr1[i]>=arr2[i]:
                        arr1[i]-=arr2[i]
                        no_ways+=1
                    else:
                        break

            if arr1.count(arr1[0])==len(arr1):

                print(no_ways+zoo*arr2[iii])

            else:

                for i in range(len(arr1)):
                    if i==iii:
                        arr1[iii]-=arr2[iii]
                    else:
                        arr1[i]=ar1[i]


                zoo+=1
                call-=arr2[iii]
                repeat(call)
        except RecursionError:
            print(-1)
        finally:
            pass

repeat(min(arr1))



