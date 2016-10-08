####### XREVO ######
import sys
def MT () :
    a=int(raw_input(' The number :'))
    b=int(raw_input(' The number You want To check ability Of / '))
    c= a/b
    d=c*b
    e=c*a
    if a == d :
        print ' ________________>YES ' , b
    elif e==a :
        print '________________>>YES'
    else :
        print ' ---------------------------->No '
def MT2():
    print ' Do not WRITE a "String" ' 
    s=int(raw_input('Type The number You want to Check it  :\n------>: ' ))
    a= s /2 
    b=a*2 
    c=s-1  
    d = c /2
    if  b==s :
        print '--->The Number ',s, ' / 2 Because  ',a,'*2=',s
    else :
        print " ---> The Number ",s, "dont \ Because " , s , '=' , '1 + ' , d , '*2'
print ' ----------->Hello Everybody Using My Script :D : \n For Use ability Test of / Type 1 : \n For User IN ChecK type 2 \n For Exit Type 3: : '
select = int(raw_input('===================================> select 1 or 2 or 3:  '))
if select == 1 :
    MT()
elif select == 2 :
    MT2()
else :
     sys.exit        
    
