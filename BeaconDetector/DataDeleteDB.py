from pymongo import MongoClient

def data_delete_db(databaseName, collectionName, filterList):
    print("")

    client = MongoClient('localhost', 27017)
    collection = client[databaseName][collectionName]

    for filter in filterList:
        collection.delete_many(filter)

    client.close()


if __name__ == "__main__":

    data_delete_db("mbeacon", "t_beacon", [{'user_id': "U001"}])
    #data_delete_db("mbeacon", "t_beacon", [{'user_id': "U001"},{'user_id': "U002"}])
    #data_delete_db("mbeacon", "t_beacon", [{'user_id': "U001"},{'user_id': "U002"},{'user_id': "U003"}])
