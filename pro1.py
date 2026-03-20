name="mounika"
vowel=0
cons=0
for i in name:
    if i in ("a","e","i","o","u","A","E","O","U","I"):
        vowel+=1
    else:
        cons+=1
print("vowel:",vowel)
print("consonant:",cons)