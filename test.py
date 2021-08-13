import urllib.request
import json, re
import pandas as pd


def validate(xyz):
    xyz.replace('"',"")
    return re.sub(r"'", r'"', xyz)


urls = ["http://localhost:8000/interfaces", "http://localhost:8000/interface/FastEthernet0/0"]

for i in urls:
    req = urllib.request.urlopen(i)
    output = req.read().decode()
    output = re.findall(r'(\{.*?\})', output)
    df = pd.DataFrame(map(lambda x: json.loads(validate(x)), output))
    print(df)
