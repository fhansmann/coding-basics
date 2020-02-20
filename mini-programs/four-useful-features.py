# 1) List Comprehension

add_func = lambda z: z ** 2
is_odd = lambda z: z%2 == 1
multiply = lambda x,y: x*y

aList = list(range(10))
print(aList)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(map(add_func, aList)))
print([x ** 2 for x in aList])
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print(list(filter(is_odd, aList)))
print([x for x in aList if x%2 == 1])
# [1, 3, 5, 7, 9]
# [1, 3, 5, 7, 9]


# List manipulation

a, b, c, d = aList[0:4]
print(f'a = {a}, b = {b}, c = {c}, d = {d}')
# a = 0, b = 1, c = 2, d = 3

a, *b, c, d = aList
print(f'a = {a}, b = {b}, c = {c}, d = {d}')
# a = 0, b = [1, 2, 3, 4, 5, 6, 7], c = 8, d = 9


# Zipping and enumerate — for-loops

numList = [0, 1, 2]
engList = ['zero', 'one', 'two']
espList = ['cero', 'uno', 'dos']
print(list(zip(numList, engList, espList)))
# [(0, 'zero', 'cero'), (1, 'one', 'uno'), (2, 'two', 'dos')]

for num, eng, esp in zip(numList, engList, espList):
    print(f'{num} is {eng} in English and {esp} in Spanish.')
# 0 is zero in English and cero in Spanish.

Eng = list(zip(engList, espList, numList))
Eng.sort() # sort by engList
a, b, c = zip(*Eng)

print(a)
print(b)
print(c)
# ('one', 'two', 'zero')
# ('uno', 'dos', 'cero')
# (1, 2, 0)
___
upperCase = ['A', 'B', 'C', 'D', 'E', 'F']
lowerCase = ['a', 'b', 'c', 'd', 'e', 'f']
for i, (upper, lower) in enumerate(zip(upperCase, lowerCase), 1):
    print(f'{i}: {upper} and {lower}.')
# 1: A and a.
# 2: B and b.
# 3: C and c.
# 4: D and d.
# 5: E and e.
# 6: F and f.

# 4 Genertors

def gen(n):    # an infinite sequence generator that generates integers >= n
    while True:
        yield n
        n += 1
        
G = gen(3)     # starts at 3
print(next(G)) # 3
print(next(G)) # 4
print(next(G)) # 5
print(next(G)) # 6
