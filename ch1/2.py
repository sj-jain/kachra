n = int(input("Enter number of coins : "))
a = list(map(int,input("Enter the values : ").strip().split()))[:n]
print(a)
from itertools import combinations
#print("List is - ", a)
g = []
c = []
i = 1
while i <= n:
    comb = list(combinations(a,i))
    print(*comb)
    for x in comb:
        c.append(x)
    t = 0
    while t <= len(c)-1:
        d = (sum(list(c[t]))) 
        if d > sum(a)/2:
            print(i)
            g.append(i)
            break 
        t += 1
    if g == [i]:
        break
    i += 1

        
#t = 0
#while t <= len(c):
    #d = (sum(list(c[t]))) 
    #if d > 1:
      #  print(1)
       # break
   # else:
        #print("error")
   # t += 1
