import itertools as it

chars = open('input.txt').read()

garbage_count = 0

def filter_garbage(txt):
    global garbage_count
    garb = False
    cit = iter(txt)
    for c in cit:
        if c == '!':
            next(cit)
        elif not garb and c == '<':
            garb = True
        elif garb and c == '>':
            garb = False
        elif not garb:
            yield c
        else:
            garbage_count += 1

assert list(filter_garbage('<a>')) == list(''), list(filter_garbage('<a>'))
assert list(filter_garbage('x<a>y')) == list('xy'), list(filter_garbage('x<a>y'))
assert list(filter_garbage('x<<a>y')) == list('xy')
assert list(filter_garbage('x<a!>>y')) == list('xy')


def star1():
    global chars
    chars = list(filter_garbage(chars))
    stack = []
    curr = ''
    for c in chars:
        if c == '{':
            stack.append(c)
        elif c == '}':
            stack.append(c)
        else:
            pass
    bracks = ''.join(stack)
    return score(bracks)

def score(txt):
    tot = 0
    stack = []
    for c in txt:
        if c == '{':
            stack.append(c)
        elif c == '}':
            tot += len(stack)
            stack.pop()
    return tot

assert score('{}') == 1
assert score('{{{}{}{{}}}}') == 16

garbage_count = 0
print("SCORE", star1())
print("GARB", garbage_count)
