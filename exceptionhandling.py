print("perform the division of two numbers")
a = int(input("Enter Number 1:"))
b = int(input("Enter Number 2:"))

try:
    c = b/a
except Exception as e:
    print("Please Enter The Correct Value Of Number 1 (Not Enter Zero)")
 
else:
    print(f"The Division Is : {c}\nDivision Successfull")
      
finally:
    print("Division Operation Finished")
    
