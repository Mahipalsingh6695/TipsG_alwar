import pymongo

# Direct MongoDB URI connection
client = pymongo.MongoClient("mongodb+srv://abhisheksainsain91:abhisheksain@91@cluster0.qrbma.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["examination_test"]
results_collection = db["results"]

class MongoDB:
    @staticmethod
    def save_result(result):
        results_collection.insert_one(result)

    @staticmethod
    def fetch_all_results():
        return list(results_collection.find())

    @staticmethod
    def fetch_sorted_results():
        return list(results_collection.find().sort("score", -1))