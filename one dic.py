# Q2. Write a python programs to join/merge/concatenate the following two dictionaries and create the new dictionary.
d1 = {1: "Amit", 2 : "Suman"}
d2 = {4 : "Ravi", 5 : "Kamal"}
# New dictionary = {1: “Amit”, 2 : “Suman”, 4 : “Ravi”, 5 : “Kamal”}
# Solution:

d1 = {1 :"Amit",2 : "Suman"}

d2 = {4:"Ravi", 5 : "Kamal"}

d3={ }

for i in (d1,d2):

  d3.update(i)

print(d3)