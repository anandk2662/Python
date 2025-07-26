#program to replace words from a file to ###

words=["Lion","king"] #selecting the words to replace
with open("file.txt") as f:
    content=f.read() #reading the file
for word in words:
    content=content.replace(word,"#"*len(word)) # for each word we are updating the content

with open("file.txt","w") as f:
    f.write(content) #writing the file to to replace the word