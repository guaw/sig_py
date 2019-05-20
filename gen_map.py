import numpy as np
import sys

# python gen_map.py datafile outfile prime_file
# python gen_map.py data/phone/Phone_data data/phone/phone_type_map.txt prime/prime1000.txt
if __name__ == "__main__":
    fpath = sys.argv[1]
    opath = sys.argv[2]
    ppath = sys.argv[3]
    type2prime = dict()

    prime = np.loadtxt(ppath, dtype=str, delimiter=",")
    i = 0
    with open(fpath) as f:
        for line in f:
            toks = line.strip().split(",")
            if toks[1] not in type2prime:
                type2prime[toks[1]] = prime[i]
                i += 1
            if toks[3] not in type2prime:
                type2prime[toks[3]] = prime[i]
                i += 1
            if toks[4] not in type2prime:
                type2prime[toks[4]] = prime[i]
                i += 1

    with open(opath, mode="w") as mf:
        for ti in type2prime:
            mf.write(ti)
            mf.write(",")
            mf.write(type2prime[ti])
            mf.write("\n")
