import json
import string
import random
from pathlib import Path


class Bank:

    database = 'data.json'

    data= []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        
        else:
            print("No Such File exists")
   
    except Exception as err:
        print(f"An Exception Occured An {err}")

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accnogen(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spchar = random.choices("!@#$%^&*",k=1)
        id = alpha + num + spchar
        random.shuffle(id)

        return "".join(id)
    


    def createaccount(self):
        info = {
            "name" : input("Enter Your Name : "),
            "age" : int(input("Enter Your Age : ")),
            "email" : input("Enter Your Email-Id : "),
            "pin" : int(input("Enter Your 4 digit Pin : ")),
            "accountno." : Bank.__accnogen(),
            "balance" : 0
        }

        if info['age'] < 18 and len(str(info('pin'))) !=4 :
            print("Sorry You Can Not Create Your Account")
        else:
            print("Account Has Been Created Successfully")

            for i in info:
                print(f"{i} : {info[i]}")
            
            print("Please Note Down Your Account Number")

            Bank.data.append(info)

            Bank.__update()

    def depositmoney(self):
        accno = input("Enter Your Account Number : ")
        pin = int(input("Enter Your Pin : "))

        userdata = [i for i in Bank.data if i['accountno.'] == accno and i['pin'] == pin]

        if userdata == False:
            print("Sorry Data Not Found")

        else:
            amount = int(input("Enter Your Deposit Amount : "))

            if amount < 0 and amount > 10000:
                print("Sorry The Amount IS Below The 0 or Above The 10000 ")

            else:
                userdata[0]['balance'] += amount 
                Bank.__update()
                print("Amount Deposited Successfully!")


    def withdrawmoney(self):
        accno = input("Enter Your Account Number : ")
        pin = int(input("Enter Your Pin : "))

        userdata = [i for i in Bank.data if i['accountno'] == accno and i['pin'] == pin]

        if userdata == False:
            print("Sorry Data Not Found")

        else:
            amount = int(input("Enter Your Withdraw Amount : "))

            if amount > userdata[0]['balance'] :
                print("Sorry You Don't Have That Much Money")

            else:
                userdata[0]['balance'] -= amount 
                Bank.__update()
                print("Amount Withdraw Successfully!")


    def showdetails(self):
        accno = input("Enter Your Account Number : ")
        pin = int(input("Enter Your Pin : "))
     
        userdata = [i for i in Bank.data if i['accountno.'] == accno and i['pin'] == pin]

        print(": Your Account Details :")

        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")

    def updatedetails(self):
        accno = input("Enter Your Account Number : ")
        pin = int(input("Enter Your Pin : "))

        userdata = [i for i in Bank.data if i['accountno.'] == accno and i['pin'] == pin]

        if userdata == False:
            print("Sorry Data Not Found")

        else:
            print("You Can Not Change Age,Account Number And Balance ")

            print("Fill The Details For Change Or Leave It Empty If no Change")

            newdata = {
                "name" : input("Enter New Name or Press Enter For Not Change : "),
                "email" : input("Enter New Email or Press Enter For Not Change : "),
                "pin" : input("Enter New Pin or Press Enter For Not Change : ")
            }

            if newdata['name'] == "":
                newdata['name'] = userdata[0]['name']
          
            if newdata['email'] == "":
                newdata['email'] = userdata[0]['email']

            if newdata['pin'] == "":
                newdata['pin'] = userdata[0]['pin']

            newdata['age'] = userdata[0]['age']
            newdata['accountno.'] = userdata[0]['accountno.']
            newdata['balance'] = userdata[0]['balance']

            if type(newdata['pin']) == str :
                newdata['pin'] = int(newdata["pin"])


            for i in newdata :
                if newdata[i] == userdata[0][i] :
                    continue
                else:
                    userdata[0][i] = newdata[i]

            Bank.__update()

            print("Details Updated Successfully!")     

    def deleteaccount(self):
         accno = input("Enter Your Account Number : ")
         pin = int(input("Enter Your Pin : "))

         userdata = [i for i in Bank.data if i['accountno.'] == accno and i['pin'] == pin]

         if userdata == False:
            print("Sorry Data Not Found")
 
         else:
            check = input("Press Y If You Want To Actually Delete The Account Otherwise Press N")
            
            if check == "n" or check == "N" :
                print("---------")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)

                print("Account Deleted Successfully!")

                Bank.__update()
user = Bank()

print("Press 1 For Creating An Account ")
print("Press 2 For Depositing The Money In The Bank")
print("Press 3 For Withdraing The Money")
print("Press 4 For Details Of Account")
print("Press 5 For Updating The Account")
print("Press 6 For Delete The Account")

res = int(input("Tell Me Your Response :"))

if res == 1:
    user.createaccount()

if res == 2:
    user.depositmoney()  

if res == 3:
    user.withdrawmoney()

if res == 4:
    user.showdetails()

if res == 5:
    user.updatedetails()

if res == 6:
    user.deleteaccount()