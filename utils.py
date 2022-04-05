import pandas as pd
import json
def init_table():
    df = pd.DataFrame(columns=["JobID", "CNode", "Status"])
    return df
def assign_node(df):
    df = df[df['Status']!='Finish']
    assign_list = df.value_counts()
    assign_node = assign_list.argmin()
    return assign_node
def create_job(assign_node, image_string):
    job_dict = {"CNode": assign_node, "Image": image_string}
    return json.dumps(job_dict)
