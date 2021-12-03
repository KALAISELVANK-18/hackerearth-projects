te = int(input())
#make the array as sorted up to the given index by adding one to the num until it is greater than or equal to
#the previous number
for i in range(te):
    le = int(input())
    arr = input()
    arrr = arr.split(' ')
    arr1 = []
    zo = 0
    for x in range(le):
        arr1.append(int(arrr[x]))
    for a in range(le - 1):
        nu = arr1[zo + 1]
        while True:
            if arr1[zo + 1] >= arr1[zo] and arr1[zo + 1] % nu == 0:
                break
            else:
                arr1[zo + 1] += 1
        zo += 1

    print(arr1)