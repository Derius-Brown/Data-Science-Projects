import sys
def cap_count(s):
    flag_list = []
    capital_letters = [c for c in s if c.isupper()]
    print(len(capital_letters))

    # Find all indices of each capital letter
    for i, char in enumerate(s):
        if char.isupper():
            flag_list.append(i)
    print(sum(flag_list))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cap_count(sys.argv[1])