vowels = 'AEIOU'

word = raw_input().strip()
score = [0, 0]

word_len = len(word)

for idx, letter in enumerate(word):
    score[letter in vowels] += word_len - idx

output = ''

if score[0] > score[1]:
    output = 'Stuart %s' % score[0]
elif score[1] > score[0]:
    output = 'Kevin %s' % score[1]
else:
    output = 'Draw'
print(output)
