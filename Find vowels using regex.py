"""
You are given a string. It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of that contains  or more vowels.
Also, these substrings must lie in between consonants and should contain vowels only.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

string = input()

pattern = r"[qwrtypsdfghjklzxcvbnm]?([aeiouAEIOU]{2,})[qwrtypsdfghjklzxcvbnm]"

findList = re.findall(pattern, string)

if len(findList) == 0:
    print("-1")
else:
    for item in findList:
        print(item)