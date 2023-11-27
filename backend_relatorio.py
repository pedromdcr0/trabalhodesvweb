from pymongo.mongo_client import MongoClient
from config import MONGODB_CONFIG


uri = f"mongodb+srv://{MONGODB_CONFIG['username']}:{MONGODB_CONFIG['password']}@cluster0.uknrsaf.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client["trabalho"]
collection = db["estoque"]

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


def preencher_relatorio():
    dados_relatorio = []
    data = collection.find()

    for item in data:
        if item["Quantidade"] < item["QuantidadeMinima"]:
            dados_relatorio.append(item)
        elif item["Quantidade"] <= 1.2 * item["QuantidadeMinima"]:
            dados_relatorio.append(item)
        else:
            pass

    return dados_relatorio
