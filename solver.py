import sys
import re
from itertools import permutations


def solver(filename, letters):
    # reads in words from txt file and saves to a list
    word_dict = []
    f = open(filename, 'r')
    text = f.read()
    f.close()
    words = text.split()
    for word in words:
        word_dict.append(word)

    # uses permutation from itertools to populate a list of every permutation from the user input
    perms = []
    for i in range(1, len(letters)+1):
        for c in permutations(letters, i):
            perms.append(''.join(c))

    # uses set intersect to return a set of all matching words from permutations
    result = set(word_dict).intersection(perms)

    # sorts and prints the set of matching words
    sort_result = sorted(result, key=len, reverse=True)

    for word in sort_result:
        print word



def main():
    input_str = raw_input("Please provide countdown letters: ")
    if not re.match("^[a-z]{9}$", input_str):
        print "Error! Only a minimum/maximum of 9 letters ranging from a-z allowed!"
        sys.exit()
    solver('words.txt', input_str)


if __name__ == '__main__':
    main()
