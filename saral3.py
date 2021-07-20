# Ek program likhiye jo ki dictionaries ki values ka sum print kare.
#  Example :- Input :- Output :- 
# my_dict = {
#         'data1':100,
#         'data2': -54,
#         'data3': 247
#        } 

# values=my_dict.values()
# totalsum=sum(values)
# print(totalsum)



my_dict = {
        'data1':100,
        'data2': -54,
        'data3': 247
       } 
# print(sum(my_dict.values()))
sum=0
for i in my_dict:
        sum=sum+my_dict[i]
print(sum)
