def readfile(path):
    data = list()
    buffer = str()

    with open(path, "r") as file:
        for line in file:
            if not line.isspace():
                if line.strip()[-1] == ";":
                    data.append(buffer + line.strip())
                    buffer = str()
                else:
                    buffer = buffer + line.strip() + "\n"

    return data

