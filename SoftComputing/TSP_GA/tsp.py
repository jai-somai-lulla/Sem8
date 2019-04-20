import numpy as np
import random
import math
from pprint import pprint
from operator import itemgetter 
import operator
from matplotlib import pyplot as plt



population_size = 15 #Paths
chromosome_size = 8 #Citys in path
GENERATIONS = 10
	
	
#def showList(l):
#	for c in l:
		
#GENE
class City:
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
	
	def show(self):
		print '(',self.x,',',self.y,')'	
	
	def distancefrom(self,city):
		dx=(self.x-city.x)**2
		dy=(self.y-city.y)**2	
		dist=pow((dx+dy),0.5)
		#print dx,dy,dist
		return dist	
		
	def equals(self,city):
		if(self.x==city.x and self.y==city.y):
			return True
		return False
					
#DNA||CHROMOSOME
class Path:
	#cList=CityList
	#path if given then no random init, if stated then copied
	def __init__(self,cList=[],path=[]):
		self.cityList=list(cList)
		self.cCount=len(cList)
		if (len(path)==0):
			self.path = self.randGen(list(self.cityList))
		else:
			self.path = path
			
	def getPath(self):
		return list(self.path)		
			
	def randGen(self,cityList):
		p=[]
		for _ in range(self.cCount):	
			r = random.randrange(0,len(cityList))
			p.append(cityList[r])
			del cityList[r]
		return p	 
		
	def makePath(self,path):
		print 's'
		
	def show(self):
		print '--PSEX--',self.fitness()	
		for i in range(len(self.path)):
				self.path[i].show()
		print '--PSEX--\n'	
		
	def fitness(self):
		total_dist	= 0
		fit=1
		for i in range(len(self.path)):
			total_dist	+= self.path[i].distancefrom(self.path[(i+1)%len(self.path)])
		#print total_dist
		
		#fit = self.cCount*100-(total_dist)
		fit = self.cCount**10/(total_dist**3)
		
		#print "Fit", fit
		return fit	
			
	def plot(self,g):
		plt.title("TSP:"+str(self.fitness())+"  "+str(g))
		plt.style.use('seaborn-whitegrid')
		for i in range(len(self.path)):
			plt.scatter(self.path[i].x,self.path[i].y,marker='.', c='r', s=50)
			plt.plot((self.path[i].x,self.path[(i+1)%len(self.path)].x),(self.path[i].y,self.path[(i+1)%len(self.path)].y),color="green",linestyle=':')
			plt.text(self.path[i].x+0.1,self.path[i].y+0, 'C{i}'.format(i=i),fontsize=15)
		
		#plt.show(block=False)
		plt.pause(0.01)
		#raw_input("Press any Key to Continue:")			
		plt.clf()
		#plt.cla()
		#plt.close()
			
	def crossover(self,spouse):
		sp=spouse.getPath()
		child =  [City()] * self.cCount
		ca=0 
		cb=0
		while(ca<cb+1):
			ca = int(random.random()*self.cCount)
			cb = int(random.random()*self.cCount)	
		cA = min(ca,cb)
		cB = max(ca,cb)
		#print cA,cB
				
		for i in range(cA,cB):
			child[i]=(sp[i])
		pos=0
		adder=[]	
		
		for i in range(0,self.cCount):
			ele = self.path[i]
			add = True
			for j in range(0,self.cCount):
				if(child[j].equals(ele)):
					add=False
					break
			if(add):
				adder.append(ele)
		for i in range(0,cA):
			child[i]=adder[pos]
			pos+=1
			
		for i in range(cB,self.cCount):					
			child[i]=adder[pos]
			pos+=1
					
				#child[i]=self.path[i]	
		return Path(self.cityList,child)#.show()




	def mutate(self, mutationRate=0.15):
		individual=self.path
		for swapped in range(len(individual)):
			if(random.random() < mutationRate):
				swapWith = int(random.random() * len(individual))
				city1 = individual[swapped]
				city2 = individual[swapWith]
				individual[swapped] = city2
				individual[swapWith] = city1
		return self



			
def init_population(population_size,cityList):
	population = []
	#Rand Gen of City Locations
	for i in range(population_size):
		population.append(Path(cityList))
	return population	
	
def showPopulation(population):
	for path in population:
		path.show()
		
def roulette(wpop,population_size):
	population=[]
	for chno in range(population_size):		
		#print '\n\nCho ',chno
		i=0
		cumSum=0
		temp = list(wpop)
		r = random.uniform(0,np.sum(np.array(temp)[:,1]))
		#print "Rand:",r

		#print "S Len",len(temp)		
		
		for tup in temp:
			cumSum+=tup[1]
			if(cumSum>r):
				#print 'Selected item ',i
				p1 = temp.pop(i)
				break
			i+=1
		#print "Mid Len",len(temp)		
		
		i=0
		cumSum=0
		r = random.uniform(0,np.sum(np.array(temp)[:,1]))
		for tup in temp:
			cumSum+=tup[1]
			if(cumSum>r):
				#print 'Selected item ',i
				p2 = temp.pop(i)
				break
			i+=1		
		#print "Now Len",len(temp)		
		population.append(p1[0].crossover(p2[0]))
	return population

def rank(wpop,population_size):
	#print 'Rank'
	temp = list(wpop)
	temp.sort(key=itemgetter(1))
	ranked=[]
	i=0
	for t in temp:
		ranked.append((t[0],i))
		i+=1	
		
	population=[]
	
	for chno in range(population_size):		
		#print '\n\nCho ',chno
		i=0
		cumSum=0
		temp = list(ranked)
		random.shuffle(temp)
		#print temp
		#for i in temp:
		#	print i
		r = random.randrange(0,np.sum(np.array(temp)[:,1]))
		#print "Rand:",r

		#print "S Len",len(temp)		
		
		for tup in temp:
			cumSum+=tup[1]
			if(cumSum>r):
				#print 'Selected item ',i
				p1 = temp.pop(i)
				#print p1
				break
			i+=1
		#print "Mid Len",len(temp)		
		
		i=0
		cumSum=0
		r = random.randrange(0,np.sum(np.array(temp)[:,1]))
		for tup in temp:
			cumSum+=tup[1]
			if(cumSum>r):
				#print 'Selected item ',i
				p2 = temp.pop(i)
				break
			i+=1		
		#print "Now Len",len(temp)		
		population.append(p1[0].crossover(p2[0]))
	return population

def tournament(wpop,population_size):
	#print 'Torni'	
	t_size = int(population_size*0.1)
	
	population = []
	for chno in range(population_size):		
		temp = list(wpop)
		t_players = []
		for i in range(t_size):
			r = random.randrange(0,len(temp))
			#print 'choose ',temp[r]
			t_players.append(temp.pop(r))
			#print 'temp size',len(temp)
		p1 = max(t_players, key = itemgetter(1))

		temp = list(wpop)
		t_players = []
		for i in range(t_size):
			r = random.randrange(0,len(temp))
			#print 'choose ',temp[r]
			t_players.append(temp.pop(r))
			#print 'temp size',len(temp)
		p2 = max(t_players, key = itemgetter(1))
	
		population.append(p1[0].crossover(p2[0]))
	return population	
	
def random_select(wpop,population_size):
	population = []
	for chno in range(population_size):	
		r = random.randrange(0,len(wpop))
		p1 = wpop[r]
		r = random.randrange(0,len(wpop))
		p2 = wpop[r]	
		population.append(p1[0].crossover(p2[0]))
	return population
		
def breed(wpop,population_size):
	totalfit=0
	arr=[]
	expanded=[]
	for tup in wpop:
		totalfit+=tup[1]
		arr.append([tup[0],tup[1]])
	#pprint(arr)
	data = np.zeros(population_size, dtype={'names':('name', 'weight'),
                          'formats':('object', 'f8')})
	arr = np.array(arr)
	#pprint(arr)
	
	data['weight']= arr[:,1].astype(np.float)
	data['weight']=data['weight']/totalfit
	data['name']= arr[:,0]
	#print '\n\n'
	#pprint (data)
	
	for i in range(population_size):
		 p=np.random.choice(data['name'],2,replace=False, p=data['weight'])
		 
		 c = p[0].crossover(p[1])
		 expanded.append(c)
		 
	#print '\n\nAfter Breeding:'
	#pprint(expanded)	 
	return expanded	
	
def mutate(population):	
	mutate_pop=[]
	for dna in population:
		mutate_pop.append(dna.mutate())
	return mutate_pop
def main():
	#print 'TSP'

	cityList=[]
	for i in range(chromosome_size):
		 cityList.append(City(random.randrange(0,1000),random.randrange(0,1000)))
	

	pmain = init_population(population_size,cityList)	


	num_method=5
	#num_rows=2
	
	#final_fit=np.array(([[0.0]*num_method])*num_rows)
	final_fit=np.array([0.0]*num_method)
	
	for method in range(num_method):
		population=list(pmain)
		for g in range(GENERATIONS):
			wpop=[]
			for cromosome in population:
				wpop.append((cromosome,cromosome.fitness()))
			fittest = max(wpop, key = itemgetter(1))[0] 
			#print "GENERATION",g,"Best :","Fitness:",fittest.fitness()	
			#fittest.show()
			
			
			#############Turn on Live display##############
			fittest.plot("Method:["+str(method)+"]  Genertation:"+str(g))
			#############Turn on Live display##############		
			if method==0:
				population = tournament(wpop,population_size)
			if method==1:
				population = random_select(wpop,population_size)
			if method==2:
				population = roulette(wpop,population_size)
			if method==3:
				population = rank(wpop,population_size)
			if method==4:
				if(g<(3*GENERATIONS/4)):
					population = roulette(wpop,population_size)	
				else:
					population = rank(wpop,population_size)
				
			population = mutate(population)
			
			#ELITEISM

			del population[population_size-1]
			population.append(fittest) 
			
			
			#print '\n\n\n'
		#final_fit[0][method]=fittest.fitness()
		final_fit[method]=fittest.fitness()
	#print final_fit	
	return final_fit
	
def plotfiitestcurve(y):
	p=[]
	for i in range(len(y)):
		p.append((i,y[i]))	
	p = np.array(p)
	plt.plot(p[:,0],p[:,1])
	plt.show()		


def data_runner():
	data=[]
	test_cases=10
	for i in range(test_cases):	
		data.append(main())
		
	acc = np.mean(data,axis=0)
	#print acc
	d={}
	d['Tournament'] = acc[0]
	d['Random_select'] = acc[1]
	d['Roulette'] = acc[2]
	d['Rank_select'] = acc[3]
	d['Roulette-Rank '] = acc[4]
	
	
	sorted_d = sorted(d.items(), key=operator.itemgetter(1),reverse =True)
	#pprint(sorted_d)
	objects=[]
	performance=[]
	for t in sorted_d:
		#print ''
		print t[0],"		Average Fitness:",t[1]
		objects.append(t[0])
		performance.append(t[1])
	
	performance = ((performance ) / np.max(performance))*100
	#print e
	y_pos = np.arange(len(objects))
	plt.bar(y_pos, performance, align='center', alpha=1)
	plt.xticks(y_pos, objects)
	plt.ylabel('Fitness Score')
	
	plt.rcParams["axes.titlesize"] = 8
	plt.title('\n\nAverage Fitness Over ['+str(test_cases)+ '] Test cases' + '\nPopulation size(Number of paths):'+str(population_size)+ '\nChromosome size(Number of Cities):'+ str(chromosome_size) + "\nGENERATIONS:" +str(GENERATIONS)) 
	plt.pause(14)
	
	#plt.plot()
	#plt.savefig('Average Fitness Over ['+str(test_cases)+ '] Test cases' + ' Population size(Number of paths):'+str(population_size)+ 'Chromosome size(Number of Cities):'+ str(chromosome_size) + " GENERATIONS:" +str(GENERATIONS)+'.png')	
		
		

if __name__=='__main__':
	#main()
	data_runner()
	
