from itertools import groupby

chars = raw_input().strip()
groups = []

for key, value in groupby(chars):
    groups.append((len(list(value)), int(key)))

print ' '.join(['(%s, %s)' % (k, v) for k, v in groups])
