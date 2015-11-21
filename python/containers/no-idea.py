_ = raw_input()
N = map(int, raw_input().split())
A = {int(number) for number in raw_input().split()}
B = {int(number) for number in raw_input().split()}
happiness = 0
for number in N:
	happiness += (number in A) - (number in B)
print(happiness)
