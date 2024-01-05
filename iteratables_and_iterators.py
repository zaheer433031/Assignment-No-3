from itertools import combinations, groupby

count, letters, select = int(input()), input().split(), int(input())
letters = sorted(letters)
combine = list(combinations(letters, select))
contain = len([c for c in combine if 'a' in c])
print(contain / len(combine))