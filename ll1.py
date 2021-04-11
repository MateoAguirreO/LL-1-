firstSets = {}


def firstOf(grammar, terminals, noTerminals):
    for k in range(10):
        for g in grammar:
            temp = []
            for i in range(len(g[1])):
                if g[1][0] in terminals and g[1][0] not in temp:
                    temp.append(g[1][0])
                if g[1][i] == '|':
                    if g[1][i+1] in terminals and g[1][i+1] not in temp:
                        temp.append(g[1][i+1])
                if g[1][0] in noTerminals and firstSets.get(g[1][0]) != temp:
                    temp = firstSets.get(g[1][0])
                if g[1][i] == '|':
                    if g[1][i+1] in noTerminals and firstSets.get(g[1][i+1]) != temp:
                        temp = (firstSets.get(g[1][i+1]))
            firstSets[g[0]] = temp

    print(firstSets)
