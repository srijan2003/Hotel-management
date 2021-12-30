import datetime
def cal():
	
	global ilist,icost,n,iquan,quan
	n=int(input("enter the total number of items="))
	for i in range(n):
		iname=str(input("enter the item"))
		ilist.append(iname)
		icost.append(item[iname])
		iquan=int(input("enter the quantity="))
		quan.append(iquan)
		
		
ilist=[ ]
icost=[ ]
quan=[ ]
name=str(input("enter the customer name="))
mob=int(input("enter the mobile number="))
item={"idly":5,"dosa":5,"vada":5,"chapathi":10,"parotta":15,"veg briyani":50,"chicken briyani":100,"coffee":15,"Tea":10}
cal( )
print("====bill====")
dtime=datetime.datetime.now( )
print(dtime.strftime("%y-%m-%d/%H:%M:%S"))
print("s.no itemname cost quantity total")
a=1
for j in range(n):
	print(a,end="     ")
	print(ilist[j],end="     ")
	print(icost[j],end="     ")
	print(quan[j],end="      ")
	print(icost[j]*quan[j])
	print( )
	a+=1
sum1=0
for k in range(n):
	m=icost[k]*quan[k]
	sum1+=m
print("The total amount to be paid=",sum1)
vamount=int(input("enter the amount received="))

if sum1==vamount:
	print("Thank you visit again")
else:
	print("Balance amount=",vamount-sum1)
	print("Thank you visit again")
