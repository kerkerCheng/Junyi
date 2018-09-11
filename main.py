import pandas as pd
import scipy.io as sio
import numpy as np
import src
import collections

num_sec = 338

df_main = pd.read_csv('hash_junyi_section_learning_data.csv')

df1 = df_main.drop(['exercise', 'difficulty', 'curriculum_guideline_id', 'section_ex_cnt'], axis=1)
df1 = df1.sort_values(['user_primary_key', 'section_title'], ascending=[True, False])
df1_val = df1.values

dd = collections.defaultdict(list)
dd_to_unique_num = {}

for i in range(df1_val.shape[0]):
    dd[df1_val[i][0]].append(df1_val[i][1])

for key, item in dd.items():
    dd_to_unique_num[key] = len(np.unique(item))

th = 50
ok_user_list = []

for key, item in dd_to_unique_num.items():
    if item > th:
        ok_user_list.append(key)

