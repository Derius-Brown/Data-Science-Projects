import sys

if len(sys.argv) > 1:
    duck_goose = sys.argv[1:]
    duck_goose = [word for word in duck_goose if word != 'goose']
    print(duck_goose)
