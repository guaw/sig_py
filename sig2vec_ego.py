from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import sys
import gc


def get_map(filepath):
    type2prime = dict()
    with open(filepath) as mf:
        for line in mf:
            toks = line.strip().split(",")
            type2prime[toks[0]] = int(toks[1])
    return type2prime


def readData(filepath, mapfile):
    type2prime = get_map(mapfile)
    with open(filepath) as f:
        for line in f:
            toks = line.strip().split(",")
            node0id = toks[0]
            node0type = type2prime[toks[1]]
            nodeid = toks[2]
            nodetype = type2prime[toks[3]]
            edgetype = type2prime[toks[4]]

            if node0id in neighbor:
                neighbor[node0id].append([nodeid, edgetype])
            else:
                neighbor[node0id] = [[nodeid, edgetype]]
            if nodeid in neighbor:
                neighbor[nodeid].append([node0id, edgetype])
            else:
                neighbor[nodeid] = [[node0id, edgetype]]

            if node0id not in V:
                V[node0id] = node0type
            if nodeid not in V:
                V[nodeid] = nodetype

            if node0id not in neighbor_v:
                neighbor_v[node0id] = []
            if nodeid not in neighbor_v[node0id]:
                neighbor_v[node0id].append(nodeid)
            if nodeid not in neighbor_v:
                neighbor_v[nodeid] = []
            if node0id not in neighbor_v[nodeid]:
                neighbor_v[nodeid].append(node0id)


def get_sig(nid, nprime):
    d = 0
    v = []
    if nid not in neighbor:
        print("%d not in neighbor", nid)
        return d, v

    sig = nprime
    for i in neighbor[nid]:
        if d >= cutoff:
            return d, v
        if sig*i[1] > sig_max:
            v.append(sig)
            sig = i[1]
            d += 1
        else:
            sig *= i[1]

    ego_dic = dict()
    for nvi in neighbor_v[nid]:
        if d >= cutoff:
            return d, v
        if sig*V[nvi] > sig_max:
            v.append(sig)
            sig = V[nvi]
            d += 1
        else:
            sig *= V[nvi]
        for nvj in neighbor_v[nid]:
            for ei in neighbor[nvi]:
                if ei[0] == nvj:
                    if ei[1] not in ego_dic:
                        ego_dic[ei[1]] = 0.5
                    else:
                        ego_dic[ei[1]] += 0.5

    for i in ego_dic:
        if d >= cutoff:
            return d, v
        for t in range(int(ego_dic[i])):
            if sig*i > sig_max:
                v.append(sig)
                sig = i
                d += 1
            else:
                sig *= i

    v.append(sig)
    d += 1
    return d, v


def get_sigs():
    d_max = 0
    vecs = dict()
    for vi in V:
        d, v = get_sig(vi, V[vi])
        vecs[vi] = v
        if d > d_max:
            d_max = d
    for r in vecs:
        for i in range(d_max - vecs[r].__len__()):
            vecs[r].append(0)
    return vecs, d_max


def decomp(d, p, v, n_max):
    vlist = []
    vidlist = []
    for i in v:
        vlist.append(v[i])
        vidlist.append(i)

    ss = StandardScaler()
    n = int(d-d*p)
    if n > n_max:
        print("n > n_max")
        vlist = ss.fit_transform(vlist)
        return vlist, vidlist, False

    with open(outvecpath+"vlist.txt", "w") as vlistf:
        for vi in vlist:
            for i in vi:
                vlistf.write(str(i))
                vlistf.write(" ")
            vlistf.write("\n")
    with open(outvecpath+"vidlist.txt", "w") as vidlistf:
        for vi in vidlist:
            vidlistf.write(str(vi))
            vidlistf.write("\n")
    print("write end")

    for x in locals().keys():
        del locals()[x]
    gc.collect()

    pca = PCA(n_components=n)
    v_pca = pca.fit_transform(vlist)
    v_pca = ss.fit_transform(v_pca)
    return v_pca, vidlist, True


# python sig2vec_ego.py fpath mpath p_target d_target sig_max outpath outvecpath
# python sig2vec_ego.py data/phone/Phone_data data/phone/phone_type_map.txt 0.9 100 1000 output/phone_ego1000/sig_vec_d10.txt output/phone_ego1000/
if __name__ == "__main__":
    fpath = sys.argv[1]
    mpath = sys.argv[2]
    p_target = float(sys.argv[3])
    d_target = int(sys.argv[4])
    sig_max = int(sys.argv[5])
    outpath = sys.argv[6]
    outvecpath = sys.argv[7]
    cutoff = 2000

    neighbor = dict()
    V = dict()
    neighbor_v = dict()

    readData(fpath, mpath)
    vec_sig, d_sig = get_sigs()
    print("get sig")
    vec_decomp, vid_list, is_pca = decomp(d_target, p_target, vec_sig, d_sig)
    with open(outpath, mode="w") as sigf:
        sigf.write(str(vec_decomp.__len__()))
        sigf.write(" ")
        sigf.write(str(vec_decomp[0].__len__()))
        sigf.write("\n")
        for i in range(vec_decomp.__len__()):
            sigf.write(str(vid_list[i]))
            for j in vec_decomp[i]:
                sigf.write(" ")
                sigf.write(str(j))
            sigf.write("\n")
