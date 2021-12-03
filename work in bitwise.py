te=int(input())
#using powers and bitwise and opertor
for i in range(te):
	n=int(input())
	num1=int(input())
	num2=int(input())
	x=input()
	y=input()
	xx=x.split(' ')
	yy=y.split(' ')
	arrx=[]
	arry=[]
	count=0
	for z in range(2):
		if z==0:
			for a in range(len(xx)):
			    arrx.append(int(xx[a]))
		if z==1:
			for t in range(len(yy)):
			    arry.append(int(yy[t]))

	for ar in range(len(arrx)):
		for arr in range(len(arry)):
			q=(arrx[ar]^arry[arr])&num1
			qq=(arrx[ar]^arry[arr])&num2
			if q==qq:
				count+=1
	print(count)