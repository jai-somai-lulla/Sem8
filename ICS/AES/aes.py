key = "0111111101111111" #16 bit
text = "1011011001111001" #16 bit	
rounds = 2

def RotNib(data):
	p1 = data[:4]
	p2 = data[4:]            	
	return (p2+p1)

def main():
	w=[[],[],[],[]]
	print "======Key-Gen======\n\n"
	print key
	w[0]=key[:8]
	w[1]=key[8:]
	print w[1]
	print RotNib(w[1])
	#w[2] = w[0] XOR 10000000 XOR SubNib(RotNib(w[1]))
	
	print "W :"+str(w)

if __name__ == "__main__":
	main()
