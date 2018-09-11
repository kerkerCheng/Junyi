import pandas as pd
import numpy as np
import collections


def get_dict():
    df_main = pd.read_csv('hash_junyi_section_learning_data.csv')

    df1 = df_main.drop(['exercise', 'difficulty', 'curriculum_guideline_id', 'section_ex_cnt'], axis=1)
    df1 = df1.sort_values(['user_primary_key', 'section_title'], ascending=[True, False])
    df1_val = df1.values

    sec = df1_val[:, 1:2]
    sec = np.unique(sec)

    sec_num_map = {}
    for i in range(len(sec)):
        sec_num_map[sec[i]] = i

    rate = {}
    time = {}

    for i in range(df1_val.shape[0]):
        rate[df1_val[i][0]] = np.zeros(len(sec))
        time[df1_val[i][0]] = np.zeros(len(sec))

    for i in range(df1_val.shape[0]):
        time[df1_val[i][0]][sec_num_map[df1_val[i][1]]] += 1
        if df1_val[i][2] is True:
            rate[df1_val[i][0]][sec_num_map[df1_val[i][1]]] += 1

    it = 0

    for key, value in rate.items():
        print(it)
        for i in range(len(value)):
            if time[key][i] != 0:
                value[i] /= time[key][i]
        it += 1

    return rate
