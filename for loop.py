l=[1,2,3,4,5,6,7]
for i in range(0,len(l)):
    if i==2:
         continue
    else:
        print(l[i])
print('*'*50)

for i in range(0,len(l)):
    if i==2:
        break
    else:
        print(l[i])

