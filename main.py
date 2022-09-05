def gensubset(l):
    if len(l) == 0:
        return [[]]
    else:
        smaller = gensubset(l[:-1])
        extra = l[-1:]
        new = []
        for i in smaller:
            new.append(i + extra)
    return smaller + new

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))
print("this is subtle change")
print("i dont know how the log works")

l = [1, 2, 3, 4, 5, 5]
print(gensubset(l))
