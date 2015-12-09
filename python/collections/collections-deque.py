from collections import deque


d = deque()

for _ in range(int(raw_input())):
    operation = raw_input().split()
    if hasattr(d, operation[0]):
        func = getattr(d, operation[0])
        try:
            func(operation[1])
        except IndexError:
            func()
            
print ' '.join(d)
