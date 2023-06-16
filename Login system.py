i = 1
while i < 4:
    Username = str(input("Enter username: "))
    Password = str(input("Enter password: "))
    if Username == "Godfred" and Password == "student@1":
        print("Success")
        break
    elif i == 3:
        print("Wrong Credential")
    i += 1