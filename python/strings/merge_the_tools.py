def merge_the_tools(string, k):
    def get_non_repeated(letters):
        """Get non repeated letters, keeping the order."""
        distinct = set()
        seen = []
        for letter in letters:
            if letter not in distinct:
                distinct.add(letter)
                seen.append(letter)
        return ''.join(seen)

    text_size = len(string)
    for t in [string[i:i + k] for i in range(0, text_size, k)]:
        print(get_non_repeated(t))
