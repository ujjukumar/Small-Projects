# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

N = int(input())

def is_valid_regex(reg):
    try:
        re.compile(reg)
        valid = True
    except re.error:
        valid = False
    
    return valid

for _ in range(N):
    reg = input()
    print(is_valid_regex(reg))