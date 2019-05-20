import math
import sys


def func_get_prime(n):
    return filter(lambda x: not [x % i for i in range(2, int(math.sqrt(x)) + 1) if x % i == 0], range(2, n + 1))


# python gen_prime.py outpath/ upper_limit
# python gen_prime.py prime/ 1000
if __name__ == "__main__":
    n = int(sys.argv[2])
    pl = list(func_get_prime(n))
    fstr = sys.argv[1] + "prime" + str(n) + ".txt"
    with open(fstr, "w") as pfile:
        for i in range(pl.__len__()-1):
            pfile.write(str(pl[i]))
            pfile.write(",")
        pfile.write(str(pl[pl.__len__()-1]))
