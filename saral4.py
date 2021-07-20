# Ek program likhiye jo ki nested dictionary me se first key or value ko remove kare.
#  Example :- Input :- Output :- 


#  output
# Dic= {
    # 1: 'NAVGURUKUL',
    # 2: 'IN',  
  	# 3:
    #   { 'B' : 'To',
    #     'C' : 'DHARAMSALA'
    #    }
    # }
# people= {
#         1: 'NAVGURUKUL',
#         2: 'IN',  
#   	    3:{    
#              'A' : 'WELCOME',
#              'B' : 'To',
#              'C' : 'DHARAMSALA'
#             }
#         }
# del people[3]['A']
# print(people)


# Do lists lekar ek dictionary banaiye jisme pehli list ke elements keys ho aur dusri list ke elements unn keys ki values ho. Example :- Input :-
 

list1=["one","two","three","four","five"]

list2=[1,2,3,4,5,]  
a={}
i=0
while i<len(list1):
      a[list1[i]]=list2[i]
      i=i+1
print(a)
      # i=i+1
