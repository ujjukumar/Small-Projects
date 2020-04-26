from sys import stdin, stdout

def seatArrangement(T):
    eqT = T % 12
    quotient = T//12
    rem = eqT % 6

    facingSeat = 12*(quotient + 1) - eqT + 1
    if rem == 1 or rem == 0:
        if eqT == 0:
            facingSeat -= 24
        stdout.write("{0} WS".format(facingSeat))
    elif rem == 2 or rem == 5:
        stdout.write("{0} MS".format(facingSeat))
    elif rem == 3 or rem == 4:
        stdout.write("{0} AS".format(facingSeat))
    stdout.write('\n')

def main():
    N = int(stdin.readline())
    for _ in range(N):
        seatArrangement(int(stdin.readline()))

if __name__ == "__main__":
    main()