import ll1

grammar = {
    1: 'S -> TX',
    2: 'X -> +TX',
    3: 'X -> ε',
    4: 'T -> FY',
    5: 'Y -> *FY',
    6: 'Y -> ε',
    7: 'F -> (S)',
    8: 'F -> a',
}
print(grammar)

START_SYMBOL = 'S'
EPSILON = "ε"

firstSets = {}
followSets = {}
terminals = []
nonTerminals = []


def startUp(grammar):

    ll1.buildFirstSets(grammar)
    ll1.buildFollowSets(grammar)
    printSet('First sets', firstSets)
    printSet('Follow sets', followSets)
    ll1.buildNonTerminals(grammar)
    ll1.buildTerminals(grammar)

def printSet(type, sets ):
    pass
