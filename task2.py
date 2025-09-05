file_name = "output.txt"
text=input("Enter text to write to the file: ")
with open(file_name, "w") as file:
    file.write(text + "\n")
print("Data successfully written to", file_name)
extra_text = input("Enter additional text to append : ")
with open(file_name, "a") as file:
    file.write(extra_text + "\n")
print("Data successfully appended.")
with open(file_name, "r") as file:
    for line in file:
        print(line.strip())