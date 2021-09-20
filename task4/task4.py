import json
import numpy as np
import pandas as pd
from qm_utils import *
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt


'''
Task-4 Using the reference set, can you identify good and bad annotators? Please use
statistics and visualizations. Feel free to get creative.
'''

data,keys = json_to_df(pd.read_json(r'C:\Users\Akshay\PycharmProjects\qm_tasks\data\anonymized_project.json'))
data2,keys2 = bicycle_keys_get(pd.read_json(r'C:\Users\Akshay\PycharmProjects\qm_tasks\data\references.json'))

# bicycle annotations get
annotations_result=[]
for bicycle_key in keys:
    data_amount = len(data[bicycle_key]['results'])
    data_id=[data[bicycle_key]['results'][i]['user']['vendor_user_id'] for i in range(data_amount)]
    annotations_result.extend(data_id)
annotations_result = sorted(set(annotations_result))

# using the reference to get data
get_refernce = [[bicycle_ref_key, data2[bicycle_ref_key]['is_bicycle']] for bicycle_ref_key in keys2]


annotators_bicycle_res = []
for bicycle_key in keys:
    data_amount = len(data[bicycle_key]['results'])
    data_id = [data[bicycle_key]['results'][i]['user']['vendor_user_id'] for i in range(data_amount)]
    data_answers= [data[bicycle_key]['results'][i]['task_output']['answer'] for i in range(data_amount)]
    # image name
    bicycle_image_url = data[bicycle_key]['results'][0]['task_input']['image_url']
    bicycle_image_name = bicycle_image_url.split("/")[-1]
    bicycle_image_name = bicycle_image_name.split(".")[0]

    for ids, ans in zip(data_id, data_answers):
        annotators_bicycle_res.append([ids, bicycle_image_name, ans])

# getting the annotators group
bicycle_annotators_group = []
for res in annotations_result:
    temp = [[ids, bicycle_image_name, ans] for ids, bicycle_image_name, ans in annotators_bicycle_res if res == ids]
    bicycle_annotators_group.append(temp)


# Count the good,bad,and blank answers
bicycle_annotators_quality = []
for bicycle_annotators in bicycle_annotators_group:
    # getting the values
    good,bad,blank = 0, 0, 0

    # getting the annotations
    bicycle_user_id = bicycle_annotators[0][0]

    # getting the count for the good,bad, and blank answer
    for id, image, annotator in bicycle_annotators:
        # getting the answers from the reference
        ids = [i for i, ref in enumerate(get_refernce) if image in ref][0]
        # checking the condition
        bicycle_good = annotator == 'yes' and get_refernce[ids][1]
        bicycle_bad = annotator == 'no' and not get_refernce[ids][1]
        bicycle_blank = annotator== ""
        # storing the if condition result
        if bicycle_good or bicycle_bad:
            good += 1
        elif bicycle_blank:
            blank += 1
        else:
            bad += 1

    bicycle_total_result = good+bad+blank

    # storing data to list
    bicycle_annotators_quality.append([bicycle_user_id, good,bad,blank,bicycle_total_result])

    print(bicycle_user_id, good,bad,blank,bicycle_total_result)


# getting the dataframe for visualization
bicycle_annotator_df = pd.DataFrame(data=bicycle_annotators_quality,
                                     columns=['bicycle_user_id', 'good','bad','blank','bicycle_total_result'])

bicycle_annotator_df.to_csv("annotation_quality_result.csv", index=False)



# reading the data got in previous step from csv file for plotting
bicycle_annotator_result_df = pd.read_csv(r"C:\Users\Akshay\PycharmProjects\qm_tasks\qm_task1\annotation_count.csv")
bicycle_annotator_df= pd.read_csv(r"C:\Users\Akshay\PycharmProjects\qm_tasks\task4\annotation_quality_result.csv")
bicycle_annotator = bicycle_annotator_df.values.tolist()


# getting bar plot
labels = bicycle_annotator_df['bicycle_user_id']
bicycle_display_data= bicycle_annotator_df[['good', 'bad', 'blank']]
ax1 = bicycle_display_data.plot(kind='bar', stacked=True, use_index=False,figsize=(13,10))
ax1.set_xticklabels(labels)
ax1.grid(True)
ax1.set_title("Result for Annotators")
ax1.set_xlabel("Id for Annotators")
ax1.set_ylabel("result_count")
ax1.figure.savefig('annotator_result_count')

# getting the pie chart
pie_labels = 'good', 'bad', 'blank'
pie_values = [bicycle_annotator_df['good'].mean(),
              bicycle_annotator_df['bad'].mean(),
              bicycle_annotator_df['blank'].mean()]

# storing the plots
plot3, axx1= plt.subplots()
axx1.pie(pie_values,autopct='%1.3f%%', startangle=90)
axx1.axis('equal')
axx1.set_title("Performance of Bicycle annotators")
axx1.legend(pie_labels)
axx1.figure.savefig('annotator_result_count-mean() pie chart')