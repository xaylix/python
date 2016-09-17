from datetime import*
import sys
def school():
	today=datetime.today
	print today()
	print " The School Studentplan : "
	day=raw_input( " -----> Please input The Day Number : ")
	day=int(day)
	assert day==int(day)
	D1 =  "  ->|8-10 Clear | 10 --> 12 3ndk Lmath | 2-4 clear | 4-->6 3ndk Physic "
	D2 =  "  -->|8-10 Clear | 10->11 HG | 11 --> 12 Islamic | 2 ->3 A | 3->4 F | 4->5 EN | 5->6 M | "
	D3 =  "  --->| 8-9 SVT G1 | 9-10 PC G2 | 10-11 PC G1 | 11-12 SVT G2 | 2-4  FR | 4-6 Clear *_* "
	D4 =  "  ---->| 8-9 EPS | 9-10 Islamic | 10-12 PH | 2-4 Clear | 4-5 EN | 5-6 F ^_^ "
	D5 =  "  ----->| 8-10 M | 10-11 SVT | 11-12  EN | l3chya dSPAMING :D "
	D6 =  "  ------>| 8-10 Clear | 10 - 12 THE FUCKING INF |  2-3 Clear | 3-4 HG | 4-5 A | 5-6 | "
	if day==1:
		print D1
	elif day==2:
		print D2
	elif day ==3:
		print D3
	elif day ==4:
		print D4
	elif day ==5:
		print D5
	elif day ==6:
		print D6
	else:
		print " 404 Not Found "
try:
	school()
except ValueError:
	print "Select Number !"
	sys.exit()