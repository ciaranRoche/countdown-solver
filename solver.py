import sys
import re
from itertools import permutations


def create_dict(filename, letters):
    word_dict = []
    f = open(filename, 'r')
    text = f.read()
    f.close()
    words = text.split()
    for word in words:
        word_dict.append(word)

    perms = []
    for i in range(1, len(letters)+1):
        for c in permutations(letters, i):
            perms.append(''.join(c))

    result = set(word_dict).intersection(perms)
    print sorted(result, key=len, reverse=True)


def main():
    input_str = raw_input("Please provide countdown letters: ")
    if not re.match("^[a-z]{9}$", input_str):
        print "Error! Only a minimum/maximum of 9 letters ranging from a-z allowed!"
        sys.exit()
    create_dict('words.txt', input_str)


if __name__ == '__main__':
    main()
