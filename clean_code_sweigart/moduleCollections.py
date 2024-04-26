import collections

scores = collections.defaultdict(int)
print(scores)

scores['A1'] += 1
scores['Zophie'] += 40

print(scores)


booksReadBy = collections.defaultdict(list)
print(booksReadBy)

booksReadBy['A1'].append(1)
booksReadBy['A1'].append('string')

print(booksReadBy['A1'])
print(booksReadBy['Zophie'])
print(booksReadBy)
