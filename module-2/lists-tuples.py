# insert multiple elements
a = [1, 2, 3]
a[1] = [2.1, 2.2, 2.3]
a
#[1, [2.1, 2.2, 2.3], 3]

# replacing the single element
a = [1, 2, 3]
a[1:2] = [2.1, 2.2, 2.3]
a
#[1, 2.1, 2.2, 2.3, 3]

# insert elements without removing anything
a = [1, 2, 7, 8]
a[2:2] = [3, 4, 5, 6]
a
#[1, 2, 3, 4, 5, 6, 7, 8]


# deleting elements 
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a[1:5] = []
a
#['foo', 'corge']

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
del a[1:5]
a
#['foo', 'corge']

# concatinate string into list
a = ['foo', 'bar', 'baz', 'qux', 'quux']
a += 'corge'
a
#['foo', 'bar', 'baz', 'qux', 'quux', 'c', 'o', 'r', 'g', 'e']

a = ['foo', 'bar', 'baz', 'qux', 'quux']
a += ['corge'] #singleton list
a
#['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
