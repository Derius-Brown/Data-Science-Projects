import sys
def count_vowels(s):
    s = s.lower()
    vowels = set('aeiou')
    unique_vowels = vowels.intersection(s)
    print(len(unique_vowels))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        count_vowels(sys.argv[1])
