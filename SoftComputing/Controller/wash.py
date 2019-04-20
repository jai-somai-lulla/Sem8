import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import time
secs=5
temperature = ctrl.Antecedent(np.arange(10, 50, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 11, 1), 'humidity')
power = ctrl.Consequent(np.arange(0, 26, 1), 'power')


temperature.automf(names=['cold','medium','hot'])
humidity.automf(names=['low','medium','high'])

power['low'] = fuzz.trimf(power.universe, [0, 0, 13])
power['medium'] = fuzz.trimf(power.universe, [0, 13, 25])
power['high'] = fuzz.trimf(power.universe, [13, 25, 25])


rule1 = ctrl.Rule(temperature['cold'] | humidity['low'], power['low'])
rule2 = ctrl.Rule(temperature['medium'], power['medium'])
rule3 = ctrl.Rule(temperature['hot'] | humidity['high'], power['high'])

power_control = ctrl.ControlSystem([rule1, rule2, rule3])

power = ctrl.ControlSystemSimulation(power_control)


power.inputs({'temperature':21,'humidity':5})


power.compute()
print power.output['power']


