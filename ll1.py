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
    pass

def getLHS(production):
   #return production.split('->')[0].replace(/\s+/g, '')
    pass

def getRHS(production):
    #return production.split('->')[1].replace(/\s+/g, '');
    pass

def firstOf(symbol):
    if (firstSets[symbol]):
        return firstSets[symbol]
    
    first= firstSets[symbol]={}

    # If it's a terminal, its first set is just itself.

    if (isTerminal(symbol)):
        first[symbol] = true
        return firstSets[symbol]
    

    productionsForSymbol = getProductionsForSymbol(symbol)
    for k in productionsForSymbol:
        production = getRHS(productionsForSymbol[k])

        for i in range(len(production)):        
            productionSymbol = production[i]
            #Epsilon goes to the first set.
            if productionSymbol == EPSILON:
                first[EPSILON] = true
                break
            

            firstOfNonTerminal = firstOf(productionSymbol)

            if not firstOfNonTerminal[EPSILON]: 
                merge(first, firstOfNonTerminal)
                break
            

            // Else (we got epsilon in the first non-terminal),
            //
            //   - merge all except for epsilon
            //   - eliminate this non-terminal and advance to the next symbol
            //     (i.e. don't break this loop)
            merge(first, firstOfNonTerminal, [EPSILON]);
            // don't break, go to the next `productionSymbol`.
        }
    }

    return first;
}