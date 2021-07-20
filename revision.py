# Ek program likhiye jo ki nested dictionary me se first key or value ko remove ka
Dic= {
        1: 'NAVGURUKUL',
        2: 'IN',  
  	    3:{    
             'A' : 'WELCOME',
             'B' : 'To',
             'C' : 'DHARAMSALA'
            }
        }
del Dic[3]['A']
print(Dic)

# Do lists lekar ek dictionary banaiye jisme pehli list ke elements keys ho aur dusri list ke elements unn keys ki values ho. Example :- Input :-
 

list1=["one","two","three","four","five"]

list2=[1,2,3,4,5,]  
a={}
i=0
while i<len(list1):
    a[list1[i]]=list2[i]
    i=i+1
print(a)
    
# Ek program likhiye jo dictionary me se duplicate keys hata de. Example :- Input :-
 
dic={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3
    } 
x={}
for x ,y in dic.items():
    j=x 
    if x==j:
        print(dic)
        break


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





# User se 10 students ke naam aur marks lekar unhe ek dictionary me store karaye.

# Output :-

# {
#     'sonu':85,
#     'Kartik':90,
#     'Deepak':96,
#     'Aman':76,
#     'Somesh':60,
#     'Umesh':85,
#     'Amarpal':70,
#     'Roshan':57,
#     'Riyaz':98,
#     'Shabid':56
# } 



# i=0
# a={}
# while i<10:
#     name=input("enter a name")
#     marks=int(input("enter a marks"))
#     a[marks]=name
#     i=i+1
# print(a)

a="MISSISSIPPI"
b={}
for i in a:
    if i not in b:
        b[i]=1
    else:
        b[i]+=1
print(b)
    

# Ek dictionary ki value ke sabhi items ko count kijiye jo ki ek list me hai.

# Input :-

dict =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}

count=0
for x in dict :
    if isinstance(dict[x]):
        count +=len(dict[x])
    print(count)