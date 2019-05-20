import sys
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# python pca.py outpath
# python pca.py output/phone1000/
if __name__ == "__main__":
    vecfolder = sys.argv[1]
    vlist = []
    vidlist = []

    with open(vecfolder+"vlist.txt") as vf:
        for line in vf:
            toks = line.strip().split()
            vlist.append([int(t) for t in toks])
    with open(vecfolder+"vidlist.txt") as vidf:
        for line in vidf:
            toks = line.strip().split()
            vidlist += toks
    print("loaded vlist & vidlist")

    for i in [1, 2, 5, 10, 20, 30]:
        n = i
        print("start:", n)
        pca = PCA(n_components=n)
        v_pca = pca.fit_transform(vlist)
        ss = StandardScaler()
        v_pca = ss.fit_transform(v_pca)

        with open(vecfolder+"sig_vec_d"+str(n)+".txt", "w") as outf:
            outf.write(str(v_pca.__len__()))
            outf.write(" ")
            outf.write(str(v_pca[0].__len__()))
            outf.write("\n")
            for i in range(v_pca.__len__()):
                outf.write(vidlist[i])
                for j in v_pca[i]:
                    outf.write(" ")
                    outf.write(str(j))
                outf.write("\n")

        print("end:", n)
