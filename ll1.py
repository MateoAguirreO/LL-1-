firstSets = {}
nextSets = {}
predictionSets = {}
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
                    if g[1][i+1] in noTerminals and firstSets.get(g[1][i+1]) != temp:
                        temp = (firstSets.get(g[1][i+1]))
                if g[1][0] in noTerminals and firstSets.get(g[1][0]) != temp:
                    temp = []
                    temp = firstSets.get(g[1][0])
                if temp is None:
                    temp = []
            firstSets[g[0]] = temp
    print('Primeros')
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
                        if g2[1][i] == first_symbol and g2[1][i+1] in terminals and g2[1][i+1] not in temp:
                            temp.append(g2[1][i+1])
                        if g[0] == g2[1][i] and g2[1][i+1] in terminals and g2[1][i+1] not in temp:
                            temp.append(g2[1][i+1])
                        if g[0] == g2[1][i]:
                            if g2[1][i+1] in noTerminals:
                                temp = firstSets.get(g2[1][i+1]) 
                                if EPSILON in temp:
                                    temp.remove(EPSILON)
                                    if str(temp).strip("[]") not in str(nextSets.get(g2[0])).strip("[]"):
                                        temp += nextSets.get(g2[0])
                            if g2[1][i+1] == '|' and g2[0] != g2[1][i] and str(nextSets.get(g2[0])).strip("[]") not in str(temp).strip("[]"):
                                temp += nextSets.get(g2[0])
                        if temp is None:
                            temp = []
                    except: 
                        try:
                            for i in nextSets.get(g2[0]):
                                if i not in temp:
                                    temp.extend(i)
                        except:
                            continue
            nextSets[g[0]] = temp
    print('Siguientes')
    print(nextSets)

def predictionSet(grammar, terminals, noTerminals, EPSILON):
    for g in grammar:
        temp = g[1].split('|')
        temp3 = []
        for t in temp:
            if t[0] in terminals:
                temp3 += t[0]
            if t[0] in noTerminals:
                temp3 += firstSets.get(t[0])
                if EPSILON in temp3:
                    temp3.remove(EPSILON)
                    temp3 += nextSets.get(g[0])
            if t[0] == EPSILON:
                temp3 += nextSets.get(g[0])
                temp3.remove(EPSILON)
        predictionSets[g[0]] = temp3
    print("Conjunto prediccion")
    print(predictionSets)

def isLL1():
    for p in predictionSets:
        if not isLL1count(predictionSets.get(p)):
            return False
    return True

def isLL1count(p):
    for i in p:
        cont = p.count(i)
        if cont > 1:
            return False
    return True