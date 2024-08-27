import sys

if len(sys.argv) > 1:
    duplicated_words = sys.argv[1:]
    unique_words = sorted(set(duplicated_words), reverse=True)
    print(unique_words)
