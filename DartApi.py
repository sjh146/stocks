#dartApiKey='a7910deaf71437b7ca18e2184ea4c9696eb82ecb'
import requests
from io import BytesIO
import zipfile
import xmltodict

api = 'https://opendart.fss.or.kr/api/corpCode.xml'
res = requests.get(api, params={'crtfc_key': crtfc_key})
data_xml = zipfile.ZipFile(BytesIO(res.content))