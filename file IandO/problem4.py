# replacing the word donkey form file.txt with lion
word="Donkey" #selecting the word to replace
with open("file.txt") as f:
    content=f.read() #reading the file
contentnew=content.replace("Donkey","Lion")
with open("file.txt","w") as f:
    f.write(contentnew) #writing the file to to replace the word