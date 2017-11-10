#/bin/python3

AttributeList = [0,1,2,3,4,5]

def TreeBuilder(AttributeList,Data):
    Tree = []
    currentYes = 0
    currentNo = 0
    for dataValue in Data:
        if dataValue[6] == "Yes":
            currentYes += 1
        else:
            currentNo += 1
    # Check if Leaf Node
    if len(Data) == (currentNo or currentYes):
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
        distinctValues = []
        for value in Data:
            if value[remainingAttributes] not in distinctValues:
                distinctValues.append(value[remainingAttributes])
        for choice in distinctValues:
            numYes = 0
            numNo = 0
            for allValues in Data:
                if choice in allValues:
                    if(allValues[6] == "Yes"):
                        numYes += 1
                    else:
                        numNo += 0

            totalNum = numYes + numNo
            attributeEntropy += (totalNum/20)*EntropyValue

        if attributeEntropy < bestEntropy:
            bestEntropy = attributeEntropy
            bestChoice = remainingAttributes
    if (bestChoice != ""):
        AttributeList.remove(bestChoice)
        Tree.append(bestChoice)
