# Ek list lijiye aur uske andar dictionaries me keys and values likhiye jaisa ki niche
#  dikhaya gaya hai (Sample Data) aur uske baad saare unique values ko ek list me print karaye.
#   Example :- Input :-
 
L=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
] 

a={}
c=[]
i=0
while i<len(L):
     a.update(L[i])
     i+=1
for i in a.values():
     if i not in c:
          c.append(i)
print(c)




u_value = set( val for dic in L for val in dic.values())
print("Unique Values: ",u_value)

# set used
# they are important for building more complex mathematical structure.