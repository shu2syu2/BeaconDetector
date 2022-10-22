import json
import datetime
from json2obj import JSONObjectMapper

def convSensorValue(userId, beaconId, rssiValue, dateLValue):
    json_value = JSONObjectMapper("""{
    "created_at": {
        "$date": {
        "$numberLong":""" + "\"" + str(dateLValue) + "\"" + """
        }
    },
    "user_id": """ + "\""  + str(userId) + "\""  + """,
    "beacon": [
        {
        "beacon_id": """ + "\""  + str(beaconId) + "\""  + """,
        "rssi": """ + str(rssiValue) + """
        }
    ]
    }""")
    return json_value
    
def data_create_json(userId, beaconId, rssiValue, rssiAdd, dateValue, secCount, outfile):

    dtStart = datetime.datetime(1970, 1, 1, 0, 0, 0, 0)
    dateDelta = dateValue - dtStart
    dateLValue = int(dateDelta.total_seconds() * 1000)

    arrayData = []
    for num in range(secCount):
        dbgDateDelta = datetime.timedelta(seconds=(dateLValue / 1000))
        dbgDateDelta = dtStart + dbgDateDelta
        print(dbgDateDelta)
        json_value = convSensorValue(userId, beaconId, rssiValue, dateLValue)
        arrayData.append(json_value.to_dict())
        dateLValue = dateLValue + 1000
        rssiValue = rssiValue + rssiAdd

    with open(outfile, 'w', encoding='utf-8') as f:
        json.dump(arrayData, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    userId = "U002"         # ユーザID
    beaconId = "B001"       # Beacon ID
    rssiValue = -30         # rssi start
    rssiAdd = -3            # next add rssi

    secCount = 3            # データ数
    # 開始時間
    datetimestr = "2022-10-19T14:12:31.000"
    dateValue = datetime.datetime.fromisoformat(datetimestr)

    outfile = "./t_beacon_add_" + str(secCount) + "_" + userId + "_" + beaconId  + "_" + dateValue.strftime("%Y%m%d%H%M%S") + ".json"

    data_create_json(userId, beaconId, rssiValue, rssiAdd, dateValue, secCount, outfile)
