import ll1

grammar = {
    1: 'E -> L A | i A | o E A | a E c A',
    2: 'A -> o E A | s E A | d E p E A | ε'
}



# print(grammar)

OPERATOR_SYMBOL = '|'
EPSILON = "ε"
first_symbol = ''
firstSets = {}
followSets = {}
productions = []
nonTerminals = []
terminals = []
splitGrammar = []


def startUp():
    print(grammar)
    splitingGrammar()
    first_symbol = buildNoTerminals(splitGrammar)
    buildProductions(splitGrammar)
    buildTerminals()
    ll1.firstOf(splitGrammar, terminals, nonTerminals, OPERATOR_SYMBOL)
    ll1.nextOf(splitGrammar, terminals, nonTerminals, first_symbol, EPSILON)
    ll1.predictionSet(splitGrammar, terminals, nonTerminals, EPSILON)
    if ll1.isLL1():
        print("Si es gramatica LL1")
    else:
        print("No es gramatica LL1")
    

def splitingGrammar():
    for value in grammar.values():
        splitGrammar.append(value.replace(' ', '').split('->'))


def buildNoTerminals(split):
    cont = 0
    for k in split:
        nonTerminals.append(split[cont][0].replace(' ', ''))
        cont = cont + 1
    first_symbol = nonTerminals[0]
    return first_symbol

def buildProductions(split):
    cont = 0
    for k in split:
        productions.append(split[cont][1].replace(' ', ''))
        cont = cont + 1

def buildTerminals():
    for i in productions:
        for c in range(len(i)):
            if i[c] not in nonTerminals and i[c] != OPERATOR_SYMBOL and i[c] not in terminals:
                terminals.append(i[c])

startUp()


