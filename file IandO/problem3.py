#Program to write the tebles from 2 to 20

def generatetables(n):
    table="" #empty string 
    for i in range(1,11):
        table+=f"{n}X{i}={n*i}\n" #storing the tables of of each number from 1 to 10 in table

    with open(f"tables/tables_{n}.txt","w") as f:
        f.write(table)  #writing each table on a unique .txt file 

for i in range(2,21):
    generatetables(i)