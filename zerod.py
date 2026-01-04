t1=(1,2,5,7,9,2,4,6,8,10)
half=len(t1)//2
print("first half of t1:",t1[:half])
print("@nd half of t1:",t1[half:])
t2=tuple(x for x in t1 if x %2==0)
print("Tuple with even valiues are",t2)
t3=(11,13,15)
c=t1+t3
print("concatenated:",c)
print("max of t1:",max(t1))
print("Min of t1:",min(t1))
