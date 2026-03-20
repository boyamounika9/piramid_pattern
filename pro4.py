array=[5,8,9,6,4,2]
fl=max(array)
sl=0
for i in array:
    if i<fl and i>sl:
        sl=i
print(sl)
