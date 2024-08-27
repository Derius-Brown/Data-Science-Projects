import sys

set_b = {'apple', 'banana', 'mango', 'orange'}

if len(sys.argv) > 1:
    set_a = set(sys.argv[1:])
    common_words = set_a.intersection(set_b)
    print(common_words)