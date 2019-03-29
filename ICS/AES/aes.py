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
	
def invSubNibble(nibble):
	matrix= [['A','5','9','B'],
	['1','7','8','F'],
	['6','0','2','3'],
	['C','4','D','E']] 

	col = int(nibble[2]+nibble[3],2)
	row = int(nibble[0]+nibble[1],2)
	return matrix[row][col]

def fieldMul(k,n):
	ans=0	
	if k==4:
		ans=n*k
		while(ans>=16):
			if(ans>=32):
				ans%=19
			ans^=19
		
	elif k==2:
		ans=2*k
		if(ans>15):
			ans=ans^19
	elif k==9:
		ans=n*k
		#if(ans)
		
	print "K	:",k
	print "N	:",n
		
	print "Mult	: {:x}".format(ans)
	print ''
	return ans
	
def fieldTable(k,n):
	table={4:['0', '4', '8', 'c', '3', '7', 'b', 'f', '6', '2', 'e', 'a', '5', '1', 'd', '9'],
	2:['0' ,'2' ,'4' ,'6', '8', 'a' ,'c' ,'e', '3' ,'1' ,'7' ,'5' ,'b' ,'9' ,'f' ,'d'],
	9:['0' ,'9' ,'1' ,'8' ,'2' ,'b' ,'3' ,'a', '4' ,'d' ,'5' ,'c', '6', 'f ','7', 'e' ]
	}
	return table[k][n] 

def mixcolumns(n1,n2):
	n1=int(n1,16)
	n2=int(n2,16)

	a1=(n1) ^ int(fieldTable(4,n2),16)
	a2=int(fieldTable(4,n1),16) ^ (n2)	
	
	return '{:x}'.format(a1),'{:x}'.format(a2)

def invmixcolumns(n1,n2):
	n1=int(n1,16)
	n2=int(n2,16)
	a1=int(fieldTable(9,n1),16) ^ int(fieldTable(2,n2),16)
	a2=int(fieldTable(2,n1),16) ^ int(fieldTable(9,n2),16)
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
	print 'Key 0		:' +k[0] + "  " +binToHex(k[0])	
	print 'Key 1		:' +k[1] + "  " +binToHex(k[1])
	print 'Key 2		:' +k[2] + "  " +binToHex(k[2])
	return k

def genCipher(plain,k):

	print '\n\n -----Encryption----- \n'
	print 'Plain Text	:' +plain + "  " +binToHex(plain)
	print '\nPreGame'
	print 'Key 0		:' +k[0] + "  " +binToHex(k[0])
	
	#Pre Round Transform
	prt = xorbin(plain,k[0],16)
	print 'PreR		:'+ prt+ "  " +binToHex(prt)
		
		
	#Round 1
	print '\nRound 1'
	temp=''
	for i in range(4):
		temp+= subNibble(prt[i*4:(i+1)*4])	
	print 'Sub :'+temp
	
	
	#t1=temp[:2]
	#t2=rotate(temp[2:],1)
	#temp=t1+t2
	t1=temp[0]+temp[3]+temp[2]+temp[1]
	temp=t1
	print 'Rot :'+temp
	
	t0,t1	= mixcolumns(temp[0],temp[1])
	t2,t3	= mixcolumns(temp[2],temp[3])
	temp = t0+t1+t2+t3
	print 'MIX :'+ temp
	
	print 'Key 1		:' +k[1] + "  " +binToHex(k[1])
	temp=xorhex(temp,binToHex(k[1]))
	print 'ARK :'+ temp
	
	print '\nRound 2'	
	#Round 2
	prt=hexToBin(temp,16)
	print 'PRT2 :'+ prt
	temp=''
	for i in range(4):
		temp+=subNibble(prt[i*4:(i+1)*4])
	print 'Sub :'+temp
	
	t1=temp[0]+temp[3]+temp[2]+temp[1]
	temp=t1
	print 'Rot :'+temp
	
	print 'Key 2		:' +k[2] + "  " +binToHex(k[2])
	temp=xorhex(temp,binToHex(k[2]))
	print 'ARK :'+ temp
	
	
	return temp
	
def genPlain(cipher,k):
	
	print '\n\n -----Decryption----- \n'
	temp=cipher
	print 'temp		:',temp
	
	#r2inv
	temp=xorhex(temp,binToHex(k[2]))
	print 'temp		:',temp
	
	t1=temp[0]+temp[3]+temp[2]+temp[1]
	temp=t1
	print 'temp		:',temp
	
	prt=hexToBin(temp,16)
	#print 'PRT2 :'+ prt
	temp=''
	for i in range(4):
		temp+=invSubNibble(prt[i*4:(i+1)*4])
	
	print 'Give to r1 inv :',temp	
		
	#r1	inv
	temp=xorhex(temp,binToHex(k[1]))	
	print 'temp		:',temp
	
	t0,t1	= invmixcolumns(temp[0],temp[1])
	t2,t3	= invmixcolumns(temp[2],temp[3])
	temp = t0+t1+t2+t3
	print 'temp		:',temp
	
	t1=temp[0]+temp[3]+temp[2]+temp[1]
	temp=t1
	print 'temp		:',temp
	
	prt=hexToBin(temp,16)
	temp=''
	for i in range(4):
		temp+= invSubNibble(prt[i*4:(i+1)*4])	
		
	#pre round	
	temp = xorhex(temp,binToHex(k[0]))
	print 'temp		Final:',temp
	
	return temp
	
	
	
def main():
	key = "0010 0100 0111 0101" #16 bit
	plain = "0001 1010 0010 0011" #16 bit
	rounds = 2
	plain = plain.replace(' ','')
	k = keyGen(key)
	#for i in range(16):
	#	fieldMul(4,i)
	cipher=genCipher(plain,k)
	print "Cipher	       :",hexToBin(cipher,16)," 0x",cipher 
	
	pt=genPlain(cipher,k)
	print "Plain	       :",hexToBin(pt,16)," 0x",pt 
	#print binToHex(k[0])
	#print binToHex(k[1])
	#print binToHex(k[2])
	
	

if __name__ == "__main__":
	main()
