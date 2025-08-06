def serialize_tpot(modelo):
    import base64
    import pickle

    # -------- serialização do modelo (pickle -> base64) --------
    data = pickle.dumps(modelo)
    modelo_pickle_b64 = base64.b64encode(data).decode("ascii")

    return {"model": modelo_pickle_b64}
