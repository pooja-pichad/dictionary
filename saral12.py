# Ek dictionary me 1 se 15 tak saare numbers ki keys banaye aur unke square unn keys ki values ho.

# Output :-

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
# d=dict()
# for i in range(1,16):
#     d[i]=i**2
# print(d)



# d=dict()
# i=0
# while i < 16:
#     d[i]=i**2
#     i=i+1
# print(d)
num1=int(input("entr a number"))
num2=int(input("enter a number"))
d=dict()
i=num1
while i <= num1:
    j=0
    while j<=num2:
       d[i]=i**3
    i=i+1
print(d)



