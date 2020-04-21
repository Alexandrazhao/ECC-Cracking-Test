# Senior_Project_2020
This is my joint major Mathematical and Computer Science Senior Project

# Introduction 
This project introduces the concept of modern cryptography including RSA system and ECC(Elliptic  curve  cryptography). This project introduces  two  algorithms:Brutal Force Algorithm to crack the private key in both RSA and ECC systems and the improved Algorithm to crack the private key in ECC system. This project mimic the cracking model for testing the security level in both systems, and designs tests for complexity analysis through RSA and ECC systems. Specifically, comparing the security level between RSA cryptosystem and Elliptic curve Cryptography by measuring the crakcing time for private keys, and discovers elements which will effect the security level for ECC. This project finds that not only the size of the finite field and size of keys would effect the cracking time for the private key, but the number of points on the corresponding elliptic curve would also effectthe security level.

# Mark
This repo includes all testing code in this project. The major code is ecc_finite_fast.py which represents as the improved algorithm and ecc_finite_brute.py which representes the brutal force algorithm. 
