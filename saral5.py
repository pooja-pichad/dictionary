# Do lists lekar ek dictionary banaiye jisme pehli list ke elements keys ho aur dusri 
# list ke elements unn keys ki values ho. Example :- Input :-
 

list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,] 
a={}
i=0
while i<len(list1):
    a[list1[i]]=list2[i]
    i=i+1
print(a)
