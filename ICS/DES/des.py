# parameters
key = "0111111101"
#cipher = "10100010"
cipher = "01101101"
P10 = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
P8 = (6, 3, 7, 4, 8, 5, 10, 9)
P4 = (2, 4, 3, 1)

IP = (2, 6, 3, 1, 4, 8, 5, 7) #Data encreption Initial permutation  
IPi = (4, 1, 3, 5, 7, 2, 8, 6) #Data encreption Final permutation

E = (4, 1, 2, 3, 2, 3, 4, 1)
S0 = [
        [1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [3, 1, 3, 2]
     ]

S1 = [
        [0, 1, 2, 3],
        [2, 0, 1, 3],
        [3, 0, 1, 0],
        [2, 1, 0, 3]
]

def permutation(perm, key):
	#MIX USING INDICES IN PXX
	permutated_key = ""
	for i in perm:
		permutated_key += key[i-1]
		
	return permutated_key

def generate_first_key(left_key, right_key):
	#LEFT SHIFT
	left_key_rot = left_key[1:] + left_key[:1]
	#print "Left ROT:"+left_key_rot
	#LEFT SHIFT
	right_key_rot = right_key[1:] + right_key[:1]
	key_rot = left_key_rot + right_key_rot
	print key_rot
	#print "Right ROT:"+right_key_rot
	return permutation(P8, key_rot)

def generate_second_key(left_key, right_key):
	left_key_rot = left_key[3:] + left_key[:3]
	right_key_rot = right_key[3:] + right_key[:3]
	key_rot = left_key_rot + right_key_rot
	return permutation(P8, key_rot)		

def F(right, subkey):
    expanded_cipher = permutation(E, right)
    xor_cipher = bin( int(expanded_cipher, 2) ^ int(subkey, 2) )[2:].zfill(8)
    left_xor_cipher = xor_cipher[:4]
    right_xor_cipher = xor_cipher[4:]
    left_sbox_cipher = Sbox(left_xor_cipher, S0)
    right_sbox_cipher = Sbox(right_xor_cipher, S1)
    return permutation(P4, left_sbox_cipher + right_sbox_cipher)

def Sbox(input, sbox):
    row = int(input[0] + input[3], 2)
    column = int(input[1] + input[2], 2)
    return bin(sbox[row][column])[2:].zfill(4)

def f(first_half, second_half, key):
	left = int(first_half, 2) ^ int(F(second_half, key), 2)
	print "Fk: " + bin(left)[2:].zfill(4) + second_half
	return bin(left)[2:].zfill(4), second_half	

def main():

	print "======Key-Gen======"
	
	print key
	p10key = permutation(P10, key)
	#print "Initial Permutation:"+p10key
	left = p10key[:len(p10key)/2]
	right = p10key[len(p10key)/2:]
	#print "Left:"+left
	#print "Right:"+right

	first_key = generate_first_key(left, right)
	second_key = generate_second_key(left, right)
	print "[*] First key: " + first_key
	print "[*] Second key: " + second_key
	
	
	print '\n==========Enrecption========'
	print "Plain text :"+cipher
	initialPremute = permutation(IP, cipher)
	print "IP: " + initialPremute
	first_half_cipher = initialPremute[:len(initialPremute)/2]
	second_half_cipher = initialPremute[len(initialPremute)/2:]
	
	left, right = f(first_half_cipher, second_half_cipher, second_key)
	
	print "SW: " + right + left
	
	left, right = f(right, left, first_key) # switch left and right!
	
	finalPremute=permutation(IPi, left + right)
	
	print "IP^-1 Encrepted Cipher Text: " + finalPremute
	#print "\n\n\n------------------------------------------------"
	
	#finalPremute="01000110"
	
	print '\n==========Decreption========'
	print "Cipher :"+finalPremute
	initialPremute=permutation(IP,finalPremute)
	print "Initial P:"+initialPremute
	first_half_cipher = initialPremute[:len(initialPremute)/2]
	second_half_cipher = initialPremute[len(initialPremute)/2:]
	left, right = f(first_half_cipher, second_half_cipher, first_key)
	print "SW: " + right + left
	left, right = f(right, left, second_key) # Swapped
	finalPremute=permutation(IPi, left + right)
	print "Plain Text: " + finalPremute
	print "\n"

	

if __name__ == "__main__":
	main()

'''
Keygen
10 bit key 
P10
split
	rot by 1 left
	merge 
	p8
	K1
	
	rot by 3 left
	merge 
	p8
	K2
'''

''' 
8 BIT DATA ->  Inital Premute(8BD)
IP 
Split L4,R4
do 2 times with k1,k2
	L4=L4
	R8=ExpPremute(R4) 
	R8=XOR(R8,KEY8)
	Split
		S0 2Bit=SBOX(R1(RC))
		S1 2Bit=SBOX(R2(RC))
		MERGE
	SX=(S0 + S1)4Bit from SBOX0,1
	p4=P4(SX)	
	L=L^p4
	L(XORED with a jumbled R),R(what i started with)
	swap L and R
	so now the other half is changed in second run
			
'''
