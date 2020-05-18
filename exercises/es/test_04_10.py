def test():
    assert len(TRAINING_DATA) == 4, "Los datos de entrenamiento no concuerdan – esperaba 4 ejemplos."
    assert all(
        len(entry) == 2 and isinstance(entry[1], dict) for entry in TRAINING_DATA
    ), "Formato incorrecto de los datos de entrenamiento. Esperaba una lista de tuples dónde el segundo elemento es un dict."
    assert all(
        entry[1].get("entities") for entry in TRAINING_DATA
    ), "Todas las anotaciones en los datos de entrenamiento deberían incluir entidades."
    assert TRAINING_DATA[0][1]["entities"] == [
        (10, 19, "GPE")
    ], "Vuelve a revisar las entidades en el primer ejemplo."
    assert TRAINING_DATA[1][1]["entities"] == [
        (17, 22, "GPE")
    ], "Vuelve a revisar las entidades en el segundo ejemplo."
    assert TRAINING_DATA[2][1]["entities"] == [
        (15, 20, "GPE"),
        (24, 32, "GPE"),
    ], "Vuelve a revisar las entidades en el tercer ejemplo."
    assert TRAINING_DATA[3][1]["entities"] == [
        (0, 6, "GPE")
    ], "Vuelve a revisar las entidades en el cuarto ejemplo."

    __msg__.good(
        "¡Muy buen trabajo!  Una vez el modelo logra buenos resultados detectando entidades GPE "
        "en los comentarios de los viajeros, podrías añadir un componente basado "
        "en reglas para determinar si la entidad es un destino turístico en "
        "este contexto. Por ejemplo, puedes resolver los tipos de entidades en relación con un knowledge base o "
        "buscarlas en un wiki de viajes."
    )
