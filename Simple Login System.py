username = input("Enter username: ")
password = input("Enter Password: ")
if username == "admin" or username=="Admin" :
    if password == "1234":
        print("Access Granted")
    else: 
     print("Access Denied")
else: 
    print("Access Denied")
