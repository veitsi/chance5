fi = open("dev.txt","r")
fo=open("dev.js","w")
fo.write("var base=[]; base['dev']=[")
for line in fi:
        line = line[:-1]
        print(line)
        fo.write('"'+line+'",')
fo.write("];")
fi.close()


fi = open("qa.txt","r")
fo.write("base['qa']=[")
for line in fi:
        line = line[:-1]
        print(line)
        fo.write('"'+line+'",')
fo.write("];")