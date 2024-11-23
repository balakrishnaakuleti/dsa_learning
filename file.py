#f = open("file.txt", "x")
f = open("file.txt", "w")

f.write("hello world")

f.close

f = open("file.txt","a")
f.write("\nnew content")
f.close

f = open("file.txt","r")
print(f.read(1))
f.close

