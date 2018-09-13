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


def get_ok_users_list(threshold):
    dic = np.load('dict_users_to_unique_num_sec.npy').item()
    ans = []
    for key, value in dic.items():
        if value > threshold:
            ans.append(key)

    return ans


def get_new_df(main_df, user_list):
    main_df_val = main_df.value
    mask = np.zeros(main_df_val.shape[0], dtype=bool)

    for i in range(main_df_val.shape[0]):
        if main_df_val[i][0] in user_list:
            mask[i] = True

    new_df_val = main_df_val[mask, :]
    new_df = pd.DataFrame(new_df_val)

    return new_df


def get_rate_dic(ok_user_list, ok_val):
    sec_list = np.load('section_list.npy').tolist()
    count = {}
    rate = {}

    for i in range(len(ok_user_list)):
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

    return rate