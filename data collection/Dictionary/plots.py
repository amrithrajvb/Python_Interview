import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as pyt
from matplotlib import rcParams
import seaborn as sb



rcParams['figure.figsize']=5,4
sb.set_style('whitegrid')

x=range(1,10)
y=[1,2,3,0,4,3,2,1,1,]
plt.plot(x,y)



