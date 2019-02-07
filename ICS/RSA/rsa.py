import numpy as np
import pandas as pd
import random
import math 


def modInverse(a, m) : 
	a = a % m; 
	for x in range(1, m) : 
		if ((a * x) % m == 1) : 
			return x 
	return 1

def is_prime(num):
	if num == 2:
		return True
	if num < 2 or num % 2 == 0:
		return False
	for n in xrange(3, int(num**0.5)+2, 2):
		if num % n == 0:
			return False
	return True

def gcd(x, y): 
	while(y): 
		x, y = y, x % y 
	return x 	

def keyGen(p,q):
	#Public key is (e, n) and private key is (d, n)
	print is_prime(p)
	print is_prime(q)
	
	if(not(is_prime(p) and is_prime(q))):
		raise ValueError("Both must be Prime")
	elif(p == q):	
		raise ValueError("Unequal values required")
	else:
		print "Begin keygen"
		n = p * q
		m = (p-1) * (q-1)	
		e = random.randrange(1, (min(p,q)-1))
		#print e
		g= gcd(e,m)
		while g != 1: 
			e = random.randrange(1, (min(p,q)-1))
			g= gcd(e,m)
		d = modInverse(e, m)
	#	print d
		return ((e, n), (d, n))
		

def encrypt(pk, plaintext):
	key, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
	cipher = []
	for char in plaintext:
		cipher.append(((ord(char) ** key) % n))	
	return cipher

def decrypt(pk, ciphertext):
	key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
	plain = ''
	for char in ciphertext:
		plain += chr((char ** key) % n)
	return plain		
		
		
def main():
	print "RSA"
	p = 19
	q = 17
	private, public =keyGen(p,q)
	print "Private :"+str(private)
	print "Public :"+str(public)
	cipher = encrypt(public,"jaiJ@1jai")
	print "Cipher: "+str(cipher)
	plain = decrypt(private,cipher)
	print "Plain  :"+str(plain)
	
if __name__ == "__main__" :
	main()
