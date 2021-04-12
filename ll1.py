firstSets = {}
nextSets = {}

def firstOf(grammar, terminals, noTerminals, OPERATOR_SYMBOL):
    for k in range(5):
        for g in grammar:
            temp = []
            for i in range(len(g[1])):
                if g[1][0] in terminals and g[1][0] not in temp:
                    temp.append(g[1][0])
                if g[1][i] == OPERATOR_SYMBOL:
                    if g[1][i+1] in terminals and g[1][i+1] not in temp:
                        temp.append(g[1][i+1])
                    if g[1][i+1] in noTerminals and firstSets.get(g[1][i+1]) != temp:
                        temp = (firstSets.get(g[1][i+1]))
                if g[1][0] in noTerminals and firstSets.get(g[1][0]) != temp:
                    temp = firstSets.get(g[1][0])
                    print(g[1][0])
                    print(temp)
                if temp is None:
                    temp = []
            firstSets[g[0]] = temp
            #print(g[0])
            #print(firstSets[g[0]])
    print(grammar)
    print(firstSets)

def nextOf(grammar, terminals, noTerminals, first_symbol, EPSILON):
    for k in range(10):
        for g in grammar:
            temp = []
            for g2 in grammar:
                for i in range(len(g2[1])):
                    try:
                        if g[0] == first_symbol and '$' not in temp:
                                temp.append('$')
                        if g2[1][i] == first_symbol and g2[1][i+1] in terminals:
                            temp.append(g2[1][i+1])
                        if g[0] == g2[1][i] and g2[1][i+1] in terminals and g2[1][i+1] not in temp:
                            temp.append(g2[1][i+1])
                        if g[0] == g2[1][i]:
                            if g2[1][i+1] in noTerminals:
                                temp = firstSets.get(g2[1][i+1]) 
                                if EPSILON in temp:
                                    temp.remove(EPSILON)
                                    temp += nextSets.get(g2[0])
                            if g2[1][i+1] == '|' and g2[0] != g2[1][i]:
                                temp = nextSets.get(g2[0])
                    except: 
                        temp = nextSets.get(g2[0])
            
            nextSets[g[0]] = temp
            
    print(nextSets)