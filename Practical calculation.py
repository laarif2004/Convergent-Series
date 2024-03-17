n=10000000
s=0
for i in range(1,n):
    s=s+1/(i*(i+1))
    if i>n-6:
        print(s)
