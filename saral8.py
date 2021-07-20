# User se 10 students ke naam aur marks lekar unhe ek dictionary me store karaye.

# Output :-

# {
#     'sonu':85,
#     'Kartik':90,
#     'Deepak':96,
#     'Aman':76,
#     'Somesh':60,
#     'Umesh':85,
#     'Amarpal':70,
#     'Roshan':57,
#     'Riyaz':98,
#     'Shabid':56
# } 

i=0
a={}
while i <10:
    name=input("enter a name")
    marks=int(input("enter a marks"))
    a[name]=marks
    i=i+1

print(a)


a={}
for i  in range(10):
    name=input("enter a name ")
    marks= int(input("enter a marks "))
    a[name]=marks
print(a)