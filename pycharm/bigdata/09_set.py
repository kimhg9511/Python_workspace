# set = {'1', '2', '3', '3', '2', '1'}
# print(set)
#
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
# union
print(a | b, set.union(a, b))  # {1, 2, 3, 4, 5, 6} {1, 2, 3, 4, 5, 6}
# intersection
print(a & b, set.intersection(a, b))  # {3, 4} {3, 4}
# difference
print(a - b, set.difference(a, b))  # {1, 2} {1, 2}
# symmetric_difference
print(a ^ b, set.symmetric_difference(a, b))  # {1, 2, 5, 6} {1, 2, 5, 6}
