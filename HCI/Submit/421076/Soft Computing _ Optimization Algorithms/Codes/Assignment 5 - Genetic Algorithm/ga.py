import random
from pprint import pprint
from operator import itemgetter 
def fitness(x):
	return abs((int(x,2)-7491)**2)
	


def init_population(population_size,chromosome_size):
	pop = []
	for c in range(population_size):
		pop.append(bin(random.randrange(0,2**chromosome_size))[2:].zfill(4))
	return pop	
	
def crossover(p1,p2):
	a=0
	b=0
	while(a<b-1):
		a = random.uniform(0,1)*len(p1)
		b = random.uniform(0,1)*len(p1)	
	c1=''
	for g in range(len(p1)):
		if(g<a or g>b):
			c1+=p1[g]
		else:
			c1+=p2[g]
	return c1		
		
	
def breed(wpop,population_size):
#	print 'breed'	
	t_size = int(0.3*population_size)
	population=[]
	for ch_no in range(population_size):
		temp = list(wpop)
		torn = []
		for i in range(t_size):
			torn.append(temp.pop(random.randrange(0,len(temp))))
		p1 = min(wpop, key = itemgetter(1))[0] 
	
		temp = list(wpop)
		torn = []
		for i in range(t_size):
			torn.append(temp.pop(random.randrange(0,len(temp))))
		p2 = min(wpop, key = itemgetter(1))[0] 
		c = crossover(p1,p2)
		population.append(c)
	return population	
			
def mutate(population):
	thresh=0.2
	mute_pop=[]
	for dna in population:
		crom=''
	#	print '---CROMMMMM--'
		for gene in dna:
			r=random.random()
			#print r,thresh,r>thresh
			if(r<thresh):
				#print 'here:::'
				#print 'mute'
				gene=str(random.randrange(0,2))	
				#print gene
				#print ''	
	 		crom+=gene
	 	#	print crom	
	 	#print '---CROMMMMM--'	
		mute_pop.append(crom)
	#print '\nAfter Mutation:'
	#pprint(mute_pop)
	return mute_pop

			
	
	
def main():
	population_size = 8
	chromosome_size = 32
	print "\nGenetic Algorithm\n"
	print "Population Size",population_size
	print "Chromosome Size",chromosome_size
	print '\n'
	GENERATIONS = 10000
	population = init_population(population_size,chromosome_size)	
	print population
	
	
	for g in range(GENERATIONS):
		wpop=[]
		for dna in population:
			wpop.append((dna,fitness(dna)))
		pprint(wpop)
		res = min(wpop, key = itemgetter(1))[0] 
		print "GENERATION",g,"Best :",res,"Fitness:",fitness(res)	
		#print '\nThis GEN:'
		##pprint(population)
		#population=[]
		#pprint(population)
		
		population=breed(wpop,population_size)
		#print '\nAfter Breeding:'
		#pprint(population)
		
		#
		#population.append(res)
		
		population = mutate(population)
		#print '\nAfter Mutation:'
		#print '\n\n\n'
		#pprint(population)
		
		del population[1]
		population.append(res)
		if(fitness(res)==0):
			print "Found",(int(res,2))
			return


if __name__=="__main__":
	main()	