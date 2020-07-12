from Coalition import Coalition
from Party import Party
from Position import Position
import math

coalitionDict = dict()
parties = list()
AllCoalitions=[[]]
isValidCoalition=True
Values=[24,26,28,30]
N=61
value=0
numOfParties = int(input("Enter number of parties: "))
print("_______________________________________")
for i in range(numOfParties):
    name = input("Enter name for party number " + str(i + 1) + ": ")
    score = int(input("Enter score for "+name+ ": "))
    position=input("Enter political side of the party: ")
    position=position.upper()
    position=position.replace("-","_")
    position = position.replace(" ", "_")
    side=Position[position]
    p = Party(name, score,side)
    parties.append(p)
    print("_______________________________________")
for x in parties:
    AllCoalitions.extend([subset + [x] for subset in AllCoalitions])
for tmp in AllCoalitions:

    totalScoreInCoalitin=0
    for party in tmp:
        totalScoreInCoalitin += party.getScore()
    for x in tmp:
        for y in tmp:
            if (x.getPosition().value == 2 and y.getPosition().value <= 0):
                isValidCoalition=False
            elif x.getPosition().value == -1 and y.getPosition().value > 0:
                isValidCoalition=False

    if totalScoreInCoalitin<N and isValidCoalition==True :
      isValidCoalition=False

    if isValidCoalition==True:
        if totalScoreInCoalitin<66:
            value=Values[0]
        elif totalScoreInCoalitin>=66 and totalScoreInCoalitin<68:
            value=Values[1]
        elif totalScoreInCoalitin>68 and totalScoreInCoalitin< 72:
            value=Values[2]
        else:
            value=Values[3]

        coalition=Coalition(tmp,value)
        key=tuple(coalition.getParties())
        coalitionDict[key]=coalition.getValue()
    isValidCoalition=True
shaply=dict()
for k in coalitionDict:
    print(k)
for party in parties:
    shaplyValue = 0
    for coalition in coalitionDict.keys():
        if party in coalition:
            var1=math.factorial(len(coalition)-1)*math.factorial(len(parties)-len(coalition))
            tmp=list(coalition)
            tmp.remove(party)
            var2=coalitionDict[coalition]-coalitionDict[tuple(tmp)]
            var3=var1*var2
            shaplyValue+=var3
    tmp= 1/math.factorial(len(parties))
    shaplyValue=shaplyValue*tmp
    shaply[party.getName()]=shaplyValue
print(shaply)






