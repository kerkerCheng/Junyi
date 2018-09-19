import pandas as pd
import scipy.io as so
import numpy as np
import src
import collections

num_sec = 338

df_main = pd.read_csv('hash_junyi_section_learning_data.csv')
df_val = df_main.values

grade_sec = []
f = open('first_grade_sec.txt', 'r', encoding='utf-8')
for line in f:
    grade_sec.append(line.strip(' \n'))

first_grade_ok_user_list = src.get_grade_ok_users_list(grade_sec, 8, 8)
grade_ok_rate_dict = src.get_grade_ok_rate_dict(first_grade_ok_user_list)
grade_ok_rate_dict = src.mask_grade_ok_rate_dict(grade_sec, grade_ok_rate_dict)

tensor = np.zeros((len(first_grade_ok_user_list), 13, 13))

k = 0
for key, value in grade_ok_rate_dict.items():
    for i in range(13):
        for j in range(13):
            tensor[k][i][j] = (value[i]*value[j])**0.5
    k += 1

so.savemat('first_grade_ok_tensor', dict(tensor=tensor))
