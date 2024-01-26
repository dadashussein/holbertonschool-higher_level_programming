#!/usr/bin/python3
import sys
end_char = ':'
argc = len(sys.argv)
if argc - 1 == 0:
    end_char = "."
print(f"{argc-1} arguments{end_char}")
for index,  comman in enumerate(sys.argv[1:], start=1):
    print("{}: {}".format(index, comman))
