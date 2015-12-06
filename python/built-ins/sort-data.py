n, m = raw_input().strip().split()
data = []

for _ in range(int(n)):
    data.append(raw_input().strip().split())

indexer = raw_input().strip()
data = [map(int, row) for row in data]

for row in sorted(data, key=lambda x: x[int(indexer)]):
    print ' '.join(str(n) for n in row)
