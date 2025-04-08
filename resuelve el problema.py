algo_dict = {
            "1": "_",
            "2": "__",
            "3": "___"
            "4": "____",
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in algo_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(algo_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("Error 404: No se ha encontrado esa palabra")
