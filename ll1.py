firstSets = {}
nextSets = {}

def firstOf(grammar, terminals, noTerminals, OPERATOR_SYMBOL):
    for k in range(10):
        for g in grammar:
            temp = []
            for i in range(len(g[1])):
                if g[1][0] in terminals and g[1][0] not in temp:
                    temp.append(g[1][0])
                if g[1][i] == OPERATOR_SYMBOL:
                    if g[1][i+1] in terminals and g[1][i+1] not in temp:
                        temp.append(g[1][i+1])
                if g[1][0] in noTerminals and firstSets.get(g[1][0]) != temp:
                    temp = firstSets.get(g[1][0])
                if g[1][i] == OPERATOR_SYMBOL:
                    if g[1][i+1] in noTerminals and firstSets.get(g[1][i+1]) != temp:
                        temp = (firstSets.get(g[1][i+1]))
            firstSets[g[0]] = temp

    print(firstSets)

def nextOf(grammar, terminals, noTerminals, OPERATOR_SYMBOL, first_symbol):
    
    for g in grammar:
        temp = []
        for g2 in grammar:
            for i in range(len(g2[1])):
                if g[0] == first_symbol:
                    if g2[1][i] == first_symbol and g2[1][i+1] in terminals:
                        temp.append(g2[1][i+1])
                        temp.append('$')
                if g[0] == g2[1][i] and g2[1][i] in terminals:
                    temp.append(g2[1][i])
           
                    
        
        nextSets[g[0]] = temp
            
    print(nextSets)