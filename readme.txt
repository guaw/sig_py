0. gen_prime.py: Generate primes file
	python gen_prime.py outpath/ upper_limit
	Parameters: path of output file, upper limit of prime
	Ex.: python gen_prime.py prime/ 1000    # Generate file 'prime1000.txt' of prime up to number 1000

1. gen_map.py: Generate files for labels to primes
    python gen_map.py datafile outfile prime_file
	Parameters: input edge set, output file, prime file
	Ex.: python gen_map.py data/phone/Phone_data data/phone/phone_type_map.txt prime/prime1000.txt

2.1 sig2vec.py: Compute node signature in direct neighbor
	python sig2vec.py fpath mpath p_target d_target sig_max outpath outvecpath
	Parameters: input edge set, map file, basis vector proportions p, total number of dimensions d, single-dimensional signature cap sig_max, output file, output path
	Ex.: python sig2vec.py data/phone/Phone_data data/phone/phone_type_map.txt 0.9 100 1000 output/phone1000/sig_vec_d10.txt output/phone1000/
2.2 sig2vec_ego: Compute node signature in ego-network
	python sig2vec_ego.py fpath mpath p_target d_target sig_max outpath outvecpath
	Parameters: input edge set, map file, basis vector proportions p, total number of dimensions d, single-dimensional signature cap sig_max, output file, output path
	Ex.: python sig2vec_ego.py data/phone/Phone_data data/phone/phone_type_map.txt 0.9 100 1000 output/phone_ego1000/sig_vec_d10.txt output/phone_ego1000/

3. pca.py: Reduce the dimension of the node signature
    python pca.py outpath
	Parameters: path of output file
    Ex.: python pca.py output/phone1000/

4. merge_vec.py: Merge node vectors
    python merge_vec.py oripath sigpath finalpath
	Parameters: basis vector file, sig vector file, final vector file
    Ex.: python merge_vec.py just/phone/vec_d90.txt output/phone1000/sig_vec_d10.txt vec/phone/just/merge_vec_d100_sig10.txt















