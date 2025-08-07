def serialize_tpot(modelo):
    import base64
    import pickle

    # -------- serialização do modelo (pickle -> base64) --------
    data = pickle.dumps(modelo)
    modelo_pickle_b64 = base64.b64encode(data).decode("ascii")

    return modelo_pickle_b64


def carregar_modelo(modelo_pickle_b64):
    """
    Recebe o campo 'modelo_pickle_b64' (string base64) e retorna o modelo carregado.
    Uso típico:
      modelo = carregar_modelo_pickle_b64(doc['model']['modelo_pickle_b64'])
      preds = modelo.predict(X_test)
    """
    import base64

    import dill as pickle  # conforme a doc que você está usando

    if not isinstance(modelo_pickle_b64, str) or not modelo_pickle_b64.strip():
        raise ValueError(
            "modelo_pickle_b64 inválido: forneça a string base64 do modelo."
        )

    data = base64.b64decode(modelo_pickle_b64)
    modelo = pickle.loads(data)  # carrega direto dos bytes
    return modelo
