# Ek program likhiye jisse ki niche di hui dictionaries ek hi dictionary me aa jaaye 
# jaise ki niche Expected result me diya gaya hain or jisski bhi keys same hai unki 
# values add ho jai. Example :- Input :- Output :- 
# Edit on Github
# Input :-
# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}

# # Output :-

# {1: 10, 2: 60, 3: 30,  5: 50, 6: 60} 
# from collections import Counter
# for key in dic2:
#     if key in dic1:
#         if key in dic3:
#             dic2[key] = dic1[key] + dic2[key]+dic3[key]

#     else:
#         pass 
# Cdict = Counter(dic3) + Counter(dic2) +Counter(dic1)
# print(Cdict)        


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)
