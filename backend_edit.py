import time
from pymongo import MongoClient
from config import MONGODB_CONFIG


uri = f"mongodb+srv://{MONGODB_CONFIG['username']}:{MONGODB_CONFIG['password']}@cluster0.uknrsaf.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client["trabalho"]
estoque_collection = db["estoque"]


def editar(id_passed, novo_nome, nova_quantidade, tipo, user):
    item_editavel = estoque_collection.find_one({"Id": int(id_passed)})

    if item_editavel:
        item_antes = item_editavel.copy()

        if int(tipo) == 1:
            item_editavel["Nome"] = novo_nome.upper()
            item_editavel["QuantidadeMinima"] = int(nova_quantidade)

        elif int(tipo) == 2:
            item_editavel["QuantidadeMinima"] = int(nova_quantidade)

        elif int(tipo) == 3:
            item_editavel["Nome"] = novo_nome.upper()

            # Atualizar o item na coleção
        estoque_collection.replace_one({"Id": int(id_passed)}, item_editavel)

        with open("arquivos/log.txt", "a") as log_file:
            log_edit_cadastro = (f"{time.asctime()} - EDITADO NO CADASTRO - {item_antes} - {item_editavel} - "
                                 f"POR: {user}\n")
            log_file.write(log_edit_cadastro)
    else:
        print("Item não encontrado no estoque")


def checar_item(id_item):
    item = estoque_collection.find_one({"Id": int(id_item)})

    if item:
        return True
    else:
        return False
