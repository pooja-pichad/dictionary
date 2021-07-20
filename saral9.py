# "MISSISSIPPI" iss word me har letter ki occurrency count karke ek dictionary me store karaye.
#  Jisme letter dictionary ki keys aur occurrency Uss dictionary ki values hongi. Example:- Output :-
 

# {M:1,I:4,S:4,P:2} 
# count = {"M":0,"I":0,"S":0,"P":0}
# word = "MISSISSIPPI"
# for i in word:
# 	if i == "M":
# 		count['M'] = count['M']+1
# 	elif i == "I":
# 		count['I'] = count['I']+1
# 	elif i == "S":
# 		count['S'] = count['S']+1
# 	elif i == "P":
# 		count['P'] = count['P']+1
# print (count)


word = 'mississippi' 
letter={}
for letter in set(word):
    print(letter, ':', word.count(letter),end=" ")

    