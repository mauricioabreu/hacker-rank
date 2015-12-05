from collections import Counter

letters = raw_input().strip()

counter = Counter(letters)

for letter, count in sorted(counter.most_common(3), key=lambda c: (-c[1], c[0])):
    print letter, count
