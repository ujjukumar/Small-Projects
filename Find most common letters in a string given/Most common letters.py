from collections import Counter

def mostCommonLetters(string):
    for letter in Counter(sorted(string)).most_common(3):		# To find three most common letters in sorted list of given string
        print(*letter)		# To unpack the tuples created after sorting

if __name__ == '__main__':
    given_string = input()
    mostCommonLetters(given_string)
