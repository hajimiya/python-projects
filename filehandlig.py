from pathlib import Path
import os

def readfileandfolder():
    path = Path('.')
    items = list(path.rglob('*'))

    for i, item in enumerate(items):
        print(f"{i+1} : {item}")

def createfile():
    try:
        readfileandfolder()
        name = input("Please Tell Me Your File Name : ")
        p = Path(name)

        if not p.exists():
            data = input("What do you want to write in this file?\n")
            with open(p, "w") as fs:
                fs.write(data)
            print("File Created Successfully!")
        else:
            print("This File Already Exists.")

    except Exception as err:
        print(f"An Error Occured: {err}")

def readfile():
    try:
        readfileandfolder()
        name = input("Which File You Want To Read: ")
        p = Path(name)

        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print("\n----- File Content -----")
                print(data)
                print("------------------------")
            print("Read Data Successfully")
        else:
            print("The File Does Not Exist")

    except Exception as err:
        print(f"An Error Occured: {err}")

def updatefile():
    try:
        readfileandfolder()
        name = input("Tell Which File You Want To Update : ")
        p = Path(name)

        if p.exists() and p.is_file():   # ← FIXED here
            print("Press 1 For Changing The Name Of Your File")
            print("Press 2 For OverWriting The Data In Your File")
            print("Press 3 For Appending Some Content In Your File")
            res = int(input("Tell Your Response: "))

            if res == 1:
                name2 = input("Tell Your New File Name : ")
                p2 = Path(name2)
                p.rename(p2)
                print("File Renamed Successfully!")

            elif res == 2:
                data = input("Write New Content (Overwrite): ")
                with open(p, 'w') as fs:
                    fs.write(data)
                print("File Updated Successfully (Overwritten)")

            elif res == 3:
                data = input("Tell What You Want To Append: ")
                with open(p, 'a') as fs:
                    fs.write(" " + data)
                print("File Updated Successfully (Appended)")
            else:
                print("Invalid Option")
        else:
            print("No Such File Exists.")

    except Exception as err:
        print(f"An Error Occured: {err}")

def deletefile():
    try:
        readfileandfolder()
        name = input("Tell Which File You Want To Delete: ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(p)
            print("File Deleted Successfully!")
        else:
            print("No Such File Exists.")
    except Exception as err:
        print(f"An Error Occured: {err}")

print("\nEnter 1 For Creating A File")
print("Enter 2 For Reading A File")
print("Enter 3 For Updating A File")
print("Enter 4 For Deleting A File\n")

check = int(input("Please Tell Your Response: "))

if check == 1:
    createfile()
elif check == 2:
    readfile()
elif check == 3:
    updatefile()
elif check == 4:
    deletefile()
else:
    print("Invalid Input")
