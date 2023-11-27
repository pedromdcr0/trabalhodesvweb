import time
from pymongo import MongoClient
from config import MONGODB_CONFIG


uri = f"mongodb+srv://{MONGODB_CONFIG['username']}:{MONGODB_CONFIG['password']}@cluster0.uknrsaf.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client["trabalho"]
collection = db["estoque"]

id_item = None


def receber_id(id_recebido):
    global id_item
    id_item = int(id_recebido)
    return id_item


def retornar_item(id_do_item):
    data = collection.find()

    if id_do_item.isdigit():
        for item in data:
            if item["Id"] == int(id_do_item):
                return item
            else:
                print("nao é numero")


def add_rmv(id_addrmv, tipo, quantidade, user):
    global id_item
    if tipo == 1:  # ADD

        item = collection.find_one({"Id": int(id_addrmv)})
        if item:
            valor_atualizado = item["Quantidade"] + quantidade
            collection.update_one({"Id": int(id_addrmv)}, {"$set": {"Quantidade": valor_atualizado}})

            with open("arquivos/log.txt", "a") as log_file:
                log_soma_cadastro = (f"{time.asctime()} - SOMADO NO ESTOQUE ({quantidade}) -"
                                     f" {item} - POR: {user}\n")
                log_file.write(log_soma_cadastro)

        else:
            print("naotem")

    elif tipo == 2:  # RMV
        item = collection.find_one({"Id": int(id_addrmv)})
        if item:
            valor_atualizado = item["Quantidade"] - quantidade
            collection.update_one({"Id": int(id_addrmv)}, {"$set": {"Quantidade": valor_atualizado}})

            with open("arquivos/log.txt", "a") as log_file:
                log_soma_cadastro = (f"{time.asctime()} - SUBTRAIDO NO ESTOQUE ({quantidade}) -"
                                     f" {item} - POR: {user}\n")
                log_file.write(log_soma_cadastro)

        else:
            print("naotem")


def checar_item(id_passed):

    dados_estoque = collection.find_one({"Id": id_passed})

    if dados_estoque:
        print('sem alert')
        return 0
    else:
        print('alert?')
        return 1
