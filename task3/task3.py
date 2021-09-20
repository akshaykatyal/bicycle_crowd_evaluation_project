import json
import numpy as np
import pandas as pd
from qm_utils import *
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

'''
Task-3 Is the reference set balanced? Please demonstrate via numbers and visualizations.
'''

data,keys = bicycle_keys_get(pd.read_json(r'C:\Users\Akshay\PycharmProjects\qm_tasks\data\references.json'))
# getting the reference data
get_refernce = [[bicycle_ref_key, data[bicycle_ref_key]['is_bicycle']] for bicycle_ref_key in keys]
reference_array= np.array(get_refernce)
# changing to the dataframe
get_ref_df = pd.DataFrame({'image_key': reference_array[:, 0], 'image_is_bicycle': reference_array[:, 1]})
get_ref_df = get_ref_df.groupby('image_is_bicycle').nunique()
ax1 = get_ref_df.plot.bar(y='image_key',figsize=(8,6))
ax1.set_title("Checking whether reference set is balanced")
ax1.figure.savefig('Check_references_balance_or_not')

