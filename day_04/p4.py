import itertools as it

"""
docstring
"""

my_input = open('inp.txt').readlines()

def no_anas(parts):
    parts = [''.join(sorted(l)) for l in parts]
    return len(set(parts)) == len(parts)

def main():
    tot = 0
    for line in my_input:
        line = line.strip()
        parts = line.split(' ')
        if len(set(parts)) == len(parts):
            tot += 1
    print(tot)

def main2():
    tot = 0
    for line in my_input:
        line = line.strip()
        parts = line.split(' ')
        if no_anas(parts):
            tot += 1
    print(tot)

# not 472
# not 512
# not 466

assert no_anas(['abcde', 'fghij']) == True
assert no_anas(['abcde', 'xyz', 'ecdab']) == False
assert no_anas('a ab abc abd abf abj'.split()) == True
assert no_anas('oiii ioii iioi iiio'.split()) == False

if __name__ == '__main__':
    main2()
