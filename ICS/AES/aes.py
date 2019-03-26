def binToHex(bin):
	bin.replace(' ', '')
	return hex(int(bin, 2))

def hexToBin(my_hexdata,l=4):
	return bin(int(my_hexdata, 16))[2:].zfill(l)

def xorbin(a,b,l=8):
	y = int(a, 2)^int(b,2)
	return bin(y)[2:].zfill(l)

def xorhex(a,b):	
	result = int(a, 16) ^ int(b, 16) # convert to integers an
	return '{:x}'.format(result)     # convert back to hexadecimal

def rotate(data,l=4):
	p1 = data[:l]
	p2 = data[l:]         
	#print 'rot	:'+binToHex(p2+p1)   	
	return (p2+p1)

def subNibble(nibble):
	#print 'Nibble	:'+ binToHex(nibble)  + " " + nibble
	matrix = [['9','4','A','B'],
	['D','1','8','5'],
	['6','2','0','3'],
	['C','E','F','7']]
	
	col = int(nibble[2]+nibble[3],2)
	row = int(nibble[0]+nibble[1],2)
	#print 'Row'+ str(row)
	#print 'Col'+ str(col)
	
	#print 'Converted	:'+matrix[row][col]
	return matrix[row][col]
	
def invSubNibbles(nibble):
	matrix= [['A','5','9','B'],
	['1','7','8','F'],
	['6','0','2','3'],
	['C','4','D','E']] 

	col = int(nibble[2]+nibble[3],2)
	row = int(nibble[0]+nibble[1],2)
	return matrix[row][col]
	
def mixcolumns(n1,n2):
	n1=int(n1,16)
	n2=int(n2,16)
	print "N1: "+str(n1)
	print "N2: "+str(n2)
	a1=((1*n1)%19) ^ ((4*n2)%19)
	a2=((4*n1)%19) ^ ((1*n2)%19)	
#	print "Mixed col	:"+'{:x}'.format(a1) + '{:x}'.format(a2)
	print "A1: "+str(a1)
	print "A2: "+str(a2)
	
	return '{:x}'.format(a1),'{:x}'.format(a2)

def invmixcolumn(n1,n2):
	n1=int(n1,16)
	n2=int(n2,16)
	a1=9*n1 ^ 2*n2
	a2=2*n1 ^ 9*n2	
	return '{:x}'.format(a1),'{:x}'.format(a2)

def keyGen(key):	
	k=[[],[],[]] #6 words(bytes) or 3x 16 bit 
	w = []
	key = key.replace(' ','')
	rc1 = '10000000'
	rc2 = '00110000'
	t2=''
	t4=''
	print "======Key-Gen======\n\n"
	#print(xorbin('1000','0111'))
	#print key
	w.append(key[:8])  			#w0
	w.append(key[8:])			#w1
	
	#print 'w[1]	:'+binToHex(w[1])
	temp=rotate(w[1])
	tx1=hexToBin(subNibble(temp[:4]))
	tx2=hexToBin(subNibble(temp[4:]))
	#print tx1+tx2
	t2=xorbin(tx1+tx2,rc1)
	#print binToHex(t2)
	
	w.append(xorbin(t2,w[0]))	#w2
	w.append(xorbin(w[2],w[1])) #w3
	
	temp=rotate(w[3])
	tx1=hexToBin(subNibble(temp[:4]))
	tx2=hexToBin(subNibble(temp[4:]))
	#print tx1+tx2
	t4=xorbin(tx1+tx2,rc2)
	#print binToHex(t4)

	
	w.append(xorbin(t4,w[2])) 	#w4
	w.append(xorbin(w[4],w[3])) #w5
	
	k[0]=w[0]+w[1]
	k[1]=w[2]+w[3]
	k[2]=w[4]+w[5]
	return k

def genCipher(plain,k):
	print 'Plain Text	:' +plain + "  " +binToHex(plain)
	print 'Key 0		:' +k[0] + "  " +binToHex(k[0])
	
	#Pre Round Transform
	prt = xorbin(plain,k[0],16)
	print 'PreR		:'+ prt+ "  " +binToHex(prt)
		
		
	#Round 1
	temp=''
	for i in range(4):
		temp+= subNibble(prt[i*4:(i+1)*4])	
	print 'Sub :'+temp
	t1=temp[:2]
	t2=rotate(temp[2:],1)
	temp=t1+t2
	print 'Rot :'+temp
	
	t0,t2	= mixcolumns(temp[0],temp[2])
	t1,t3	= mixcolumns(temp[1],temp[3])
	temp = t0+t1+t2+t3
	print 'MIX :'+ temp
	
	
	
	
	
def main():
	key = "0010 0111 0100 0101" #16 bit
	plain = "0001 0010 1010 0011" #16 bit
	rounds = 2
	plain = plain.replace(' ','')
	k = keyGen(key)
	
	genCipher(plain,k)
	
	#print binToHex(k[0])
	#print binToHex(k[1])
	#print binToHex(k[2])
	
	

if __name__ == "__main__":
	main()
