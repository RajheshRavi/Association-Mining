import pandas as pd

dataFrame = pd.read_csv('googleplaystore.csv')

'''

Apriori Algorithm

'''
def split(a):
    if int(a)+.5 <= a :
        return int(a)+.5
    else:
        return int(a)

ratVCat = {}
dataFrameFillNan = dataFrame['Rating'].fillna(1)
for i in range(len(dataFrameFillNan)):
    #print(dataFrame['Content Rating'][i],dataFrame['Category'][i])
    if split(dataFrameFillNan[i]) in ratVCat :
        if dataFrame['Category'][i] not in ratVCat[split(dataFrameFillNan[i])]:
            #print(dataFrame['Content Rating'][i],dataFrame['Category'][i])
            ratVCat[split(dataFrameFillNan[i])].append(dataFrame['Category'][i])
    else:
        ratVCat[split(dataFrameFillNan[i])] = [dataFrame['Category'][i]]
print(ratVCat)

attributes = set()
for i in ratVCat:
    for j in ratVCat[i]:
        attributes.add(j)

supportCount = int(input('Enter the Support Count '))

C = []              # C matrix
L = []              # L matrix 
notNullFlg = True

C.append({})        # C 1 
for i in ratVCat:
    for j in ratVCat[i]:
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
    for j in ratVCat:
        if i[0] in ratVCat[j] and i[1] in ratVCat[j]:
            C[1][i] += 1
L.append({})        # L 2
for i in C[1]:
    if C[1][i] >= supportCount:
        L[1][i] = C[1][i]
#print(L[1])

length = 2        
while len(L[-1]) > 0 and length <= len(attributes):   # For length > 2
    length += 1
    print(length)
    print(len(L[-1]),"Length of L")
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
        #print(ele)
        flg = True
        for ele1 in ratVCat:
            flg = True
            #print('Hai')
            for i in ele:
                #print('i loop')
                if i not in ratVCat[ele1]:
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