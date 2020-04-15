from collections import defaultdict 

for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    total=0
    po2=[]

    for i in range(n):
        x=l[i]
        if x%2==1:
            po2.append(0)
        else:
            if x%4==0:
                po2.append(2)
            else:
                po2.append(1)
    

    Sum=1
   
    prevSum = defaultdict(lambda : 0) 
    
    res = 0 
    
    currsum = 0 
    
    for i in range(0, n):   
    
        currsum += po2[i]  
      
        if currsum == Sum:   
            res += 1         
    
         
          
        if (currsum - Sum) in prevSum: 
            res += prevSum[currsum - Sum]  
            
    
         
        prevSum[currsum] += 1 
       
    total = (( n*(n+1) )//2) - res
    print(total)
        

 
    
   
    
    
