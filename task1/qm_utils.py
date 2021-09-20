import json
import pandas as pd

'''
Util functions that are used in subtasks of task-1
'''


def bicycle_num_annotators(anno):
	'''
	1.a This function returns the number of annotators that work for the
	solving of the task this function returns the number of annotators present in the
	json and that support the tasks
	'''
	bicycle_annotators = set()
	bicycle_tasks = anno["results"]["root_node"]["results"]
	for task_id in bicycle_tasks:
		for result in bicycle_tasks[task_id]["results"]:
			bicycle_annotators.add(result["user"]["id"])
	print(bicycle_annotators)
	bicycle_annotators = sorted(set(bicycle_annotators))
	save_todf = pd.DataFrame({'Names of annotators': bicycle_annotators})
	save_todf.to_csv("bicycle_annotators.csv", index=False)
	return len(bicycle_annotators)


def json_to_df(audi_data):
	"""
	Function to get the keys for the json file
	this function takes the json and changes that to dataframe
	"""
	audi_data = audi_data.iloc[0][0]['results']
	audi_keys = list(audi_data.keys())
	return audi_data, audi_keys

def bicycle_duration_data(key,data, index):
    '''
    takes key and data from the json file and gets the data required for the
    use, here it is the duration data
    '''
    task_user_id = data[key]['results'][index]['user']['vendor_user_id']
    task_duration = data[key]['results'][index]['task_output']['duration_ms']
    return [task_user_id, task_duration]