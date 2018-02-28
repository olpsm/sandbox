s=0
i = 0
while i < 5:
    print('*');s+=1
    if i % 2 == 0:
        print('**'); s+=2
    if i > 2:
        print('***'); s+=3
    i = i + 1
print (s)
