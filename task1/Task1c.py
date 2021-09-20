import json
import numpy as np
from qm_utils import *
from matplotlib.pyplot import figure

'''
Task-1.c Did all annotators produce the same amount of results, or are there
differences?
'''

data,keys = json_to_df(pd.read_json(r'C:\Users\Akshay\PycharmProjects\qm_tasks\data\anonymized_project.json'))

annotations_result=[]
for bicycle_key in keys:
    data_amount = len(data[bicycle_key]['results'])
    data_id=[data[bicycle_key]['results'][i]['user']['vendor_user_id'] for i in range(data_amount)]
    annotations_result.extend(data_id)

# getting occurence of each annotator
bicycle_annotators, bicycle_annotator_count = np.unique(np.array(annotations_result), return_counts=True)

print(bicycle_annotators,bicycle_annotator_count)

# creating a dataframe
df3 = pd.DataFrame({"user_id": bicycle_annotators, "annotation_count": bicycle_annotator_count})
print(df3)
figure(figsize=(8, 6), dpi=80)
ax=df3.plot(kind='bar')
ax.set_xlabel('Annotation User Id')
ax.set_ylabel('Annotations Count')
ax.figure.savefig('plot_for_checking_annotation difference.png')
df3.to_csv("annotation_count.csv", index=False)