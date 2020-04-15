t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    c = 0
    for i in range(0,n):
        l = i-5
        r = i+1
        if l<0:
            l=0
        temp = a[l:r]
        if ( (min(temp)==a[i]) and (temp.count(a[i])==1) ):
            c += 1
    print(c)
        
