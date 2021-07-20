dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# Expected output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

i=0
while i<len(dict1):
    dict3 = {**dict1, **dict2}           
    i=i+1
print(dict3)


# **
#  **kwargs. 
#  In this way, we can add multiple length arguments to one dictionary in a single statement.

# result={}
# for key,value in dict1.items():
#     if key  not in dict2.values():
#         result[key]=value
# print(result)


