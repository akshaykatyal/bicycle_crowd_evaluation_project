import json
import numpy as np
import pandas as pd
from qm_utils import *
from matplotlib.pyplot import figure

'''
Task-2 Besides picking yes or no the annotators had the chance to tell if the data were
corrupted or if they for any reason were not able to solve the task. These are fields
'cant_solve' and 'corrupt_data' given in the task_output.
a. How often does each occur in the project and do you see a trend within the
annotators that made use of these options?

'''

data,keys = json_to_df(pd.read_json(r'C:\Users\Akshay\PycharmProjects\qm_tasks\data\anonymized_project.json'))
annotation_count = pd.read_csv(r"C:\Users\Akshay\PycharmProjects\qm_tasks\task1\annotation_count.csv")


def data_check(key, index):

    count_cantsolve= data[key]['results'][index]['task_output']['cant_solve']
    count_corruptdata = data[key]['results'][index]['task_output']['corrupt_data']
    return count_cantsolve or count_corruptdata


def return_data(key, index):
    user_id = data[key]['results'][index]['user']['vendor_user_id']
    count_cant_solve = data[key]['results'][index]['task_output']['cant_solve']
    count_corrupt_data = data[key]['results'][index]['task_output']['corrupt_data']
    return [user_id, int(count_cant_solve), int(count_corrupt_data)]


def result_count(user_id):

    result_count_dict = annotation_count.set_index('user_id').to_dict()
    count = result_count_dict['result_count'][user_id]
    return int(count)


# Gather rows of data with users with 'cant_solve' and 'corrupt_data'
bicycle_unsolve_data = []

for bicycle_key in keys:
    annotation_amount = len(data[bicycle_key]['results'])
    unsolve_data = [return_data(bicycle_key, i) for i in range(annotation_amount) if data_check(bicycle_key, i)]

    bicycle_unsolve_data.extend(unsolve_data)

unsolved_ids = sorted(set(np.array(bicycle_unsolve_data)[:, 0]))

print(unsolved_ids)
combined_unsolved_data = []

for idss in unsolved_ids:
    # getting answer from each user
    user_result = np.array([item for item in bicycle_unsolve_data if item[0] == idss])


    # getting count for corrupted and cant solve
    bicycle_cant_solve = np.sum(user_result[:, 1] == '1')
    bicycle_data_corrupt = np.sum(user_result[:, 2] == '1')

    # getting a list for the data
    combined_unsolved_data.append([id, bicycle_cant_solve, bicycle_data_corrupt])

combined_unsolved_data_df = pd.DataFrame(data=combined_unsolved_data,
                                        columns=['user_id', 'count_cant_solve', 'count_corrupt_data'])

print(combined_unsolved_data_df[['user_id', 'count_cant_solve', 'count_corrupt_data']])

figure(figsize=(8, 6), dpi=80)
ax1=combined_unsolved_data_df.plot(x='user_id',y=['count_cant_solve','count_corrupt_data'],kind='bar',figsize=(13,10))
ax1.set_xlabel('Annotation User Id')
ax1.set_ylabel('Cant-solve/corrupt Count')
ax1.figure.savefig('plot_for_cant_solve_&_corrupt_count.png')


