# Senior_Project_2020
This is my joint major Mathematical and Computer Science Senior Project in Bard College

# Abstract 
This thesis introduces the concept of Public-key cryptography, including RSA (Ron Rivest, Adi Shamir, Leonard Adleman) and ECC (Elliptic curve cryptography) system in the beginning chapters. Then, it uses two algorithms: Brute Force Algorithm for both RSA and ECC, and the Improved Algorithm only for ECC to mimic the cracking model for testing the security level in both systems. It designs experiments to run complexity analysis on RSA and ECC. Measuring the cracking time for private keys, this project compares the security level between the RSA cryptosystem and Elliptic curve cryptography.

Notably, this thesis concentrates on the elements that aﬀect the security level of ECC. Early study in the ﬁeld suggests that the size of the ﬁnite ﬁeld and the scope of keys aﬀect the security level of ECC. After collecting data that suggest the same result, this project focuses on the number of points on the corresponding elliptic curve, which proved to be another factor that aﬀects the cracking time for private keys. This conclusion only applies to the improved algorithm, which is proven to be more eﬀective than the brute force algorithm under various circumstances. Following the same trail of testing: the properties of the elliptic curve and cracking private keys through the improved algorithm, this thesis suggests that ECC should avoid elliptic curves with prime numbers of points over ﬁnite ﬁelds, due to our tests showing that they are less secure.
# Mark
This repo includes all testing code in this project. The major code is ecc_finite_fast.py which represents as the improved algorithm and ecc_finite_brute.py which representes the brutal force algorithm. 

## The Final data comparison
![Final data form](4.4.12.png)
![Final data form](4.4.14.png)
![Final data form](4.4.7.png)


# Conclusion
This thesis brieﬂy introduces the Public-Key cryptography, including Elliptic Curve Cryptography and RSA cryptosystem through mathematical concepts. We implement the necessary procedures of the elliptic curve cryptography and the RSA, make programs to mimic their key generation processes, and use these programs to crack private keys in both systems. For elliptic curve cryptography, we also measure the cracking time to ﬁnd out which element on an elliptic curve would aﬀect the security level.

We ﬁrstly compare the cracking time for the private key between Elliptic curve cryptography and RSA cryptosystem. The conclusion was cohesive with previous research: Through Brute Force Algorithm, trying out every number for the private key within a broad range to ﬁnd the right number, cracking a private key in ECC takes longer time than in RSA cryptosystem under the same key length. Meanwhile, it takes longer to crack a private key for both systems when we enlarge the key sizes. Furthermore, focusing on ECC only, the cracking time increases when we increase the size of p, which is the size of a ﬁnite ﬁeld F p . In other words, larger ﬁnite ﬁelds can ensure higher security levels.

Secondly, we introduce the improved algorithm, another method for cracking the private key based on Schoof’s algorithm: Using concepts in group law to count the number of points on an elliptic curve over a ﬁnite ﬁeld eﬃciently, we apply the order of a subgroup to cut down the cracking procedures. We make a comparison between this Improved Algorithm and Brute Force Algorithm. When the private key size increases, the Improved Algorithm takes much less time than the former method.

More essentially, we discover that the number of points on an elliptic curve also aﬀects the cracking time for a private key. We see that the Improved Algorithm speeds up the cracking eﬃciency compared to Brute Force Algorithm, even when the size of a ﬁnite ﬁeld increases. However, using Improved Algorithm forces us to pay attention to the property of the number of points on an Elliptic curve over the ﬁnite ﬁeld. According to our tests, we found that the improved algorithm can only perform eﬃciently when the number of points on an elliptic curve is a large prime number, where this property of the curve does not impact the eﬃciency of brute force algorithm. This indicates that if curves have 2 k , or a composite number of points on the curve where k is a positive integer, using the improved algorithm to crack the private key becomes diﬃcult. The reason might be related to the order of a subgroup and components of a composite number but I have not carried out the related research. This thesis strengthens my interest in cryptography and I will proceed to improve this research in the future, ﬁguring out what makes an elliptic curve more suitable for cryptography facing various cracking methods.
