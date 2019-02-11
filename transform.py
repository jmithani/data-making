import sys
import json

raw = json.load(sys.stdin)

datasets = raw['result']['results']

formatted = []

for dset in datasets:
    if dset['url']:
        url  = dset['url']
    elif dset['resources']:
        url  = dset['resources'][0]['url']
    else:
        url  = 'none'

    #formatted.append(dset)

    formatted.append({
        'url': url,
        'title': dset['title'],
        'date': dset['metadata_modified']
    })

#print(type(datasets))

json.dump(formatted, sys.stdout)
