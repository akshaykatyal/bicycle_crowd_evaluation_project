
import json
import pandas as pd
'''
Util functions that are used in task-3
'''


bicycle_ref=pd.read_json(r'C:\Users\Akshay\PycharmProjects\qm_tasks\data\references.json')

def bicycle_keys_get(df):
    """
    this is used to get the keys from the dataframe for the
    bicycle dataset in this case, keys are given
    """
    bicycle_keys = df.keys()
    return bicycle_ref, bicycle_keys

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