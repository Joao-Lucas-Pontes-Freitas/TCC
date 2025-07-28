"""
Módulo para operações com MongoDB
"""
import os
from pathlib import Path
from pymongo import MongoClient
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)


def mongo_insert(doc: dict, mongo_uri: str = None, mongo_db: str = None, mongo_collection: str = None):
    """
    Insere um documento no MongoDB
    
    Args:
        doc: Documento a ser inserido
        mongo_uri: URI de conexão do MongoDB (se None, usa variável de ambiente)
        mongo_db: Nome do banco de dados (se None, usa variável de ambiente)
        mongo_collection: Nome da coleção (se None, usa variável de ambiente)
    
    Returns:
        str: ID do documento inserido ou None em caso de erro
    """
    # Usar valores das variáveis de ambiente se não fornecidos
    if mongo_uri is None:
        mongo_uri = os.getenv("MONGODB_CONNECTION_STRING")
    if mongo_db is None:
        mongo_db = os.getenv("MONGODB_DB")
    if mongo_collection is None:
        mongo_collection = os.getenv("MONGODB_COLLECTION")
    
    client = None
    try:
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
        collection = client[mongo_db][mongo_collection]
        res = collection.insert_one(doc)
        return str(res.inserted_id)
    except Exception as e:
        print(f"Erro ao inserir no MongoDB: {e}")
        return None
    finally:
        if client:
            client.close()