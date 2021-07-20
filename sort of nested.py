a=[[4,2,13],[3,8,5],[9,6,17]]
# output = [17,13,9,8,6,5,4,3,2]
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        b.append(a[i][j])
        b.sort()
        j=j+1
    i=i+1
print(b)
i=1
c=[]
while i<=len(b):
    c.append(b[-i])
    i+=1
print(c)

