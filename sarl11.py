# Ek code likhiye jo dictionary ki 3 highest value print karaye.
# 
# Input :-

my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }

# Output :-

# [58,56,100]


my_list=[]
my_list_key=[]
for i in range(3):
    max=0
    for value in my_dict:
        if max<my_dict[value]:
            max=my_dict[value]
            key=value
    my_list.append(max)
    my_list_key.append(key)
    my_dict.pop(key)
print(my_list)
# print(my_list_key)

