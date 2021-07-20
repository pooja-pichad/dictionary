# Ek program likhiye jo dictionary me se duplicate keys hata de. Example :- Input :-
 
dic={
    "ball":"red",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3
    } 
# del dic["ball"]
# print(dic)


result={}
for key,value in dic.items():
    if value not in result.values():
        result[key]=value
print(result)


