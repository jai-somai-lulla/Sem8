import pandas as pd
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import time


def make_mfs(df):
	temperature = ctrl.Antecedent(np.arange(min(df['AT']), max(df['AT']), 1), 'temperature')
	humidity = ctrl.Antecedent(np.arange(min(df['RH']), max(df['RH']), 1), 'humidity')
	power = ctrl.Consequent(np.arange(min(df['PE']), max(df['PE']), 1), 'power')
	temperature.automf(names=['cold','medium','hot'])
	humidity.automf(names=['low','medium','high'])
	power.automf(names=['low','medium','high'])
	return temperature,humidity,power


def make_controller1(temperature,humidity,power):
	rule1 = ctrl.Rule(temperature['cold'] | humidity['low'], power['low'])
	rule2 = ctrl.Rule(temperature['medium'], power['medium'])
	rule3 = ctrl.Rule(temperature['hot'] | humidity['high'], power['high'])
	power_control = ctrl.ControlSystem([rule1, rule2, rule3])
	power = ctrl.ControlSystemSimulation(power_control)
	return power
	
def make_controller0(temperature,humidity,power):
	rule1 = ctrl.Rule(temperature['cold'] | humidity['medium'], power['high'])
	rule2 = ctrl.Rule(temperature['medium'], power['medium'])
	rule3 = ctrl.Rule(temperature['hot'] | humidity['high'], power['low'])
	power_control = ctrl.ControlSystem([rule1, rule2, rule3])
	power = ctrl.ControlSystemSimulation(power_control)
	return power	

def test_controller(controller,data):
	controller.input['temperature'] = data[0]
	controller.input['humidity'] = data[1]
	controller.compute()
	return controller.output['power']

def mse(controller,df):
	e=0
	for i in range(len(df)):
		op = test_controller(controller,[df['AT'][i],df['RH'][i]])
		e+= (op-df['PE'][i])**2
	return e/len(df)
	
def fitness(error):
	if(error<=0.0001):
		return 1
	else:
	 return 1/error
		

def main():
	print 'Power controller'
	df = pd.read_csv('data.csv')
	df =  df[0:20]
	print df	
	temperature,humidity,power=make_mfs(df)
	power_contorller1 = make_controller1(temperature,humidity,power)
	print fitness(mse(power_contorller1,df))
	
	power_contorller0 = make_controller0(temperature,humidity,power)
	print fitness(mse(power_contorller0,df))



if __name__ == '__main__':
	main()