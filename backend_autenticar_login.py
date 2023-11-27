from pymongo import MongoClient
from config import MONGODB_CONFIG


uri = f"mongodb+srv://{MONGODB_CONFIG['username']}:{MONGODB_CONFIG['password']}@cluster0.uknrsaf.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)
db = client["trabalho"]
login_collection = db["login"]


def autenticar(username, password):
    user = login_collection.find_one({"Username": username, "Password": password})

    if user:
        if user["Admin"] == 1:
            print("admin")
            return True
        elif user["Admin"] == 0:
            print("nonadmin")
            return False

    print("naoencontrado")
    return None