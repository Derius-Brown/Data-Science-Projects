import sys

if len(sys.argv) > 1:
    word = sys.argv[1]
    counter = {}
    for char in word:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    print(counter)
