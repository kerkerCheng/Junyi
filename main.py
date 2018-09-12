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

tensor = {}
count = {}
rate = {}

for i in range(len(ok_user_list)):
    tensor[ok_user_list[i]] = np.zeros((338, 338))
    count[ok_user_list[i]] = np.zeros(338)
    rate[ok_user_list[i]] = np.zeros(338)

for i in range(ok_val.shape[0]):
    user_this = ok_val[i][0]
    sec_this = ok_val[i][2]
    (count[user_this])[sec_list.index(sec_this)] += 1

    if ok_val[i][5] is True:
        (rate[user_this])[sec_list.index(sec_this)] += 1

for key, value in rate.items():
    for i in range(338):
        if (count[key])[i] != 0:
            value[i] /= (count[key])[i]
