import pandas as pd
import numpy as np
import collections


def get_all_rate_dict():
    df_main = pd.read_csv('hash_junyi_section_learning_data.csv')

    df1 = df_main.drop(['exercise', 'difficulty', 'curriculum_guideline_id', 'section_ex_cnt'], axis=1)
    df1_val = df1.values

    sec_list = np.load('section_list.npy').tolist()

    rate = {}
    time = {}

    for i in range(df1_val.shape[0]):
        rate[df1_val[i][0]] = np.zeros(len(sec_list))
        time[df1_val[i][0]] = np.zeros(len(sec_list))

    for i in range(df1_val.shape[0]):
        time[df1_val[i][0]][sec_list.index(df1_val[i][1])] += 1
        if df1_val[i][2] is True:
            rate[df1_val[i][0]][sec_list.index(df1_val[i][1])] += 1

    it = 0

    np.save('user_section_times_dict.npy', time)

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


def get_grade_ok_users_list(grade_list, threshold):
    user_times_dict = np.load('user_section_times_dict.npy').item()
    sec_list = np.load('section_list.npy').tolist()
    ans_list = []

    mask = np.zeros((len(sec_list)), dtype=bool)

    for i in range(len(sec_list)):
        if sec_list[i] in grade_list:
            mask[i] = True

    for key, item in user_times_dict.items():
        tmp = item[mask]
        times = np.count_nonzero(tmp)
        if times >= threshold:
            ans_list.append(key)

    return ans_list


def get_new_df(df_main, user_list):
    main_df_val = df_main.value
    mask = np.zeros(main_df_val.shape[0], dtype=bool)

    for i in range(main_df_val.shape[0]):
        if main_df_val[i][0] in user_list:
            mask[i] = True

    new_df_val = main_df_val[mask, :]
    new_df = pd.DataFrame(new_df_val)

    return new_df


def get_grade_dict(filename, sec_list, rate):

    grade_sec = []
    f = open(filename, 'r', encoding='utf-8')

    for line in f:
        grade_sec.append(line.strip(' \n'))

    mask = np.zeros(len(sec_list))
    for i in range(len(sec_list)):
        if sec_list[i] in grade_sec:
            mask[i] = 1

    mask = mask.astype(bool)

    for key, item in rate.items():
        rate[key] = item[mask]

    return rate


def get_grade_ok_rate_dict(ok_user_list):
    ans = {}
    rate_dict = np.load('all_user_rate_dict.npy').item()

    for key, item in rate_dict.items():
        if key in ok_user_list:
            ans[key] = item

    return ans


def mask_grade_ok_rate_dict(grade_sec, rate):

    sec_list = np.load('section_list.npy').tolist()
    mask = np.zeros(len(sec_list), dtype=bool)
    for i in range(len(sec_list)):
        if sec_list[i] in grade_sec:
            mask[i] = True

    for key, item in rate.items():
        rate[key] = item[mask]

    return rate

