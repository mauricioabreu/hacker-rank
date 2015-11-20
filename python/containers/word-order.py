from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


word_counter = OrderedCounter(
    [raw_input() for _ in range(int(raw_input()))]
)

print len(word_counter)
print ' '.join([str(count) for _, count in word_counter.iteritems()])
