import ll1

grammar = {
    1: 'S -> QA',
    2: 'A -> oQA | ε',
    3: 'Q -> RB',
    4: 'B -> RB | ε ',
    5: 'R -> F a | x | y',
    6: 'F -> z'
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
    # ll1.buildFirstSets(grammar)
    # ll1.buildFollowSets(grammar)
    # printSet('First sets', firstSets)
    # printSet('Follow sets', followSets)
    # ll1.buildNonTerminals(grammar)
    # ll1.buildTerminals(grammar)
    # this.nonTerminals = buildNoTerminals()
    splitingGrammar()
    first_symbol = buildNoTerminals(splitGrammar)
    buildProductions(splitGrammar)
    buildTerminals()
    ll1.firstOf(splitGrammar, terminals, nonTerminals, OPERATOR_SYMBOL)
    ll1.nextOf(splitGrammar, terminals, nonTerminals, first_symbol, EPSILON)

def splitingGrammar():
    for value in grammar.values():
        splitGrammar.append(value.replace(' ', '').split('->'))
    print(splitGrammar)


def buildNoTerminals(split):
    cont = 0
    for k in split:
        nonTerminals.append(split[cont][0].replace(' ', ''))
        cont = cont + 1
    first_symbol = nonTerminals[0]
    print("Primer simbolo")
    print(first_symbol)
    print("No Terminales")
    print(nonTerminals)
    return first_symbol

def buildProductions(split):
    cont = 0
    for k in split:
        productions.append(split[cont][1].replace(' ', ''))
        cont = cont + 1
    print(productions)

def buildTerminals():
    for i in productions:
        for c in range(len(i)):
            if i[c] not in nonTerminals and i[c] != OPERATOR_SYMBOL and i[c] not in terminals:
                terminals.append(i[c])
    print(terminals)

startUp()


def printSet(type, sets):
    pass
