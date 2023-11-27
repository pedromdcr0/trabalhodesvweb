
import time
from pymongo import MongoClient
from config import MONGODB_CONFIG


uri = f"mongodb+srv://{MONGODB_CONFIG['username']}:{MONGODB_CONFIG['password']}@cluster0.uknrsaf.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client["trabalho"]
estoque_collection = db["estoque"]
notas_collection = db["notas"]


def remover_item(id_item, user):
    item_removido = estoque_collection.find_one({"Id": id_item})

    if item_removido:
        estoque_collection.delete_one({"Id": id_item})
        estoque_collection.update_many({"Id": {"$gt": id_item}}, {"$inc": {"Id": -1}})

        with open("arquivos/log.txt", "a") as log_file:
            log_rmv_cadastro = (f"{time.asctime()} - REMOVIDO DO CADASTRO - {item_removido} - "
                                f"POR: {user}\n")
            log_file.write(log_rmv_cadastro)
    else:
        print("item nao encontrado")


def remover_nota(id_nota, user):
    nota_removida = notas_collection.find_one({"Nota": id_nota})

    if nota_removida:
        notas_collection.delete_one({"Nota": id_nota})

        with open("arquivos/log.txt", "a") as log_file:
            log_rmv_nota = f"{time.asctime()} - NOTA REMOVIDA - {nota_removida} - POR: {user}\n"
            log_file.write(log_rmv_nota)
    else:
        print("Nota não encontrada")


