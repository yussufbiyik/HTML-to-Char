import re, argparse


parser = argparse.ArgumentParser(description='Convert a html file to char variables for NodeMCU WebServers.')
parser.add_argument('-f', '--file', type=str, metavar='', help='File name including file format. Default is index.html.')
parser.add_argument('-o', '--out', type=str, metavar='', help='File name of output. Default is result.txt.')
args = parser.parse_args()

if isinstance(args.file, str):
    filename = args.file
else:
    filename = "index.html"
if isinstance(args.out, str):
    outfilename = args.out
else:
    outfilename = "result.txt"
    

try:
    targetFile = open(filename,"a+")
    targetFile.seek(0)
    fileLength = sum(1 for line in targetFile)
    targetFile.seek(0)
    
    result = open(outfilename,"w+")
    x=1
    result.write("char *html = ")
    for line in targetFile:
        strippedLine = line.strip()
        if strippedLine != "":
            editedLine = strippedLine.replace("\"","\'")
            result.write("\""+editedLine)
            currentLine = result.tell()
            result.seek(currentLine)
            if x == fileLength:
                result.write("\";\n")
            else:
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