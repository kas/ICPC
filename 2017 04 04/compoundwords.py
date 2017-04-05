import sys

def get_compounds(words):
    compounds = []
    for first_word in words:
        for second_word in words:
            compound = ''
            if first_word == second_word:
                continue
            else:
                compound = first_word + second_word
            if compound in compounds:
                continue
            else:
                compounds.append(compound)
    return compounds

words = []

x = 0

for i in sys.stdin:
    words += i.split()

compounds = get_compounds(words)

for compound in compounds:
    print(compound)
