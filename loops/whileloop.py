n=int(input())
i=1
count=0
while n>=i:
    if n%2==0:
        count+=1
    n-=1
print(count)