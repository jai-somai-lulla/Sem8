import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from copy import deepcopy
#0.1489

def main():
	print 'K-Means'
	data = np.array([(0.1,0.6),(0.15,0.71),(0.08,0.9),(0.16,0.85),(0.2,0.3),(0.25,0.5),(0.24,0.1),(0.3,0.2)])
	#data = np.array([(2,3),(2,1),(1,3),(-2,-3),(-1,-3),(-2,-1)])
	centers = np.array([(0.1,0.6),(0.3,0.2)])
	n = data.shape[0]
	c = data.shape[1]
	k = centers.shape[0]
	print "Data"
	print data
	print "Centers"
	print centers
	clusters = np.zeros(n)
	distances = np.zeros((n,k))
	
main()