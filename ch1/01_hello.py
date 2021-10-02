a = input("write name")
b = "abcd"
for x in b:
    a = a.replace(x,"")   
a = a.replace("",".")
c = len(a) - 1 
a = a[:len(a) - 1]
print(a)
