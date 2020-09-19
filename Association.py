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

'''

Apriori Algorithm

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

attributes = set()
for i in ageVCat:
    for j in ageVCat[i]:
        attributes.add(j)

supportCount = int(input('Enter the Support Count '))

C = []              # C matrix
L = []              # L matrix 
notNullFlg = True

C.append({})        # C 1 
for i in ageVCat:
    for j in ageVCat[i]:
        if j in C[0]:
            C[0][j] += 1
        else:
            C[0][j] = 1
L.append({})        # L 1
for i in C[0]:
    if C[0][i] >= supportCount:
        L[0][i] = C[0][i]
#print(C)
#print(L)

# length = 2
C.append({})        # C 2
lis = list(L[0])
for i in range(len(lis)-1):
    for j in range(i+1, len(lis)):
        C[1][(lis[i],lis[j])] = 0
#print(C[1])
for i in C[1]:
    for j in ageVCat:
        if i[0] in ageVCat[j] and i[1] in ageVCat[j]:
            C[1][i] += 1
L.append({})        # L 2
for i in C[1]:
    if C[1][i] >= supportCount:
        L[1][i] = C[1][i]
#print(L[1])

length = 2        
while len(L[-1]) > 0 and length <= len(attributes):   # For length > 2
    length += 1
    lis = list(L[-1])
    temp = []
    for i in range(len(lis)-1):
        for j in range(i+1,len(lis)):
            if len(set(list(lis[i])+list(lis[j]))) == length:
                temp.append(set(list(lis[i])+list(lis[j])))
    C.append({})        # C matrix
    for i in temp:
        C[-1][tuple(i)] = 0
    #print(C[-1])
    for ele in C[-1]:
        flg = True
        for ele1 in ageVCat:
            flg = True
            #print('Hai')
            for i in ele:
                #print('i loop')
                if i not in ageVCat[ele1]:
                    flg = False
                    break
            if flg :
                C[-1][ele] += 1
    #print(C[-1])
    L.append({})        # L matrix
    for i in C[-1]:
        if C[-1][i] >= supportCount:
            L[-1][i] = C[-1][i]
#print(L[-1])        # Filal Set is empty
print(L[-2])        # Final Rules

if len(L) > 2:
    confidence = float(input("Entere your confidence value "))
#    total3 = 0
#    total2 = 0
    total = 0
    for i in L[0]:
        total += L[0][i]
#   for i in L[-2]:
#        total2 += L[-2][i]
#    for ele in L[-3]:
#        total3 += L[-3][ele]
    for record in L[-2]:
        lis = []
        lisRec = list(record)
        for i in range(len(record)):
            if len(record) > 2:
                lis.append((tuple(lisRec[0:i]+lisRec[i+1:]),lisRec[i]))
            else:
                if i == 0:
                    lis.append((lisRec[1],lisRec[0]))
                else:
                    lis.append((lisRec[0],lisRec[1]))
        for i in lis:
            if i[0] in L[-3]:
                if (L[-2][record]*100.0)/(L[-3][i[0]]*1.0) >= confidence:
                    # Using Support Count
                    print(i[0],"->",i[1]," has confidence of",(L[-2][record]*1.0)/(L[-3][i[0]]*1.0)*100.0,"%")
                    print(i[0],"->",i[1]," has lift of",(L[-2][record]*1.0)/(L[-3][i[0]]*L[0][i[1]]/total))
                    '''
                if (L[-2][record]*1.0/total2)/(L[-3][i[0]]*1.0/total3) >= confidence:
                    # Using Support
                    print(i[0],"->",i[1]," has confidence of",(L[-2][record]*1.0/total2)/(L[-3][i[0]]*1.0/total3)*100.0,"%")
                    print(i[0],"->",i[1]," has lift of",(L[-2][record]*1.0/total2)/(L[-3][i[0]]*1.0/total3*L[0][i[1]]/total)*100.0)
                    '''
else:
    print("No Association Found")