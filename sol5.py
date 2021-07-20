# Hum square brackets ka use karke dictionary ke values ko access kar sakte hain. 
# Jaisa ki niche dikhaya gaya hai. Example 1:-
 
person={
    'name':'jack',
    'age':20,
    'gender':'male',
    4:'organisation'}

result = person['age'] 
x = person.get("gender")
print(person[4])
print(x)
print(result) 