from pymongo import MongoClient
from config import MONGODB_CONFIG


uri = f"mongodb+srv://{MONGODB_CONFIG['username']}:{MONGODB_CONFIG['password']}@cluster0.uknrsaf.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)
db = client["trabalho"]
collection_estoque = db["estoque"]
collection_notas = db["notas"]


def preencher_dados():
    dados = []

    data = collection_estoque.find()

    dados.clear()
    for item in data:
        dados.append(item)

    return dados


def preencher_notas(id_item):
    dados_notas = []
    print(id_item)
    nome = None

    estoque_data = collection_estoque.find({"Id": int(id_item)})
    print(estoque_data)

    for item in estoque_data:
        nome = item["Nome"]

    notas_data = collection_notas.find({"Item": nome})
    dados_notas.clear()

    for item in notas_data:
        dados_notas.append(item)

    print(dados_notas)

    return dados_notas
