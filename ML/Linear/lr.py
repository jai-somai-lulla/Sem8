import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression


def fit(s):
	xbar =  np.mean(s['year'])
	ybar = np.mean(s['value'])
	#print xbar,ybar
	work =pd.DataFrame(s)
	work['year']-=xbar
	work['value']-=ybar
	n = np.sum(work['year']*work['value'])
	d = np.sum(work['year']**2)
	m = float(n)/d
	c = ybar-(m*xbar)

	print 'm',m
	
	#print m,c
	return m,c

def fit2(s):
	xbar =  np.mean(s['year'])
	ybar = np.mean(s['value'])
	sdx = np.std(s['value'],ddof=1)
	sdy = np.std(s['year'],ddof=1)
	r = np.corrcoef(s['value'],s['year'])[0,1]
	print 'r',r
	print 'sdx',sdx
	print 'sdy',sdy
	
	m=(float(r*sdy)/(sdx))*(len(s)-1)
	c = ybar-(m*xbar)

	print 'm',m
	
	
	#print m,c
	return m,c

def lib(s):
	reg = LinearRegression().fit(np.array(s['year']).reshape(-1, 1), s['value'])
	print 'lrScore',reg.score(np.array(s['year']).reshape(-1, 1), s['value'])
	#print reg.coef_
	return reg.coef_,reg.intercept_
	
	
def pred(m,c,df):
	ypred = (df['year']*m) + c
	#print ypred
	mse = np.sum((ypred-df['value'])**2)
	m1 = np.sum((	np.mean(df['value'])	-	df['value']	)**2	)
	r = 1 - (float(mse)/m1)
	print "MSE",mse/len(df)
	print "R2",r
	plt.scatter(df['year'],df['value'])
	plt.plot(df['year'],ypred)
	plt.pause(10)
	
	
def main():
	print 'LR'
	df = pd.read_csv('dat.csv')
	#df.info()
	cols = list(df)
	#m,c = fit(df)
	#print 'BestFit'
	#pred(m,c,df)
	print '\n\nSK'
	m,c = lib(df)
	pred(m,c,df)

if __name__ == '__main__':
	main()