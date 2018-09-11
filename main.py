import pandas as pd
import scipy.io as sio
import numpy as np
import src

rate = src.get_dict()
key_list = list(rate.keys())

num_user = len(key_list)
num_sec = 338
rate_arr = np.zeros((num_user, num_sec))

for i in range(len(key_list)):
    rate_arr[i, :] = rate[key_list[i]]

sio.savemat('RateArray.mat', {'RateArray': rate_arr})
