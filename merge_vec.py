import sys

# python merge_vec.py oripath sigpath finalpath
# python merge_vec.py just/phone/vec_d90.txt output/phone1000/sig_vec_d10.txt vec/phone/just/merge_vec_d100_sig10.txt
if __name__ == "__main__":
    oripath = sys.argv[1]
    sigpath = sys.argv[2]
    finalpath = sys.argv[3]
    merge_vec = dict()
    d = 0

    with open(oripath) as orif:
        for orii in orif:
            toks = orii.strip().split(" ")
            if toks.__len__() <= 2:
                d = int(toks[1])
                continue
            merge_vec[toks[0]] = toks[1:]
    with open(sigpath) as sigf:
        cnt = 1
        for sigi in sigf:
            toks = sigi.strip().split(" ")
            if cnt == 1:
                d += int(toks[1])
                cnt = 0
                continue
            if toks[0] in merge_vec:
                merge_vec[toks[0]] += toks[1:]
            else:
                print("del ", toks[0])

    with open(finalpath, mode="w") as ff:
        ff.write(str(merge_vec.__len__()))
        ff.write(" ")
        ff.write(str(d))
        ff.write("\n")
        for i in merge_vec:
            ff.write(i)
            for j in merge_vec[i]:
                ff.write(" ")
                ff.write(j)
            ff.write("\n")
