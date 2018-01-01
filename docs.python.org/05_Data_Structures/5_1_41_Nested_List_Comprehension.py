matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(4)])


transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print (transposed)


re_transposed = list()
for i in range(3):
    re_transposed_row = list()
    for row in transposed:
        re_transposed_row.append(row[i])
    re_transposed.append(re_transposed_row)

print(re_transposed)

print ([[row[i] * 9 for row in re_transposed if row[i] * 9 > 20] for i in range(4)])

print('''
        When working with nested loops in list comprehensions remember 
        that the for clauses remain 
        in the same order as in our original for loops.
    ''')

#Practice

vec = []
for x in range(3):
    vec.append(x*3)
print (vec)
print ([x*3 for x in range(3)])

