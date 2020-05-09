import json
import subprocess
import requests

filename = input("filename: ")
version = input("version code: ")
r = requests.get('https://getbible.net/json?version='+version)
r = r.text[1:]
r = json.loads(r[:-2])
with open(filename+"-version.json", "w") as outfile:
    json.dump(r, outfile)

