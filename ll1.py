import index
import re


def buildFirstSets(grammar):
    index.firstSets = {}
    buildSet(firstOf)


def followSets(grammar):
    pass


def buildNonTerminals(grammar):
    pass


def buildTerminals(grammar):
    pass


def buildFollowSets(grammar):
    pass


def isTerminal(symbol):
    pass


def buildSet(builder):
    for k in index.grammar:
        builder(index.grammar[k][0])


def getProductionsForSymbol(symbol):
    productionsForSymbol = {}
    for k in index.grammar:
        if index.grammar[k][0] == symbol:
            productionsForSymbol[k] = index.grammar[k]

    return productionsForSymbol


def getLHS(production):
    prod = []

    for i in range(production):
        if(production[i] == '-'):
            break
        prod.append(production[i])

    return prod


def getRHS(production):
    prod = []
    ban = False
    for i in range(production):
        if(ban):
            prod.append(production[i])
        else:
            if(production[i] == '>'):
                ban = True
    return prod


def merge(first, firstOfNonTerminal):
    pass


    


def firstOf(symbol):
    if index.firstSets[symbol]:
        return index.firstSets[symbol]

    first = index.firstSets[symbol] = {}

    # If it's a terminal, its first set is just itself.

    if (isTerminal(symbol)):
        first[symbol] = True
        return index.firstSets[symbol]
    productionsForSymbol = getProductionsForSymbol(symbol)
    for k in productionsForSymbol:

        production = getRHS(productionsForSymbol[k])

        for i in range(len(production)):
            productionSymbol = production[i]
            # Epsilon goes to the first set.
            if productionSymbol == index.EPSILON:
                first[index.EPSILON] = True
                break

            firstOfNonTerminal = firstOf(productionSymbol)

            if not firstOfNonTerminal[index.EPSILON]:
                merge(first, firstOfNonTerminal)
                break

            # Else (we got epsilon in the first non-terminal),

            # - merge all except for epsilon
            # - eliminate this non-terminal and advance to the next symbol
            # (i.e. don't break this loop)
            merge(first, firstOfNonTerminal, [index.EPSILON])
            # don't break, go to the next `productionSymbol`.

    return first
