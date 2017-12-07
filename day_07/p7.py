import itertools as it

inp = [x.strip() for x in open('input.txt').readlines()]


def parse():
    retval = []
    for line in inp:
        parts = line.split(' ')
        base = parts.pop(0)
        weight = int(parts.pop(0)[1:-1])
        subs = []
        if parts:
            assert parts[0] == '->'
            parts.pop(0)
        if parts:
            for p in parts:
                p = p.replace(',', '')
                assert ',' not in p
                subs.append(p)
        retval.append((base, weight, subs))
        #print(retval[-1])
    return retval

def star1():
    d = {}
    names = set()
    for name, weight, subs in parse():
        names.add(name)
        for sub in subs:
            d.setdefault(sub, [])
            d[sub].append(name)
            names.add(sub)
    for name in names:
        if not d.get(name):
            print(name)
    return

def star2():
    names = set()
    weights = {}
    defs = {}
    for name, weight, subs in parse():
        names.add(name)
        weights[name] = weight
        defs[name] = []

    for name, weight, subs in parse():
        for sub in subs:
            defs[name] = subs

    print("WEIGHT",weights['jdxfsa'])  # this is the one that fails the assert
    for i in range(200):
        print("LEN", len(defs))
        for name, subs in list(defs.items()):
            if all(defs.get(sub, []) == [] for sub in subs):
                subw = [weights[sub] for sub in subs]
                assert all(w == subw[0] for w in subw), list(zip(subw, subs))
                weights[name] += sum(subw)
                for subn in subs:
                    defs.pop(subn, None)
                defs[name] = []
    print(defs)


if __name__ == '__main__':
    star1()
    star2()
