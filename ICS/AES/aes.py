key = "0010 0100 0111 0101" #16 bit
pt = '1001 0100 0010 0111'
rc1='80'
rc2='30'

S = [['9','4','A','B'],
	['D','1','8','5'],
	['6','2','0','3'],
	['C','E','F','7']]	
	
Si = [['A','5','9','B'],
	['1','7','8','F'],
	['6','0','2','3'],
	['C','4','D','E']] 
	
	

def xor(h1,h2):
	return hex(int(h1,16)^int(h2,16))[2:]

def subNibble(nib,box):
	bits = bin(int(nib,16))[2:].zfill(4)
	row = int(bits[0]+bits[1],2)
	col = int(bits[2]+bits[3],2)
	return box[row][col]

def genT(oddw,rc):
	t0=subNibble(oddw[0],S)	
	t1=subNibble(oddw[1],S)
	t2=t1+t0
	return xor(t2,rc)
	
	
def keygen(key):
	sk = []
	w = [0]*6
	
	k = hex(int(key.replace(' ',''),2))[2:]
	#print k
	w[0] = k[:2]
	w[1] = k[2:]
	sk.append(w[0]+w[1])

	t2=genT(w[1],rc1)
	#print t2
	
	w[2]=xor(t2,w[0])
	w[3]=xor(w[2],w[1])
	sk.append(w[2]+w[3])
	
	t4=genT(w[3],rc2)
	w[4]=xor(t4,w[2])
	w[5]=xor(w[4],w[3])
	sk.append(w[4]+w[5])
	return sk
	
def rot(state):
	return state[0]+state[3]+state[2]+state[1]
	
def sub(state,S):
	r=''
	for s in state:
		r+=subNibble(s,S)
	return r


#	1	4
#	4	1	

def mult(num,h):
	h=int(h,16)
	val = num * h
	
	if(num!=9):
		if val >= 64:	
			val ^= 76
		if val >= 32:
			val ^= 38
		if val >= 16:
			val ^= 19
		
	else:
		val = 8 * h
		if val >= 64:
			val ^= 76
		if val >= 32:
			val ^= 38
		if val >= 16:
			val ^= 19
		val ^= h	
		
	#print h,"*",num,"=",hex(val)
	return hex(val)[2:]
			
def mix(state):
	s00= xor(mult(1,state[0]),mult(4,state[1]))
	s10= xor(mult(4,state[0]),mult(1,state[1]))
	s01= xor(mult(1,state[2]),mult(4,state[3]))
	s11= xor(mult(4,state[2]),mult(1,state[3]))
	return s00+s10+s01+s11

	
def mix_inv(state):
	s00= xor(mult(9,state[0]),mult(2,state[1]))
	s10= xor(mult(2,state[0]),mult(9,state[1]))
	s01= xor(mult(9,state[2]),mult(2,state[3]))
	s11= xor(mult(2,state[2]),mult(9,state[3]))
	return s00+s10+s01+s11	
	
def encrypt(pt,k):

	pt = hex(int(pt.replace(' ',''),2))[2:]
	print "Plain",pt
	#PreGame
	temp= xor(pt,k[0])
	print "Pre",temp
	
	#R1
	temp=rot(temp)
	print "Rot",temp
	temp=sub(temp,S)
	print "Sub",temp
	temp =mix(temp)
	print "Mix",temp
	temp = xor(temp,k[1])
	
	#R2
	temp=rot(temp)
	print "Rot",temp
	temp=sub(temp,S)
	print "Sub",temp
	temp = xor(temp,k[2])
	print	"cipher",temp
	return temp
	
def decrypt(cipher,k):
	print	"\n\n\nCipher",cipher
	#R2 i 
	temp = xor(cipher,k[2])
	temp=sub(temp,Si)
	temp=rot(temp)
	
	print "R2 i",temp
	
	#R1 i
	temp = xor(temp,k[1])

	temp =mix_inv(temp)
	temp=sub(temp,Si)
	#print "R1 i",temp
	temp=rot(temp)
	print "R1 i",temp
	
	#pre
	temp= xor(temp,k[0])
	print "Plain",temp
	
	return temp
	
	
	
def main():
	subk = keygen(key)
	print subk
	cipher=encrypt(pt,subk)
	#print cipher
	plain = decrypt(cipher,subk)

if __name__ == '__main__':
	main()