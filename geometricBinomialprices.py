import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd

#creating a function
def gbm (so=10,mean=0.15,stddev=0.30,weeks=1,totalweeks=52):
    T = weeks/totalweeks
    rootT = math.sqrt(T)
    newPrice = list()
    random = np.random.normal(0,1,10)

    for i in range(len(random)):
        newPrice.append(so+((mean*so*T) +(stddev*so*random[i]*rootT)))
    print(newPrice)

gbm(so = 100)

price = gbm(so = 100)

plt.plot(gbm(so = 100), marker = 'o')
#plt.xticks(range(0,len(price)+1,1))
plt.show()







