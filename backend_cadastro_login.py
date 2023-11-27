from pymongo import MongoClient
from config import MONGODB_CONFIG


uri = f"mongodb+srv://{MONGODB_CONFIG['username']}:{MONGODB_CONFIG['password']}@cluster0.uknrsaf.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)
db = client["trabalho"]
login_collection = db["login"]


def cadastro(usuario, senha, conf_senha, admin):

    if login_collection.find_one({"Username": usuario}):
        print(usuario)
        print("Usuário já existe")
        return False

    # Verificar se as senhas coincidem
    if senha != conf_senha:
        print("Senhas não coincidem")
        return False

    # Inserir novo usuário no MongoDB
    novo_login = {"Username": usuario, "Password": senha, "Admin": admin}
    login_collection.insert_one(novo_login)

    print("Cadastro realizado com sucesso")
    return True