with open("Ch-9 File Input-Output.md") as f: #wihle using with you don't have to close the file
    data=f.read()
    print(data)
#this closes the file automatically