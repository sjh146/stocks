#dartApiKey='a7910deaf71437b7ca18e2184ea4c9696eb82ecb'
#url="https://opendart.fss.or.kr/api/corpCode.xml"

import requests
import io
import zipfile
import xmltodict
import pandas as pd

url="https://opendart.fss.or.kr/api/corpCode.xml"

api_key='a7910deaf71437b7ca18e2184ea4c9696eb82ecb'


params = {
    "crtfc_key": key
}
resp = requests.get(url, params=params)

f = io.BytesIO(resp.content)
zfile = zipfile.ZipFile(f)

zfile.namelist()

xml = zfile.read("CORPCODE.xml").decode("utf-8")
dict_data = xmltodict.parse(xml)

data = dict_data['result']['list']
df = pd.DataFrame(data)

df.head()