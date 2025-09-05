file_name = "sample.txt"
try:
    with open(file_name, "r") as file:
        file1 = file.readlines()
        print("Reading file content:")
        for line in file1:
            print(line.strip())
except FileNotFoundError:
    print("The File ",file_name," not found")

