# Ek program likho jo ki dictionaries ki values ko sort(ascending or descending) kar de.

# Input :-

# dict={'bijender':45,'deepak':60,'param':20,'anjali':30,'roshini':50}

# Expected result in Ascending Order:

# {'param':20,'anjili':30,'bijender':45,'roshini':50,'deepak':60}

# Expected result in Descending Order:

# {'deepak':60,'roshini':50,'bijender':45,'anjili':30,'param':20}

    
dict={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
sorted_values=sorted(dict.values())
sorted_dict={}
for i in sorted_values:
    for k in dict.keys():
        if dict[k]==i:
            sorted_dict[k]=dict[k]
            break
print(sorted_dict)