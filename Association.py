import pandas as pd

dataFrame = pd.read_csv('googleplaystore.csv')
'''
category = {}

for i in dataFrame['Category']:
    if i in category:
        category[i] += 1
    else:
        category[i] = 1
print(category)

age = {}
for i in dataFrame['Content Rating']:
    if i in age:
        age[i] += 1
    else:
        age[i] = 1
print(age)
'''
ageVCat = {}
for i in range(len(dataFrame['Content Rating'])):
    #print(dataFrame['Content Rating'][i],dataFrame['Category'][i])
    if dataFrame['Content Rating'][i] in ageVCat :
        if dataFrame['Category'][i] not in ageVCat[dataFrame['Content Rating'][i]]:
            #print(dataFrame['Content Rating'][i],dataFrame['Category'][i])
            ageVCat[dataFrame['Content Rating'][i]].append(dataFrame['Category'][i])
    else:
        ageVCat[dataFrame['Content Rating'][i]] = [dataFrame['Category'][i]]
print(ageVCat)
        
supportCount = int(input('Enter the Support Count '))

C = []
L = []
notNullFlg = True

C.append({})
for i in ageVCat:
    for j in ageVCat[i]:
        if j in C[0]:
            C[0][j] += 1
        else:
            C[0][j] = 1
L.append({})
for i in C[0]:
    if C[0][i] >= supportCount:
        L[0][i] = C[0][i]
#print(C)
#print(L)

# length = 2
C.append({})
lis = list(L[0])
for i in range(len(lis)-1):
    for j in range(i+1, len(lis)):
        C[1][(lis[i],lis[j])] = 0
#print(C[1])
for i in C[1]:
    for j in ageVCat:
        if i[0] in ageVCat[j] and i[1] in ageVCat[j]:
            C[1][i] += 1
L.append({})
for i in C[1]:
    if C[1][i] >= supportCount:
        L[1][i] = C[1][i]
print(L[1])
        
'''
while len(L[-1]) > 0:
    length += 1
    lis = list(L[-1])
    setTemp = set()
    lis = []
    for i in range(len(lis)-1):
        setTemp = set()
        for ele in L[-1][lis[i]]:
            setTemp.add(ele)
        for j in range(i+1,len(lis)):
            for ele in L[-1][lis[j]]:
                setTemp.add(ele)
                if len(setTemp) == length:
                    lis.append(setTemp)
                setTemp = set(ele)
    print(lis)
    break
'''            
    