email = input("Enter your email: ")

if email.count("@")== 1:
    if email.count(".") >= 1:
        print("Success")
    else:
        print("Invalid email")
else:
    print("Invalid email")
