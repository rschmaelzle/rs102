def test():
    assert (
        'spacy.load("en_core_web_md")' in __solution__
    ), "¿Estás cargando el modelo mediano correctamente?"
    assert "doc[1].vector" in __solution__, "¿Estás obteniendo el vector correcto?"
    __msg__.good(
        "¡Bien hecho! En el próximo ejercicio usarás a spaCy para predecir "
        "similitudes entre documentos, spans y tokens a través de los word vectors "
        "usados detrás de cámaras."
    )
