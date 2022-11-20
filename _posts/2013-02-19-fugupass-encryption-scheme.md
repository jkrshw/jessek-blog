---
layout: post
title: FuguPass Encryption Scheme
date: 2013-02-19 10:20
tags: encryption fugupass
slug: fugupass-encryption-scheme
---

[Last post](http://jessek.co.nz/2013/02/fugupass.html) I introduced the FuguPass password encryption script. In this post I'm going to go over the encryption scheme used which is based on RSA Laboratories [PKCS #5: Password-Based Cryptography Standard](http://www.rsa.com/rsalabs/node.asp?id=2127).

## Derived Key

The bulk of my implementation focused on deriving a key to use for the existing implementation of the Blowfish encryption algorithm. The derived key is generated as a function of the master key, a salt and an iteration count.

The master key being what the user entered and the salt is generated using the javascript Math.random() function, which is NOT a secure random implementation, with a fixed prefix. An iteration count of 1000 is used. The salt is to make it difficult for an attacker to pre-compute a large number of hashes and perform [rainbow attacks](http://en.wikipedia.org/wiki/Rainbow_table). The iteration count slows down brute force attacks. A count of 1000 means an attacker can try 1000 less passwords in the time it would have otherwise taken to try 1 with only a small overhead to computing the derived key.

	DK = (PRF, p, s, c)

1. Retrieve the master key (p)
2. Generate a random salt (s) and select iteration count (c)
3. Use a Pseudo Random Function (HMAC with SHA256) to generate U1, U2....Uc where:

	* U1 = PFR(p,s)
	* U2 = PRF(p, U1)
	* ...
	* Uc = PRF(p, Uc-1)

4. Calculate DK = U1 ^ U2 ^ ... ^ Uc

## Encryption

On submitting a password, a random salt is generated and a derived key calculated. The Blowfish implementation is then initialised with the DK and the encryption function is called on the plaintext. The resulting cipher text and the salt used are stored along with an identifier for the password.

This ensures that each password is encrypted with a different key. So even if you reuse passwords anyone looking at the EncryptedPasswords spreadsheet wont be able to tell which passwords are the same.

## Decryption

Decryption is almost identical to encryption. The DK is calculated from the salt that was stored with the cipher text and the master key entered by the user, after initialising the Blowfish algorithm the decryption function is called and the plaintext is returned to the user.

## Flaws

The number one rule of encryption is [don't do it](http://bindshell.nl/pub/cryptography-presentation-tnphp/#4) right? I'm sorry to say there are probably several flaws in my implementation. If you find any leave a comment, I'd love to learn more.

That was very wordy. Next time I'll go over how I've done some simple styling and basic tests of the algorithm.