def txt_to_dict():
    with open("planets.txt", encoding="utf-8") as file:
        for i in file.read.split("\n\n"):
            yield set(i)