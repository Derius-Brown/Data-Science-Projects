import sys

set_b = {'apple', 'banana', 'mango', 'orange'}

if len(sys.argv) > 1:
    set_a = set(sys.argv[1:])
    diff_words = set_a.difference(set_b)
    print(diff_words)
