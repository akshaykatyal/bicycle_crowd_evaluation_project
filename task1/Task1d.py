import json
import numpy as np
from qm_utils import *
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
'''
Task-1.c Are there questions for which annotators highly disagree?
'''

data,keys = json_to_df(pd.read_json(r'C:\Users\Akshay\PycharmProjects\qm_tasks\data\anonymized_project.json'))
bicycle_annotation_disagree = []

for bicycle_key in keys:
    bicycle_data_amount = len(data[bicycle_key]['results'])
    bicycle_data_answers = [data[bicycle_key]['results'][i]['task_output']['answer'] for i in range(bicycle_data_amount)]
    bicycle_data_solves = [data[bicycle_key]['results'][i]['task_output']['cant_solve'] for i in range(bicycle_data_amount)]
    bicycle_ans_yes = bicycle_data_answers.count('yes')
    bicycle_ans_no = bicycle_data_answers.count('no')
    bicycle_annotation_disagree.append([bicycle_key, bicycle_ans_yes, bicycle_ans_no])

# creating a dataframe for annotations
bicycle_annotation_df=pd.DataFrame(data=bicycle_annotation_disagree,columns=["key_id", "solve_yes", "solve_no"])
mean_yes=bicycle_annotation_df['solve_yes'].mean()
mean_no=bicycle_annotation_df['solve_no'].mean()
figure(figsize=(8, 6), dpi=80)
ax=bicycle_annotation_df.plot(x="key_id",y=['solve_yes','solve_no'],kind='bar')
ax.set_xlabel('Annotation User Id')
ax.set_ylabel('Disagreement count Yes/No')
ax.figure.savefig('plot_for_checking_disagreement.png')
print(bicycle_annotation_df)

# plotting pie chart
pie_labels = 'solve_yes', 'solve_no'
pie_values = [bicycle_annotation_df['solve_yes'].mean(),
              bicycle_annotation_df['solve_no'].mean()]


plot3, axx1= plt.subplots()
axx1.pie(pie_values,autopct='%1.3f%%', startangle=90)
axx1.axis('equal')
axx1.set_title("Disagreement check")
axx1.legend(pie_labels)
axx1.figure.savefig('plot_for_checking_disagreement-pie-chart.png')