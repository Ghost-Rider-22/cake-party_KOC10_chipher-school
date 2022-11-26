cakeangle=360
N=eval(input("Enter Number of cuts: "))
# First case
if(cakeangle%N==0):
    print("YES the cake will cut in equal pieces of size",N)
else:
    print("NO the cake will not cut in equal pieces of size",N)
#Second case
if(N>cakeangle): #Only when N is greater tha cake angle cake can't be cut into pieces
    print("NO the cake will not cut in piece of any size",N)
else:
    print("YES the cake will cut in piece of any size",N)
n=1 # Third case
for i in range(N):
    cakeangle-=n
    n+=1
    if(cakeangle<0):
        print("NO the cake will not cut into pieces such that no two of them are equal",N)
        break
else:
        print("YES the cake will cut into pieces such that no two of them are equal",N)
