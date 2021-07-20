# Ek dictionary ki value ke sabhi items ko count kijiye jo ki ek list me hai.

# Input :-

dict =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}

# Output :-

# total count:5

sum=[]
count=0
for x in dict.values():
   sum=sum+x
print(sum)
i=0
while i<len(sum):
   a=sum[i]
   count=count+1
   i=i+1
print(count)   



conter = sum(map(len, dict.values()))        
print(conter)



# A Map is a Value that provides instructions on how to locate another values.
#  all collections that allow non linear access (ie only get first or get last) are a Map, 
#  as even a simple Array has an index that maps to the correct value.