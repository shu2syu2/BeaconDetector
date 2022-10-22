from pymongo import MongoClient

def data_delete_db(userIds):
    print("")

    client = MongoClient('localhost', 27017)
    collection = client["mbeacon"]["t_beacon"]

    for user in userIds:
        collection.delete_many({'user_id': user})

    client.close()


if __name__ == "__main__":

    data_delete_db(["U001"])
    #data_delete_db(["U001", "U002"])
    #data_delete_db(["U001", "U002", "U003"])
