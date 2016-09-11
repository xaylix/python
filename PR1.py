print "1-Repeat Number:\n2-Repeat Name:\n3-Luck Game:"
ch=raw_input(" ------------->Select 1 or 2 or 3 : ")
ch = int(ch)
if ch ==1:
	r1s=raw_input("input Number You want to Repeat :")
	r1s=int(r1s)
	r2s=raw_input("Input The number of times to repeat ")
	r2s=int(r2s)
	for i in range(0,r2s):
		print r1s
elif ch ==2:
    r3s=raw_input("input Number You want to Repeat :")
    r3s=str(r3s)
    r4s=raw_input("Input The number of times to repeat ")
    r4s=int(r4s)
    for i in range(0,r4s):
    	print r3s
elif ch ==3 :
    import random
P1=random.randrange(1,3)
P2=input('input Your Numer beetwen 1-3 : ')
if P1==P2:
    print"Nice Luck"
else:
    print"No THE Number is : ",P1
