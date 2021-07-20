#Removing Elements from a Dictionary:-

# Hum dictionary ke elements ko kahin tareeko se remove kar sakte hain. Jaisa ki niche dikhaya gaya hain. Hum pop( ) method ka use karke specified element ko remove kar sakte hain :
 
# CAR_DETAILS={
#     "brand": "Ford",
#     "model": "jason",
#     "year": 1964
# }
# CAR_DETAILS.pop("model")
# print(CAR_DETAILS) 



# person={
#     'name':'jack',
#     'id':22,
#     'place':'dharamsala'
# }
# person.popitem()
# print(person) 


# states_capitals = {
#   'Gujarat' : 'Gandhinagar',
#   'Maharashtra' : 'Mumbai',
#   'Rajasthan' : 'Jaipur',
#   'Bihar' : 'Patna'
#   }
# for state in states_capitals:
#       print(state) 


# states_capitals = {
#     'Gujarat' : 'Gandhinagar',
#     'Maharashtra' : 'Mumbai',
#     'Rajasthan' : 'Jaipur',
#     'Bihar' : 'Patna'
#     }

# for state in states_capitals:
#     print(states_capitals[state]) 


# details ={
#     "name":  "Bijender",
#     "age":  17,
#     "class":  "10th"
#     }
# for x in details.values():
#     print(x) 


# movie ={
#     "name":  "Puli",
#     "hero":  "Vijay",
#     "rating":  7.5
#     }
# for x,y in movie.items():
#     print(x,y) 


meal ={
    "monday":  "Chole chawal",
    "sunday":  "Fried rice",
    "wednesday":  "dosa"
    }
print(len(meal)) 