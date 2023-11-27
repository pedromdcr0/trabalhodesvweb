import time
from pymongo import MongoClient
from config import MONGODB_CONFIG


uri = f"mongodb+srv://{MONGODB_CONFIG['username']}:{MONGODB_CONFIG['password']}@cluster0.uknrsaf.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client["trabalho"]
estoque_collection = db["estoque"]
notas_collection = db["notas"]


def adicionar_estoque(nome, quantidade, quantmin, unidade, user):

    ultimo_item = estoque_collection.find_one(sort=[("Id", -1)])
    novo_id = ultimo_item["Id"] + 1 if ultimo_item else 1

    novo_item = {"Id": novo_id,
                 "Nome": nome.upper(),
                 "Quantidade": int(quantidade),
                 "QuantidadeMinima": int(quantmin),
                 "Unidade": unidade.upper()}

    estoque_collection.insert_one(novo_item)
    with open("arquivos/log.txt", "a") as log_file:
        log_cadastro = f"{time.asctime()} - CADASTRO - {novo_item} - POR {user}\n"
        log_file.write(log_cadastro)


def cadastrar_nota(nome, fornecedor, nota, data, preco, user):

    nota_add = {"Item": nome,
                "Fornecedor": fornecedor.upper(),
                "Nota": nota,
                "Data": data,
                "Preco": float(preco)}

    notas_collection.insert_one(nota_add)

    with open("arquivos/log.txt", "a") as log_file:
        log_cadastro_nota = f"{time.asctime()} - CADASTRO NOTA - {nota_add} - POR {user}\n"
        log_file.write(log_cadastro_nota)
