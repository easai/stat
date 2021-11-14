"""
変動係数
CV = Var[X]/E[X]
scipy.stats.variation(array)
"""

from scipy import stats

Biden=[28.2,28.3,25.6]
Sanders=[17.5,17.6,15.7]
Warren=[21.3,20.6,22.7]

print(stats.variation(Biden))
print(stats.variation(Sanders))
print(stats.variation(Warren))

"""
0.04567194460232075
0.051558271077593726
0.04054427508888167
"""