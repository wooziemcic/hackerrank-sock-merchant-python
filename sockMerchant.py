    import math
    import os
    import random
    import re
    import sys

    # Complete the sockMerchant function below.
    def sockMerchant(n, ar):
        d = {x:ar.count(x) for x in ar}
        b = list(d.values())
        s = 0
        for i in b:
            s += i//2
        return s

    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        n = int(input())

        ar = list(map(int, input().rstrip().split()))

        result = sockMerchant(n, ar)

        fptr.write(str(result) + '\n')

        fptr.close()
