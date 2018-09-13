import pandas as pd
import scipy.io as so
import numpy as np
import src
import collections

num_sec = 338

df_main = pd.read_csv('hash_junyi_section_learning_data.csv')
df_val = df_main.values

ok_user_list = np.load('morethan100_section_userslist.npy').tolist()
all_user_list = np.load('all_user_list.npy').tolist()
sec_list = np.load('section_list.npy').tolist()

ok_df = pd.read_csv('more_than_100_sec_users.csv')
ok_df = ok_df.sort_values(['user_primary_key', 'section_title'], ascending=[True, False])
ok_val = ok_df.values

rate = np.load('ok_user_rate_mapping.npy').item()
tensor = np.zeros((len(ok_user_list), 338, 338))

k = 0
for key, value in rate.items():
    for i in range(338):
        for j in range(338):
            tensor[k][i][j] = (value[i]*value[j])**0.5
    k += 1

