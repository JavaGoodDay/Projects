bill=int(input("enter bill:"))
paid=int(input("enter amount paid:"))

n50=0
n20=0
n10=0
n5=0
n2=0
n1=0

change=paid-bill

if change>=50:
    n50= int(change/50)
if change-(n50*50)>=20:
    n20= int((change-(n50*50)/20)
if change-(n50*50)-(n20*20)>=10:
    n10= int((change-(n50*50)-(n20*20)/10)
if change-(n50*50)-(n20*20)-(n10*10)>=5:
    n5= int((change-(n50*50)-(n20*20)-(n10*10)/5)
if change-(n50*50)-(n20*20)-(n10*10)-(n5*5)>=2:
    n2= int((change-(n50*50)-(n20*20)-(n10*10)-(n5*5)/2)
if change-(n50*50)-(n20*20)-(n10*10)-(n5*5)-(n2*2)>=1:
    n1= int((change-(n50*50)-(n20*20)-(n10*10)-(n5*5)-(n2*2)/1)



print("Fifty Pound Notes",n50)
print("Twenty Pound Notes",n20)
print("Ten Pound Notes",n10)
print("Five Pound Notes",n5)
print("Two Pound Coins",n2)
print("One Pound Coins",n1)