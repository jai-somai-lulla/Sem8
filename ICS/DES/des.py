plain = '10010111'#8
key = '1001011101'#10

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

def permute(PX,bits):
	r=''
	for p in PX:
		r+=bits[p-1]
	return r
	
def rotL(bits,c):
	return bits[c:]+bits[:c]

def keygen(key):
	sk=[]
	temp = permute(P10,key)
	l , r = temp[:5],temp[5:]
	
	l1 ,r1 = rotL(l,1),rotL(r,1)
	sk.append(permute(P8,l1+r1))
	
	l3,r3 = rotL(l,3),rotL(r,3)
	sk.append(permute(P8,l3+r3))
	
	return sk

def sbox(b,box):
	row=int(b[0]+b[3],2)
	col=int(b[1]+b[2],2)
	return bin(box[row][col])[2:].zfill(4)
	
	
def F(r,k):
	e = permute(E,r)
	l = sbox(e[:4],S0)
	r = sbox(e[4:],S1)
	mask = bin(int(l+r,2)^int(k,2))[2:].zfill(8)
	
	return permute(P4,mask)
		
def f(l,r,k):
	mask = F(r,k)
	l = bin(int(l,2)^int(mask,2))[2:].zfill(4)
	r = r
	
	return l,r	
	
def encrypt(pt,k):
	print "Plain:",pt,int(pt,2)
	temp = permute(IP,pt)
	l,r = temp[:4],temp[4:]
	print 'TEMP',int(temp,2)
	#r1
	l,r=f(l,r,k[0])
	print 'TEMP',int(r+l,2)
	#r2
	l,r=f(r,l,k[1])
	print 'TEMP',int(l+r,2)
	temp = permute(IPi,l+r)
	print "Cipher:",temp,int(temp,2)
	return temp	

def decrypt(cipher,k):
	print '\n\n\nCipher',cipher,int(cipher,2)
	temp = permute(IP,cipher)
	print 'TEMP',int(temp,2)
	l,r = temp[:4],temp[4:]	
	#r1
	l,r=f(l,r,k[1])
	print 'TEMP',int(r+l,2)
	#r2
	l,r=f(r,l,k[0])
	print 'TEMP',int(l+r,2)
	temp = permute(IPi,l+r)
	print "Plain:",temp,int(temp,2)
	return temp	

def main():
	sk=keygen(key)
	print sk
	cip = encrypt(plain,sk)
	pl = decrypt(cip,sk)
if __name__ == '__main__':
	main()
