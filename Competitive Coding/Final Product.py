from sys import stdin, stdout

N = stdin.readline()

A = list(map(int, stdin.readline().split()))

m = 10000000007
answer = 1
for item in A:
    answer = (answer*item) % m

stdout.write(str(answer))