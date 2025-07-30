def nonempty_lines(name):
    with open(name, encoding="utf-8") as file:
        for i in file.readlines():
            if len(i.strip("\n")) > 25:
                yield "..."
            elif len(i.strip("\n")) > 0:
                yield i.strip("\n")