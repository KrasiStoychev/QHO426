line = ""
inputfilename = input("Plase eneter name of file : ?")
inputfile = open(inputfilename,'r')
print(f"Opening file {inputfilename} , for reading.")

for line in inputfile:
    print("line",end = "")