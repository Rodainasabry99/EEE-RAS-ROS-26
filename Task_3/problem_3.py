def common_elements(set1, set2):
    return set1.intersection(set2)

print(common_elements({1, 2, 3}, {2, 3, 4}))
print(common_elements({5, 6}, {7, 8}))
print(common_elements({1, 2}, {1, 2}))