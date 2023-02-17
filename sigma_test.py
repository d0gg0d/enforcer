#!/usr/bin/env python3
import yaml
import uuid

ref_keys = ['title', 'id', 'status', 'description', 'references', 'author', 'date', 'modified', 'logsource', 'detection', 'falsepositives', 'tags', 'level']

def authorAdd(data):
    prepend = ', '
    name = 'Richard Han'
    data['author'] = data['author'] + prepend + name
    return data

def uuidAdd(data):
    uuid_value = str(uuid.uuid4()) 
    data['id'] = uuid_value
    return data

def sigmaSort(data):
    # Indenting isn't perfect so formatting needs to be fixed
    new_order = dict()
    for k in ref_keys:
        new_order[k] = data[k]
    return new_order

def newSigma():
    ruleName = 'new_rule.yml'
    with open(ruleName,'w') as output:
        for ref in ref_keys:
            output.write(ref+': \n')
    with open(ruleName) as f:
        data = yaml.load(f, Loader=yaml.loader.FullLoader)
        uuidAdd(data)
    with open(ruleName, 'w') as output:
        yaml.dump(data, output, sort_keys=False, default_flow_style=False,indent=1)


def tagSearch(data, tagName):
    items = list(data.items())
    sub_items = list(items[11][1])
    for value in sub_items:
        if value == tagName:
            print(data['title'])
            return
    


# with open('test.yml') as f:
#     data = yaml.load(f, Loader=yaml.loader.FullLoader)
#     print(data)
#     print("------------------")
#     print(data['author'])
#     print("-----------------")
#     # data['author'] = data['author'] + ', Richard Han'
#     # print(data['author']('Richard Han'))
#     authorAdd(data)
#     print(data['author'])
#     with open('out.yml', 'w') as o:
#         yaml.dump(data,o, sort_keys=False, default_flow_style=False)
# print("done")

with open('test.yml') as f:
    data = yaml.load(f, Loader=yaml.loader.FullLoader)
    #print(data.keys())
    data = sigmaSort(data)
    data = authorAdd(data)
    data = uuidAdd(data)
    newSigma()
    tagSearch(data, 'attack.t1003')
    
    #print(data.keys())
    #print(data)
    #items = list(data.items())
    #print(items[10])
    #sub_items = list(items[10][1])
    #print(sub_items[0])
    #print(sub_items[1])
    #print(sub_items[2])
    with open('out.yml', 'w') as output:
        yaml.dump(data, output, sort_keys=False, default_flow_style=False,indent=4)
    
