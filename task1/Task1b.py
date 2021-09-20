import json
from qm_utils import *
from matplotlib.pyplot import figure
'''
Task-1.b What are the average, min and max annotation times (durations)? Feel free to
add visual representations here such as graphs if you like.
'''
data, keys = json_to_df(pd.read_json(r'C:\Users\Akshay\PycharmProjects\qm_tasks\data\anonymized_project.json'))
'''
This gets the duration data from the json file that is the
anonymized json project and then plots the time duration 
gets the average, min and also max
'''
annotation_durations = []
for bicycle_key in keys:
    data_amount = len(data[bicycle_key]['results'])

    # getting data that is not corrupted as some 'corrupted' key is given
    rows = [bicycle_duration_data(bicycle_key,data, i) for i in range(data_amount)
                if not data[bicycle_key]['results'][i]['task_output']['corrupt_data']]

    # getting the data to the list
    annotation_durations.extend(rows)


# Store data to dataframe
bicycle_duration_df = pd.DataFrame(data=annotation_durations, columns=['user_id','duration'])

print(bicycle_duration_df.describe())
df2 =bicycle_duration_df.groupby(['user_id'], sort=False)['duration'].sum()
figure(figsize=(8, 6), dpi=80)
ax=df2.plot(kind='bar')
ax.set_xlabel('Annotation User Id')
ax.set_ylabel('Count')
ax.figure.savefig('plot_for_time_before-clean.png')
# Duration has some negative values removing that and cleaning the data

bicycle_duration_df=bicycle_duration_df.loc[bicycle_duration_df['duration'] > 0]

# Again printing the data
df2 =bicycle_duration_df.groupby(['user_id'], sort=False)['duration'].sum()
figure(figsize=(8, 6), dpi=80)
ax1=df2.plot(kind='bar')
ax1.set_xlabel('Annotation User Id')
ax1.set_ylabel('Count')
ax1.figure.savefig('plot_for_time_after-clean.png')

print(bicycle_duration_df.describe())
bicyle_annotation_duration=[i for i in bicycle_duration_df['duration']]

avg_annotation_time=sum(bicyle_annotation_duration)/len(bicycle_duration_df)
maximum_time = max(bicyle_annotation_duration)
minimum_time=min(bicyle_annotation_duration)
# print the average annotation time
print("The average annotation time is " + str(avg_annotation_time))
# print the max annotation time
print("The max annotation time is " + str(maximum_time))
# print the min annotation time
print("The min annotation time is " + str(minimum_time))
