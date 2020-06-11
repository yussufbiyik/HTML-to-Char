import re

try:
    targetFile = open("index.txt","a+")
    targetFile.seek(0)
    fileLength = sum(1 for line in targetFile)
    targetFile.seek(0)
    
    result = open("result.txt","w+")
    x=1
    result.write("char *html = ")
    for line in targetFile:
        if line != "\n":
            editedLine = line.replace("\"","\'")
            result.write("\""+editedLine)
            currentLine = result.tell()
            if x == fileLength:
                result.seek(currentLine)
                result.write("\";\n")
            else:
                result.seek(currentLine-2)
                result.write("\"\n")
            print("Line completed.")
            x = x+1  
        else:
            print("Skipped empty line.")
            x = x+1 
finally:
    targetFile.close()
    result.close()
    print("Proccess ended, conversion complete.")