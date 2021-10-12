import json
from collections import OrderedDict

EXISTING_DATA_FILE_PATH = '../packages/web/src/coh/data/cu2021/commanderData.json'
NEW_DATA_FILE_PATH = '../scripts/commanderData.json'

orderedOriginal = {}
newData = {}

with open(EXISTING_DATA_FILE_PATH, "r") as originalFile:
    orderedOriginal = json.load(originalFile, object_pairs_hook=OrderedDict)

with open(NEW_DATA_FILE_PATH, "r") as newFile:
    newData = json.load(newFile)

for k, v in orderedOriginal.items():
    for ability in v['abilities']:
        newAbility = [x for x in newData[k]['abilities'] if x['name'] == ability['name']][0]
        ability['commandPoints'] = newAbility['commandPoints']

with open(EXISTING_DATA_FILE_PATH, "w", encoding='utf-8') as originalFile:
    json.dump(orderedOriginal, originalFile, ensure_ascii=False, indent=2)
    # output = json.dumps(orderedOriginal, ensure_ascii=False, indent=2)
    # output2 = re.sub(r'": \[\s+', '": [', output)
    # output3 = re.sub(r'",\s+', '", ', output2)
    # output4 = re.sub(r'"\s+\]', '"]', output3)
    # originalFile.write(output4)