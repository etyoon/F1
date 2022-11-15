import matplotlib.pyplot as plt
import pandas as pd
from points_delta import *
from sponsor import *
from team_id import *
from trends import *

test = google_trends(['Kingfisher Airlines'], '2010-02-01 2010-12-1')
test2 = constructor_points('2010', 'force_india')

fig,ax = plt.subplots()
ax.plot(test.index, test.iloc[:,0].values, color = 'red')
ax.set_xlabel("date", fontsize = 14)
ax.set_ylabel("searches", color = 'red', fontsize = 14)

ax2 = ax.twinx()
ax2.plot(test2.iloc[:,1].values, test2.iloc[:,0].values, color = "orange")
ax2.set_ylabel('points', color = 'orange', fontsize = 14)

plt.show()
