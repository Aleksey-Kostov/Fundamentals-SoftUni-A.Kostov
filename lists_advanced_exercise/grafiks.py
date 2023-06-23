import json
from time import time, gmtime, ctime
from urllib import request
import datetime
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from contourpy.util import data

plt.ylabel('kW')
#plt.axis([0, 24, 0, 500])
plt.ylim(0, 500)
plt.xlim(tm_hour())
plt.xlabel('time')
plt.grid(True)

plt.legend()
plt.show()
