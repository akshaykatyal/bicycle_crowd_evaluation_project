import json
from qm_utils import *

import json
with open(r'C:\Users\Akshay\PycharmProjects\qm_tasks\data\anonymized_project.json') as audi_anon:    # loading annotations file
    annotations = json.load(audi_anon)

'''
Task-1.a Getting the number of annotators that are
supporting the tasks
'''
num_anno = bicycle_num_annotators(annotations)
# Printing the number of annotators contributing
print("Contributing annotators for the Tasks: ", num_anno)
