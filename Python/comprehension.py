import sys

if len(sys.argv) > 1:
    my_ints = [int(x) for x in sys.argv[1:]]
    my_ints = [x * 10 if x % 3 == 0 else x for x in my_ints]
    print(my_ints)
