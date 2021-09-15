import requests
import json

# function to get meta data details 
def fn(key):
    url = 'http://169.254.169.254/latest/meta-data/' + key
    val = requests.get(url)
    val = val.content.decode("utf-8").replace('/','')
    if "\n" in val:
        val = val.splitlines()
    return val

# function to convert to json
def dict_to_json(dict):
    return json.dumps(dict, indent = 4)

# Query a particular data key from instance metadata
data_key = input("please enter data key to query:")
datadict = {}
datadict[data_key] = fn(data_key)
print(dict_to_json(datadict))