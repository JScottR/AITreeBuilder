#/bin/python3
import csv
import math

AttributeList = [0,1,2,3,4,5,6]

def getChoices(data, attribute):
    distinctValues = []
    for value in data:
        if value[attribute] not in distinctValues:
            distinctValues.append(value[attribute])
    return distinctValues

def TreeBuilder(AttributeList,Data):
    Tree = []
    currentYes = 0
    currentNo = 0
    for dataValue in Data:
        if dataValue[7] == "Yes":
            currentYes += 1
        else:
            currentNo += 1
    # Check if Leaf Node
    if len(Data) == currentNo or len(Data) == currentYes:
        if currentYes != 0:
            return "Yes"
        else:
            return "No"
    # Just base case 
    if len(AttributeList) == 0:
        return
    bestEntropy = 1
    bestChoice = ""
    ## Need to find attribute that tells us most split on that attribute
    for remainingAttributes in AttributeList:
        attributeEntropy = 0
        ##distinctValues = []
        ##for value in Data:
        ##    if value[remainingAttributes] not in distinctValues:
        ##        distinctValues.append(value[remainingAttributes])
        distinctValues = getChoices(Data, remainingAttributes)
        print(distinctValues)
        for choice in distinctValues:
            print(choice)
            numYes = 0
            numNo = 0
            for allValues in Data:
                print(allValues[7])
                if choice in allValues:
                    if(allValues[7] == "Yes"):
                        numYes += 1
                    else:
                        numNo += 1

            totalNum = numYes + numNo
            if (numYes != 0 and numNo != 0):
                attributeEntropy += (totalNum/20)*((-numYes/totalNum)*math.log2(numYes/totalNum)+(-numNo/totalNum)*math.log2(numNo/totalNum))
            print(attributeEntropy)

        if attributeEntropy < bestEntropy:
            bestEntropy = attributeEntropy
            bestChoice = remainingAttributes
    if (bestChoice != ""):
        currentAttributeList = list(AttributeList)
        currentAttributeList.remove(bestChoice)
        Tree.append(bestChoice)
        attributeChoices = getChoices(Data, bestChoice)
        print(attributeChoices)
        for choice in attributeChoices:
            newData = []
            for dataValue in Data:
                if choice in dataValue:
                    # print(choice)
                    # print(dataValue)
                    newData.append(dataValue)
            # print(newData)
            children = TreeBuilder(currentAttributeList,newData)
            Tree.append([choice,children])
            # print(Tree)
    return Tree
with open('MoviesAIProblem.csv','r') as csvfile:
    fileReader = csv.reader(csvfile)
    data = list(fileReader)
print(data)
decisionTree =  TreeBuilder(AttributeList,data)
print("Tree")
print(decisionTree)
