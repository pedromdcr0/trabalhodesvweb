from pymongo import MongoClient
from config import MONGODB_CONFIG


uri = f"mongodb+srv://{MONGODB_CONFIG['username']}:{MONGODB_CONFIG['password']}@cluster0.uknrsaf.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)
db = client["trabalho"]
collection_estoque = db["estoque"]
collection_notas = db["notas"]


def pesquisa(input_pesquisa):
    dados_retornados = []

    resultados = collection_estoque.find({"Nome": {"$regex": input_pesquisa, "$options": "i"}})

    # Adicionar os resultados à lista dados_retornados
    for item in resultados:
        dados_retornados.append(item)

    return dados_retornados


def pesquisa_notas(input_pesquisa):
    dados_retornados = []

    resultados = collection_estoque.find({"Nome": {"$regex": input_pesquisa, "$options": "i"}})

    # Adicionar os resultados à lista dados_retornados
    for item in resultados:
        dados_retornados.append(item)

    return dados_retornados
