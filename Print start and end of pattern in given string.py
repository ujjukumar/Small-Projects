# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

String = input()
word = input()

pattern = re.compile(word)
result = pattern.search(String)
if not result: print((-1,-1))
while result:
    print((result.start(), result.end()-1))
    result = pattern.search(String, result.start() + 1)