file_name = input("input keyword :")
file = open(f"{file_name}.txt", "w")
file.write("file content")
file.close
