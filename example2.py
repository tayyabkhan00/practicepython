file="example2.txt"
with open('file',"w") as file:
    file.write("tayyab\n")
    file.write("btech")
# file.close()

with open('file',"r") as file:
 content = file.read()
print(content)
