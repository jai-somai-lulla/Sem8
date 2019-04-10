import random
from pprint import pprint
from operator import itemgetter 
import numpy as np
from numpy.random import choice

'''
Population
In a GA, each iteration, or generation, results in a series of possible hypotheses for best approximating a function, and the population refers to the complete set or pool of these generated hypotheses after a given iteration.

Chromosome | DNA
In an obvious nod to biology, a chromosome is a single hypothesis of which many make up a population.

Gene
In a GA, potential hypotheses are made up of chromosomes, which are, in turn, made up of genes. Practically, in a GA, chromosomes are generally represented as binary strings, a series of 1s and 0s, which denote inclusion or exclusion of particular items represented by position in the string. A gene is a single bit within such a chromosome.
'''


def init_population(population_size,chromosome_size):
	pop = []
	for c in range(population_size):
		dna=''
		for g in range(chromosome_size):
			 dna+=chr(random.randrange(32,126))
		pop.append(dna)
	#print pop
	return pop		 

def fitness(dna,optimal):
	fitness = 0
	for c in xrange(len(dna)):
		fitness += abs(ord(dna[c]) - ord(optimal[c]))
	if(fitness==0):
		return 1
	else:
		return 1.0/fitness	
		 			 			
def crossover(parent1, parent2,dnasize):
	child = ''
	ca = int(random.random() * dnasize)
	cb = int(random.random() * dnasize)
	#print parent1, parent2
	cB= max(ca,cb)
	cA= min(ca,cb)
	#print cA,cB
	
	for i in range(dnasize):
		if(i>=cA and i<=cB):
			child+=parent1[i]
		else:
			child+=parent2[i] 	
	#print "P1 ",parent1,"P2 ",parent2,"Child",child
	#print child
	return child	

def breed(wpop,population_size):
	totalfit=0
	arr=[]
	expanded=[]
	for tup in wpop:
		totalfit+=tup[1]
		arr.append([tup[0],tup[1]])
	#pprint(arr)
	data = np.zeros(population_size, dtype={'names':('name', 'weight'),
                          'formats':('U11', 'f8')})
	arr = np.array(arr)
	
	data['weight']= arr[:,1].astype(np.float)
	data['weight']=data['weight']/totalfit
	data['name']= arr[:,0]
	#print '\n\n'
	#pprint (data)
	
	for i in range(population_size):
		 p=np.random.choice(data['name'],2,replace=False, p=data['weight'])
		 
		 c = crossover(p[0], p[1], len(p[0]))
		 expanded.append(c)
		 
	#print '\n\nAfter Breeding:'
	#pprint(expanded)	 
	return expanded	
	
def mutate(population):
	thresh=0.2
	mute_pop=[]
	for dna in population:
		crom=''
		for gene in dna:
			r=random.random()
			#print r,thresh,r>thresh
			if(r<thresh):
				#print 'here:::'
				gene=chr(random.randrange(32,126))		
	 		crom+=gene	
		mute_pop.append(crom)
	#print '\nAfter Mutation:'
	#pprint(mute_pop)
	return mute_pop		 		
		
def main():
	optimal="HELLO TANVI"
	population_size = 50
	chromosome_size = len(optimal)
	print "\nGenetic Algorithm\n"
	print "Goal:",optimal
	print "Population Size",population_size
	print "Chromosome Size",chromosome_size
	print '\n'
	GENERATIONS = 100000
	
	population = init_population(population_size,chromosome_size)	
	#del population[1]
	#population.append(optimal)
	#crossover("adssadas","fisdoapq" ,8)
	#population = mutate(population)
	#return 
	for g in range(GENERATIONS):
		wpop=[]
		for dna in population:
			wpop.append((dna,fitness(dna,optimal)))
		#pprint(wpop)
		res = max(wpop, key = itemgetter(1))[0] 
		print "GENERATION",g,"Best :",res,"Fitness:",fitness(res,optimal)	
		#print '\nThis GEN:'
		##pprint(population)
		#population=[]
		#pprint(population)
		
		population = breed(wpop,population_size)
		#print '\nAfter Breeding:'
		#pprint(population)
		
		#
		#population.append(res)
		
		population = mutate(population)
		#print '\nAfter Mutation:'
		print '\n\n\n'
		pprint(population)
		
		del population[1]
		population.append(res)
		if(fitness(res,optimal)==1):
			print "Found"
			return
		

if __name__=="__main__":
	main()	