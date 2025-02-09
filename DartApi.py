#dartApiKey='a7910deaf71437b7ca18e2184ea4c9696eb82ecb'

import dart_fss as dart


api_key='a7910deaf71437b7ca18e2184ea4c9696eb82ecb'

dart.set_api_key(api_key=api_key)

corp_list = dart.get_corp_list()
samsung = corp_list.find_by_corp_name('삼성전자', exactly=True)[0]
