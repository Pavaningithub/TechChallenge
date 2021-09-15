import json

#Function to Parse JSON file retrieve based on KEY
def get_object_data(keys):
    with open('JsonObject.json') as f:
        data = json.load(f)
        val = keys.split('/')
        for key in val:   
            if key in data:
                data = data[key]
                if key == val[-1]:
                    print("value =", data)
            else:
                print(key, " :- Key doesn't exist in JSON Object")
                exit()

keys = input("please enter key to query: ")
get_object_data(keys)
