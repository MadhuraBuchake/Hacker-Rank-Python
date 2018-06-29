#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    splt = s.split(':')
    if splt[2][2:4] == 'PM' and splt[0]!= '12':
        t = int(splt[0]) + 12
        splt[0] = str(t)
    elif int(splt[0]) == 12 and splt[2][2:4] == 'AM':
        splt[0] = '00'
    splt[2] = splt[2][:2]
    return(':'.join(splt))

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
