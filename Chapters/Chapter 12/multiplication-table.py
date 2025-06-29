n=int(input("Enter the number: "))

table=[n*i for i in range(1,11)]
print(table)


with open("txt files/multiplication.md" , "a") as f:
    f.write(f"table of {n} \n")
    for i in table:
        f.write(f"{i}\n")
    f.write("\n")