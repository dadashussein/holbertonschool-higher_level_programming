#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    sum = 0
    for i in range(length):
        num = int(sys.argv[i + 1])
        sum = sum + num
    print(sum)
