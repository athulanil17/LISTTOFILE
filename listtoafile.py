thelist=input("Enter the list of items:")
lst=thelist.split(" ")
lists=list(lst)
print(lists)
with open("list.txt","w") as file:
    for items in lists:
        file.write(items+"\n")
    file.close()
