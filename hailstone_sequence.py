import itertools
def hailstone_sequence():
    pattern = list()
    for a,b in itertools.product(range(0, 11), range(0,11)):
        holdingPattern = 0
        for x in range(1,101):
            pattern = [x]
            count = 0
            while count <= 100:
                count += 1
                x = x/2 if x%2 == 0 else a*x+b
                if x in pattern:
                    holdingPattern += 1
                    break
                else:
                    pattern.append(x)
                if x == 1 or x == 0:
                    break
        if holdingPattern > 0:
            print(' When a = {0} and b = {1}, then total number of converging holding patterns is {2}'.format(a,b,holdingPattern))
hailstone_sequence()