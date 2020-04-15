for _ in range(int(input())):
    n,m,k = list(map(int,input().split()))
    l=[]
    for i in range(n):
        print(list(map(int,input().split()))[k-1],end=" ")
    
