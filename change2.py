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
    change=change-(n50*50)
    print("Fifty Pound Notes",n50)
if change>=20:
    n20= int(change/20)
    change=change-(n20*20)
    print("Twenty Pound Notes",n20)
if change>=10:
    n10= int(change/10)
    change=change-(n10*10)
    print("Ten Pound Notes",n10)
if change>=5:
    n5= int(change/5)
    change=change-(n5*5)
    print("Five Pound Notes",n5)
if change>=2:
    n2= int(change/2)
    change=change-(n2*2)
    print("Two Pound Coins",n2)
if change>=1:
    n1= int(change/1)
    change=change-(n1*1)
    print("One Pound Coins",n1)

if n50>=1:
    
if n20>=1:
    print("Twenty Pound Notes",n20)
if n10>=1:
    print("Ten Pound Notes",n10)
if n5>=1:
    print("Five Pound Notes",n5)
if n2>=1:
    print("Two Pound Coins",n2)
if n1>=1:
    print("One Pound Coins",n1)