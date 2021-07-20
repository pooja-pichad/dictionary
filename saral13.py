# Ek code likhiye jo dictionary ki 3 highest value print karaye. Example :-
 
my_dict = {
    'a':50, 
    'b':58,
    'c':56,
    'd':40,
    'e':100, 
    'f':20
    } 

#  expect result:-['e','b','c']

from collections import Counter
a=[]
# Counter=my_dict
k = Counter(my_dict)
high = k.most_common(3) 
print(my_dict, "\n")
for i in high:
    # print(i[0],end=" ")
    a.append(i[0])
print(a)


# my_list=[]
# my_list_key=[]
# for i in range(3):
#     max_1=0
#     for value in my_dict:
#         if max_1<my_dict[value]:
#             max_1=my_dict[value]
#             key=value
#     my_list.append(max_1)
#     my_list_key.append(key)
#     my_dict.pop(key)
# # print(my_list)
# print(my_list_key)
