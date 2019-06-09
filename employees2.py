myfile = open("employees2.txt", "a+")
myfile.seek(0)
print(myfile.read())