from __future__ import annotations

import os
from typing import Any, Mapping
from pymongo import MongoClient
from pymongo.errors import (
    ServerSelectionTimeoutError, ConnectionFailure,
    ConfigurationError, OperationFailure,
)

ENV_PATH = "/home/joao/Documentos/TCC/.env"
APP_NAME = "TCC"

def _env(name: str) -> str:
    v = os.getenv(name)
    if not v or not v.strip():
        raise RuntimeError(f"variável de ambiente ausente: {name}")
    return v.strip()

def _normalize_uri(uri: str, app_name: str = APP_NAME) -> str:
    """Garante retryWrites, w=majority e appName sem duplicar parâmetros."""
    add = []
    if "retryWrites=" not in uri:
        add.append("retryWrites=true")
    if "w=" not in uri:
        add.append("w=majority")
    if "appName=" not in uri:
        add.append(f"appName={app_name}")
    if add:
        uri += ("&" if "?" in uri else "?") + "&".join(add)
    return uri

def get_client(uri: str | None = None) -> MongoClient:
    uri = _normalize_uri((uri or _env("MONGODB_CONNECTION_STRING")).strip())
    return MongoClient(
        uri,
        serverSelectionTimeoutMS=10000,
        connectTimeoutMS=10000,
        socketTimeoutMS=20000,
    )

def mongo_insert(doc: Mapping[str, Any],
                 mongo_db: str | None = None,
                 mongo_collection: str | None = None,
                 mongo_uri: str | None = None) -> str:
    """Insere um documento e retorna o _id como string."""
    db = mongo_db or _env("MONGODB_DB")
    coll = mongo_collection or _env("MONGODB_COLLECTION")
    client: MongoClient | None = None
    try:
        client = get_client(mongo_uri)
        client.admin.command("ping")
        res = client[db][coll].insert_one(dict(doc))
        return str(res.inserted_id)
    except (ServerSelectionTimeoutError, ConnectionFailure,
            ConfigurationError, OperationFailure) as e:
        raise RuntimeError(f"falha Mongo: {e}") from e
    finally:
        if client:
            client.close()