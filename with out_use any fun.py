a={1:3,4:5,3:8,6:7}


# with out using key function

for i in a :
    print(i)



# with out using values fun 
for i in a :
    print(i,a[i])



# with out using del fun

dict = {"Hello": 56,
                  "at": 23,
                  "test": 43,
                  "this": 43}



a='this'
b={}
for key,value in dict.items():
    if key is not a:
        b[key]=value
dict=b
print(dict)


# with out use update add any value
a={1:2,3:4,4:6}
a[5]=7
print(a)


# dictionary item value dikhegi
print(a[1])


# with fun keys
x=a.keys()
print(x)

# with fun values

x=a.values()
print(x)


# del fun use
del a[1]
print(a)

# pop fun
a.pop(3)
print(a)

# popitem fun
a.popitem()
print(a)



