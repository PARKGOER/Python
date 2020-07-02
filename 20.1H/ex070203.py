f=open("C:\\Users\\박정호\\Desktop\\Python\\newfile.txt",'r')
for i in range(1,11) :
    line=f.readline()
    print(line,end="")
f.close()
