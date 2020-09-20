def read_File_Content(path):
    c=0
    with open(path, "r") as file:
        for line in file:
            c+=1
            if len(line.strip())!=0:
                print(f"line no {c} is not space")
            else:
                print(f"line no {c} is space")