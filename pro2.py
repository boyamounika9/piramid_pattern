name="mounika"
reverse=len(name)*" "
for i in name:
    for j in range(-1,-(len(name)),-1):
        reverse[j]+=i
        continue
print(reverse)


