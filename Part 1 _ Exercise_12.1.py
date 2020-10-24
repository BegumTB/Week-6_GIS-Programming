#Write a function called most_frequent that takes a string and prints the letters
#in decreasing order of frequency. Find text samples from several different languages
#and see how letter frequency varies between languages.

from __future__ import print_function, division
def most_frequent(s):
    hist = make_histogram(s)
    t = []
    for x, freq in hist.items():
        t.append((freq, x))

    t.sort(reverse=True)

    res = []
    for freq, x in t:
        res.append(x)

    return res

def make_histogram(s):
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist

def read_file(filename):
     return open(filename).read()


if __name__ == '__main__':
    string = read_file('words.txt')
    letter_seq = most_frequent(string)
    for x in letter_seq:
        print(x)    





