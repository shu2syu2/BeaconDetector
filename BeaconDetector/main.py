import json
import datetime

date = datetime.datetime(year=2022, month=10, day=1, hour=0, minute=0, second=0)
sensor = 10

dt = datetime.datetime.fromtimestamp()

seconds = date.long

str = {
    "東京":{
        "population": sensor,
        "capital": "東京"
    },
    "北海道":{
        "population": 538,
        "capital": "札幌市"
    },
    "沖縄":{
        "population": 143,
        "capital": "那覇市"
    }
}

with open('.\population.json', 'w', encoding='utf-8') as f:
    json.dump(str, f, ensure_ascii=False)
