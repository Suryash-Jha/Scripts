#!/usr/bin/python3            
#To find the python interpreter, when we execute it without python3

"""
To use:
./rank.py <contest-name>
"""

import requests
import json
import sys                                      #To get the passed arguments in terminal

main_url= "https://www.codechef.com/api/rankings/"
contest_name= sys.argv[1]
# contest_name= input("Enter Contest Name: ")
# contest_name="SEP221C"
# print(contest_name)

url= main_url+contest_name

dict={}

cookies = {
    '_fbp': 'fb.1.1655306318354.66392898',
    '_gcl_au': '1.1.2137790817.1655306319',
    'pg_mm2_cookie_a': '85654c31-1e1e-48ec-9f8b-0e71d258436a',
    'pg_custom_timeout': '',
    '_gaexp': 'GAX1.2.ZSnpSbMMTrSD8u_ztDmgRQ.19258.1!e86zI6iZQP21BjwhFrlHsw.19258.1!3OQ5zfjWSXuHlGe2eBjqbA.19258.1',
    'twk_uuid_627c0f75b0d10b6f3e71c35d': '%7B%22uuid%22%3A%221.H3NO5nd4jOeziibZm2mRXYSI3644LExvXsLy2XAJpeX6oKXKytIrDYkyJ5vtWMPxtdPxOmdp3K4GQf06bf07sXMb0lg4y6VSxlwRr20XGemYXnB479arAdNf5nK9agSM1Md8X1QD9MJkd5ss%22%2C%22version%22%3A3%2C%22domain%22%3A%22codechef.com%22%2C%22ts%22%3A1658326231790%7D',
    'twk_uuid_62397c18a34c2456412c3b26': '%7B%22uuid%22%3A%221.H3NMbQzCA5paUeWeHE3S0JdRNNp3WPDuQiFonJ8fJcBrCBAVhTuKUuCbnUKDAgn6QnnQCk4SSwVYleQBJh3z5Upe5NDi9N1RJ0vwflOcLcDwPvkQv50vgNeCcKHWYawcCZU7Rm3m7IMpr6Jl%22%2C%22version%22%3A3%2C%22domain%22%3A%22codechef.com%22%2C%22ts%22%3A1658577496450%7D',
    'pg_beacon': '1',
    'SESS93b6022d778ee317bf48f7dbffe03173': '439668598d6f0100c152f374307b95b8',
    'uid': '3137718',
    'pg_ip': '106.202.28.82',
    'FCNEC': '[["AKsRol8CCWw6bn69-Z9VofdR1ftk9RFdtdWy-fl4aSRwTQXyQ2tnwGnA2R0NgaJJNNGo4Q0b1AAaazrUVMCf0xkhE7qsb28Ihdt5Pj3igZ6QEN46V192fyjjxu6kYbyQegrxdcFhdS8DuPb3g-uGpKkpeuih3Sj3Ug=="],null,[]]',
    'pg_preconnecting': 'unset',
    '_gid': 'GA1.2.470779492.1662809140',
    'pg_after_init_response_time': '484',
    '_clck': '17nqn5c|1|f4s|0',
    'aasd': '1%7C1662888904152',
    '__aaxsc': '2',
    '__gads': 'ID=f702a7a3ed66e141:T=1655306346:S=ALNI_Ma-UnSJcmLeoqvlrVxBbOcG-Iw6tA',
    '__gpi': 'UID=000006ad96536525:T=1655306346:RT=1662888967:S=ALNI_MYP3iUpXkfMGriNtcMwBbc3u6ExUw',
    'pg_analytics': 'disabled',
    '_clsk': '167x5m4|1662898821498|4|1|b.clarity.ms/collect',
    '_gat_UA-141612136-1': '1',
    '_ga_C8RQQ7NY18': 'GS1.1.1662898158.81.1.1662899228.0.0.0',
    '_ga': 'GA1.1.306524194.1655306320',
    'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjb2RlY2hlZi5jb20iLCJzdWIiOiIzMTM3NzE4IiwidXNlcm5hbWUiOiJ0aGVfY29ucXVlcm9yOSIsImlhdCI6MTY2Mjg5OTI5MCwibmJmIjoxNjYyODk5MjkwLCJleHAiOjE2NjI5ODU2OTB9.p3lPQb96gMbIB6eRRu7ROH4wzw5uEIhAKUzhxK2tNpo',
}

headers = {
    'authority': 'www.codechef.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.codechef.com/rankings/SEP221C?filterBy=Institution%3DMaharaja%20Agrasen%20Institute%20of%20Technology%2C%20New%20Delhi&itemsPerPage=100&order=asc&page=1&sortBy=rank',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
    'x-csrf-token': '2dae1895146b9b0fe2c0b75b794922bd7eb973a1a4f362d2cc3e13dc17a96683',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'filterBy': 'Institution=Maharaja Agrasen Institute of Technology, New Delhi',
    'itemsPerPage': '100',
    'order': 'asc',
    'page': '1',
    'sortBy': 'rank',
}
print(url)
r = requests.get(url, params=params, cookies=cookies, headers=headers).json()
users= r['list']
c=1;
for i in users:
  v= []
  rankVar= i['rank']
  scoreVar= i['score']
  userIdVar= i['user_handle']
  v.append(rankVar)
  v.append(scoreVar)
  v.append(userIdVar)
  dict[c]= v;
  c+= 1

"""
To get coloured text, using ANSI

\033[1;31m -> RED
\033[1;32m -> GREEN
\033[1;37m -> WHITE

"""
print("\033[1;31mS.No. \t User ID \t \t \t \tRank \t \tScore")                  #
for i in dict:
  if(len(dict[i][2])<8):
      print(f'\033[1;37m {i}\t{dict[i][2]}\t\t\t\t\t{dict[i][0]}\t\t{dict[i][1]}')  
  elif(dict[i][2]=="the_conqueror9"):
      print(f'\033[1;32m {i}\t{dict[i][2]}\t\t\t\t{dict[i][0]}\t\t{dict[i][1]}')
  else:
      print(f'\033[1;37m {i}\t{dict[i][2]}\t\t\t\t{dict[i][0]}\t\t{dict[i][1]}')
